// The site's configuration as astro.config.mjs and the scripts read it:
// site.config.mjs's values with every option it leaves out filled in, each
// "auto" settled against the repository, and the required values checked.
// `node scripts/config.mjs` prints the result, so a person can see what the
// sync will read before it runs. site.config.mjs itself runs no code, so the
// pages that show the title import it directly.
import { execFileSync, spawnSync } from "node:child_process";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, extname, posix, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as given from "../site.config.mjs";

export const SITE_DIR = resolve(dirname(fileURLToPath(import.meta.url)), "..");
export const REPO_ROOT = resolve(SITE_DIR, "..");
export const BUNDLE_DIR = resolve(REPO_ROOT, ".lokf", "knowledge");

const fail = (what) => {
  throw new Error(`site.config.mjs: ${what}`);
};
const has = (rel) => existsSync(resolve(REPO_ROOT, rel));
const isDir = (rel) => has(rel) && statSync(resolve(REPO_ROOT, rel)).isDirectory();
const isFile = (rel) => has(rel) && statSync(resolve(REPO_ROOT, rel)).isFile();

/** A required value: a string with no placeholder left in it. */
function required(name) {
  const value = given[name];
  if (typeof value !== "string" || value === "") fail(`${name} must be a string`);
  if (/<[A-Z_]+>/.test(value)) fail(`${name} still holds a placeholder (${value}); ktl-website's Step 1 fills it`);
  return value;
}

// ---- the addresses ---------------------------------------------------------

export const REPO = required("REPO");
export const REPO_URL = `https://github.com/${REPO}`;
export const CUSTOM_DOMAIN = given.CUSTOM_DOMAIN ?? null;
// A custom domain serves the site at its root; a project site lives under
// the owner's Pages domain at /<repository>/.
export const SITE = CUSTOM_DOMAIN ? `https://${CUSTOM_DOMAIN}` : required("SITE").replace(/\/$/, "");
export const BASE = CUSTOM_DOMAIN ? "" : required("BASE").replace(/\/$/, "");
export const SITE_URL = SITE + BASE;
export const TITLE = required("TITLE");
export const DESCRIPTION = required("DESCRIPTION");
export const BRANCH = given.BRANCH ?? "main";

// Links to repository files name the commit the site was built from, so a
// reader lands on the text the page was rendered from.
export const REF = (() => {
  if (process.env.GITHUB_SHA) return process.env.GITHUB_SHA;
  try {
    return execFileSync("git", ["-C", REPO_ROOT, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
  } catch {
    return BRANCH;
  }
})();

// ---- what the site shows beside the bundle ---------------------------------

/** An option left out or set to "auto" takes `fallback` when the repository has it, and null otherwise. */
function settle(name, fallback, present) {
  const value = given[name] === undefined ? "auto" : given[name];
  if (value === "auto") return present(fallback) ? fallback : null;
  if (value !== null && !present(value)) fail(`${name} names ${value}, which is not in the repository`);
  return value;
}

export const ASSETS = settle("ASSETS", ".assets", isDir);

// The Knowledge Trust Ladder logo, which "auto" takes: a copy the repository
// already holds, outside this site and outside a skill's templates, the one
// nearest the root first, or else the copy this site carries in src/assets/.
// The -dark.svg file beside it is the dark version when there is one.
const KTL_LOGO = "knowledge-trust-ladder-logo.svg";
function ktlLogo() {
  const site = relative(REPO_ROOT, SITE_DIR).replaceAll("\\", "/");
  const ls = spawnSync("git", ["-C", REPO_ROOT, "ls-files", "--cached", "--others", "--exclude-standard", "--", `*${KTL_LOGO}`], {
    encoding: "utf8",
  });
  const own = (ls.status === 0 ? ls.stdout.split("\n") : [KTL_LOGO, `.assets/${KTL_LOGO}`])
    .filter((f) => (f === KTL_LOGO || f.endsWith(`/${KTL_LOGO}`)) && !f.startsWith(`${site}/`) && !f.includes("templates/website/"))
    .filter(isFile)
    .sort((a, b) => a.split("/").length - b.split("/").length || (a < b ? -1 : a > b ? 1 : 0));
  const light = own[0] ?? `${site}/src/assets/${KTL_LOGO}`;
  const dark = light.replace(/\.svg$/, "-dark.svg");
  return { light, dark: isFile(dark) ? dark : light };
}

export const LOGO = (() => {
  const value = given.LOGO === undefined ? "auto" : given.LOGO;
  if (value === null) return null;
  const logo = value === "auto" ? ktlLogo() : typeof value === "string" ? { light: value } : value;
  const light = logo.light ?? fail("LOGO needs at least a light file");
  const dark = logo.dark ?? light;
  const favicon = logo.favicon ?? (extname(light) === ".svg" ? light : null);
  for (const file of [light, dark, favicon]) {
    if (file && !isFile(file)) fail(`LOGO names ${file}, which is not in the repository`);
  }
  return { light, dark, favicon };
})();
/** The generated logo files, named by their source's type, and the favicon the site serves. */
export const LOGO_FILES = LOGO ? { light: `logo-light${extname(LOGO.light)}`, dark: `logo-dark${extname(LOGO.dark)}` } : null;
export const FAVICON = LOGO?.favicon ? `/favicon${extname(LOGO.favicon)}` : "/favicon.svg";

// docsPages() keeps its list here once read. It is declared before HOME,
// which asks for the list while this module is still loading.
let docsPagesRead = null;

// The mkdocs site this one replaces: four of mkdocs.yml's settings, in its
// own keys. "auto" reads them from mkdocs.yml at the root, and an object
// gives them here once mkdocs.yml is gone. They settle "auto" DOCS (the
// folder, the order of the pages, the pages left out), the files served
// beside the pages, and the redirects that keep mkdocs' addresses.
export const MKDOCS = (() => {
  const value = given.MKDOCS === undefined ? "auto" : given.MKDOCS;
  if (value === null) return null;
  let settings;
  if (value === "auto") {
    if (!isFile("mkdocs.yml")) return null;
    settings = readMkdocsYml(readFileSync(resolve(REPO_ROOT, "mkdocs.yml"), "utf8"));
  } else if (typeof value === "object" && !Array.isArray(value)) settings = value;
  else fail('MKDOCS must be "auto", null, or mkdocs.yml\'s settings as { docs_dir, nav, exclude_docs, site_url }');
  const docs_dir = (settings.docs_dir ?? "docs").replace(/\/$/, "");
  if (!isDir(docs_dir)) {
    if (value === "auto") return null;
    fail(`MKDOCS names docs_dir ${docs_dir}, which is not a folder in the repository`);
  }
  if (settings.nav !== undefined && !Array.isArray(settings.nav)) fail("MKDOCS.nav must be a list, as in mkdocs.yml");
  if (settings.exclude_docs !== undefined && typeof settings.exclude_docs !== "string") fail("MKDOCS.exclude_docs must be a string, as in mkdocs.yml");
  return {
    docs_dir,
    nav: settings.nav ?? [],
    exclude_docs: settings.exclude_docs ?? "",
    site_url: typeof settings.site_url === "string" ? settings.site_url.replace(/\/$/, "") : null,
    // mkdocs gives a page a folder address unless this is false, and only
    // folder addresses are kept.
    use_directory_urls: settings.use_directory_urls !== false,
  };
})();

/**
 * The four settings the site takes from mkdocs.yml, read from its block
 * YAML with no YAML parser, so that config.mjs runs before npm ci. A value
 * is a plain or quoted scalar, a block scalar (| or >), or, for nav, a list
 * whose entries are a file, `Title: file`, or `Title:` over a list of its
 * own. Every other key is passed over, with the Python tags mkdocs.yml can
 * hold. A nav in flow style, [a, b], stops with a pointer to MKDOCS.
 */
function readMkdocsYml(text) {
  const lines = text.split(/\r?\n/);
  const indent = (line) => line.match(/^ */)[0].length;
  const blank = (line) => /^\s*(?:#.*)?$/.test(line);
  const scalar = (raw) => {
    const s = raw.trim();
    if (/^'.*'$/.test(s)) return s.slice(1, -1).replaceAll("''", "'");
    if (/^".*"$/.test(s)) return s.slice(1, -1).replace(/\\(["\\])/g, "$1").replaceAll("\\n", "\n");
    return s.replace(/\s+#.*$/, "");
  };
  const list = (block) => {
    const items = [];
    const at = indent(block[0]);
    for (let i = 0; i < block.length; ) {
      const line = block[i];
      if (indent(line) !== at || !/^-(?:\s|$)/.test(line.slice(at))) fail(`mkdocs.yml's nav has a line this reader cannot place: "${line.trim()}"; give MKDOCS its settings in site.config.mjs`);
      let j = i + 1;
      while (j < block.length && indent(block[j]) > at) j++;
      const entry = line.slice(at + 1).trim();
      const pair = entry.match(/^("[^"]*"|'[^']*'|[^"':#][^:#]*?):(?:\s+(.*))?$/);
      if (!pair) items.push(scalar(entry));
      else if (pair[2] !== undefined && scalar(pair[2]) !== "") items.push({ [scalar(pair[1])]: scalar(pair[2]) });
      else items.push({ [scalar(pair[1])]: j > i + 1 ? list(block.slice(i + 1, j)) : null });
      i = j;
    }
    return items;
  };
  const settings = {};
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/^(docs_dir|site_url|use_directory_urls|exclude_docs|nav):(?:\s+(.*?))?\s*$/);
    if (!m) continue;
    const [, key, inline = ""] = m;
    // The value's own lines: those indented under the key, and for nav a
    // list at the key's own indent, which YAML allows too.
    let j = i + 1;
    while (j < lines.length && (blank(lines[j]) || indent(lines[j]) > 0 || (key === "nav" && /^-(?:\s|$)/.test(lines[j])))) j++;
    const block = lines.slice(i + 1, j);
    i = j - 1;
    if (/^[|>]/.test(inline)) {
      const body = block.slice(0, block.findLastIndex((line) => line.trim() !== "") + 1);
      const at = Math.min(...body.filter((line) => line.trim() !== "").map(indent));
      const kept = body.map((line) => line.slice(at));
      settings[key] = inline.startsWith("|") ? kept.join("\n") + "\n" : kept.join(" ") + "\n";
    } else if (key === "nav") {
      if (inline.startsWith("[")) fail("mkdocs.yml's nav is in flow style, which this reader does not read; give MKDOCS its settings in site.config.mjs");
      const items = block.filter((line) => !blank(line));
      settings.nav = items.length ? list(items) : [];
    } else if (key === "use_directory_urls") {
      settings[key] = !/^(?:false|no|off)$/i.test(scalar(inline));
    } else {
      settings[key] = scalar(inline);
    }
  }
  return settings;
}

/** A gitignore pattern, as exclude_docs writes one, as a regular expression over a path. */
function gitignorePattern(pattern) {
  const anchored = pattern.startsWith("/") || pattern.slice(0, -1).includes("/");
  const body = pattern
    .replace(/^\//, "")
    .split(/(\*\*\/|\/\*\*|\*\*|\*|\?|\[[^\]]*\])/)
    .map((part) => {
      if (part === "**/") return "(?:.*/)?";
      if (part === "/**") return "(?:/.*)?";
      if (part === "**") return ".*";
      if (part === "*") return "[^/]*";
      if (part === "?") return "[^/]";
      if (/^\[[^\]]*\]$/.test(part)) return part.replace(/^\[!/, "[^");
      return part.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    })
    .join("");
  return new RegExp(`${anchored ? "^" : "^(?:.*/)?"}${body}$`);
}

// The pages mkdocs leaves out: a file or folder whose name starts with a dot
// and the templates/ folder, which mkdocs leaves out unasked, then each line
// of exclude_docs, the last that matches deciding.
const MKDOCS_EXCLUDE = MKDOCS
  ? [".*", "/templates/", ...MKDOCS.exclude_docs.split("\n")]
      .map((line) => line.trim())
      .filter((line) => line && !line.startsWith("#"))
      .map((line) => {
        const negated = line.startsWith("!");
        const pattern = negated ? line.slice(1) : line;
        return { negated, folder: pattern.endsWith("/"), re: gitignorePattern(pattern.replace(/\/$/, "")) };
      })
  : [];

/** Whether mkdocs leaves out a path under its docs folder: the file itself, or a folder it sits in. */
export function mkdocsExcludes(path) {
  const parts = path.split("/");
  let excluded = false;
  for (const rule of MKDOCS_EXCLUDE) {
    const hit = parts.some((_, i) => (i < parts.length - 1 || !rule.folder) && rule.re.test(parts.slice(0, i + 1).join("/")));
    if (hit) excluded = !rule.negated;
  }
  return excluded;
}

/** mkdocs' nav as a list of { title, file }, sections opened in order; a link that leaves the site is skipped. */
function mkdocsNav(items = MKDOCS?.nav ?? []) {
  return items.flatMap((item) => {
    if (typeof item === "string") return /^[a-z]+:/i.test(item) ? [] : [{ title: null, file: item }];
    if (!item || typeof item !== "object") return [];
    return Object.entries(item).flatMap(([title, entry]) =>
      Array.isArray(entry) ? mkdocsNav(entry) : typeof entry === "string" && !/^[a-z]+:/i.test(entry) ? [{ title, file: entry }] : [],
    );
  });
}

export const DOCS = (() => {
  const value = given.DOCS === undefined ? "auto" : given.DOCS;
  if (value === null) return null;
  const docs =
    value === "auto"
      ? { dir: MKDOCS?.docs_dir ?? "docs" }
      : typeof value === "string"
        ? { dir: value }
        : { dir: value.dir ?? "docs", groups: value.groups };
  if (!isDir(docs.dir)) {
    if (value === "auto") return null;
    fail(`DOCS names ${docs.dir}, which is not a folder in the repository`);
  }
  // "auto" over an mkdocs site takes its nav as the pages' order and their
  // labels. A page the nav does not list follows by title, as in mkdocs.
  const nav =
    value === "auto" && MKDOCS
      ? mkdocsNav()
          .filter((entry) => entry.file.endsWith(".md"))
          .map((entry) => ({ name: posix.normalize(entry.file).slice(0, -3), label: entry.title }))
      : null;
  return { dir: docs.dir, groups: docs.groups ?? null, nav };
})();

/**
 * A docs page's address under the site's base, as Starlight gives it: each
 * folder and the file name in lower case, with the characters
 * github-slugger drops dropped, and an index page at its folder's address.
 */
export function docsRoute(name) {
  const slug = name
    .split("/")
    .map((part) => part.toLowerCase().replace(/[^\p{L}\p{M}\p{N}\p{Pc}\- ]/gu, "").replace(/ /g, "-"))
    .join("/");
  const folder = slug === "index" ? "" : slug.replace(/\/index$/, "");
  return folder ? `/docs/${folder}/` : "/docs/";
}

export const CHANGELOG = (() => {
  const value = given.CHANGELOG === undefined ? "auto" : given.CHANGELOG;
  if (value === null) return null;
  const file = value === "auto" ? "CHANGELOG.md" : value;
  if (!isFile(file)) {
    if (value === "auto") return null;
    fail(`CHANGELOG names ${file}, which is not in the repository`);
  }
  // A release page needs one released version in Keep a Changelog form.
  if (/^## \[[^\]]+\] - \d{4}-\d{2}-\d{2}/m.test(readFileSync(resolve(REPO_ROOT, file), "utf8"))) return file;
  if (value === "auto") return null;
  return fail(`${file} has no "## [version] - YYYY-MM-DD" heading, which a release page needs`);
})();

// The tag a release carries, with {version} for its number, so that a
// release page can link the repository and the bundle as they stood at the
// release. null links nothing.
export const RELEASE_TAG = (() => {
  const value = given.RELEASE_TAG === undefined ? "v{version}" : given.RELEASE_TAG;
  if (value === null) return null;
  if (typeof value !== "string" || !value.includes("{version}")) fail("RELEASE_TAG must hold {version}, such as \"v{version}\", or be null");
  return value;
})();

export const PAGES = (given.PAGES ?? []).map((p) => {
  if (!p.slug || !p.source) fail("each PAGES entry needs a slug and a source");
  if (!isFile(p.source)) fail(`PAGES names ${p.source}, which is not in the repository`);
  if (p.retells && !isFile(p.retells)) fail(`PAGES names ${p.retells}, which ${p.source} retells, and it is not in the repository`);
  // A retelling's level is the words a reader chooses it by, its label unless given.
  const label = p.label ?? p.slug;
  return { slug: p.slug, source: p.source, label, retells: p.retells ?? null, level: p.level ?? label };
});

// ---- the schema's pages and the data, which the repository's commands build --

/** A folder's justfile, by any name just reads (justfile in any case, or .justfile), or null. */
function justfileIn(dir) {
  if (!isDir(dir)) return null;
  const name = readdirSync(resolve(REPO_ROOT, dir))
    .filter((n) => /^\.?justfile$/i.test(n) && isFile(posix.join(dir, n)))
    .sort()[0];
  return name ? posix.join(dir, name) : null;
}

/**
 * Whether a justfile has a recipe of this name: a line that opens it, with or
 * without parameters and their defaults, and not an assignment such as
 * `name := value`. website-preflight.sh's has_recipe uses the same pattern.
 */
function hasRecipe(justfile, recipe) {
  const opens = new RegExp(`^@?${recipe}(?:[ \\t]+[^:=\\s][^:]*)?:(?!=)`);
  return readFileSync(resolve(REPO_ROOT, justfile), "utf8")
    .split("\n")
    .some((line) => opens.test(line));
}

/**
 * The first of these folders whose justfile has the recipe, as { dir, build }.
 * dir is the folder the recipe writes, `out` under that folder. build is the
 * command that runs the recipe from the repository's root. just runs a recipe
 * in its justfile's own folder.
 */
function recipeIn(dirs, recipe, out) {
  for (const dir of dirs) {
    const justfile = dir ? justfileIn(dir) : null;
    if (justfile && hasRecipe(justfile, recipe)) {
      return { dir: posix.join(dir, out), build: dir === "." ? `just ${recipe}` : `just --justfile ${justfile} ${recipe}` };
    }
  }
  return null;
}

/** A linkmo project's folder, as its answers file at the root names it, or null. */
function linkmoDir() {
  if (!isFile(".copier-answers.linkmo.yml")) return null;
  const m = readFileSync(resolve(REPO_ROOT, ".copier-answers.linkmo.yml"), "utf8").match(/^linkmo_dir:\s*["']?([^"'\s#]+)["']?\s*$/m);
  // The folder goes into a shell command, so only a name linkmo's own question accepts is used.
  return m && /^[A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?$/.test(m[1]) && isDir(m[1]) ? m[1] : null;
}

/** A { dir, build } option given in full or as a folder alone; build is the command that writes the folder, or null. */
function folderOption(name, value) {
  const option = typeof value === "string" ? { dir: value } : value;
  if (typeof option?.dir !== "string" || option.dir === "") fail(`${name} needs a dir, the folder from the repository root`);
  const dir = posix.normalize(option.dir.replaceAll("\\", "/")).replace(/\/$/, "");
  if (dir.startsWith("..") || dir.startsWith("/")) fail(`${name}.dir must be a folder inside the repository`);
  const build = option.build ?? null;
  if (build !== null && typeof build !== "string") fail(`${name}.build must be a command, or null`);
  if (build === null && !isDir(dir)) fail(`${name} names ${dir}, which is not in the repository, and no build command to write it`);
  return { dir, build };
}

// The schema's pages: LinkML's gen-doc writes one per class, slot,
// enumeration and type, which the site renders under a Schema topic. "auto"
// takes the first of the repository's root, a linkmo project's folder and
// the linkml-sidecar's .linkml/ whose justfile has a gen-doc recipe, which
// writes the pages to docs/elements there.
export const SCHEMA = (() => {
  const value = given.SCHEMA === undefined ? "auto" : given.SCHEMA;
  if (value === null) return null;
  if (value !== "auto") return folderOption("SCHEMA", value);
  return recipeIn([".", linkmoDir(), ".linkml"], "gen-doc", "docs/elements");
})();

// The data: a folder of SQLite databases, which the site serves under
// /browse/ beside their Datasette metadata, and a page that opens each one in
// Datasette Lite. Left out, it is null: the databases go on a public site,
// so a person turns this on. "auto" takes the browse/ folder a linkmo
// project's build-browse recipe writes.
export const BROWSE = (() => {
  const value = given.BROWSE ?? null;
  if (value === null) return null;
  if (value !== "auto") return folderOption("BROWSE", value);
  return recipeIn([linkmoDir()], "build-browse", "browse");
})();

// The workspace of a domain host, whose graph.json the graph page draws
// beside the bundle's own: the folder under the site where the
// knowledge-federation workflow serves it, or null. The workflow always
// serves it at workspace/, so the setting says only whether the page offers
// it. The workflow adds the folder after the site is built, so the page
// reads it when a reader opens the view.
export const WORKSPACE = (() => {
  const value = given.WORKSPACE === undefined ? "auto" : given.WORKSPACE;
  if (value === null || value === false) return null;
  if (value === true) return "workspace";
  if (value === "auto") return isFile(".github/workflows/knowledge-federation.yaml") ? "workspace" : null;
  fail(`WORKSPACE must be "auto", true or null, since the federation workflow serves the workspace at workspace/ under the site, not ${JSON.stringify(value)}`);
})();

/** Where the graph page finds the workspace: its folder, its graph.json under the site's base, and its index as a full address; null with no workspace. */
export function workspaceLinks() {
  return WORKSPACE ? { folder: WORKSPACE, graph: `${BASE}/${WORKSPACE}/graph.json`, index: `${SITE_URL}/${WORKSPACE}/index.md` } : null;
}

/** The first `# ` line of a file outside fenced code, or null. */
function firstTitle(rel) {
  let fence = null;
  for (const line of readFileSync(resolve(REPO_ROOT, rel), "utf8").split("\n")) {
    const m = line.match(/^\s*(`{3,}|~{3,})/);
    if (fence) {
      if (m && m[1][0] === fence[0] && m[1].length >= fence.length) fence = null;
    } else if (m) fence = m[1];
    else if (/^# /.test(line)) return line.slice(2).trim();
  }
  return null;
}

// The buttons under the home page's title when HOME.actions is not set: the
// bundle, the docs' architecture page when the site has one, the health page
// and the graph.
function defaultActions() {
  return [
    { text: "Browse the bundle", link: "/knowledge/", icon: "right-arrow" },
    ...(docsPages().includes("architecture") ? [{ text: "Architecture", link: "/docs/architecture/", variant: "secondary" }] : []),
    { text: "Bundle health", link: "/health/", variant: "secondary" },
    { text: "Knowledge graph", link: "/graph/", variant: "secondary" },
  ];
}

export const HOME = (() => {
  const home = { source: "auto", tagline: null, actions: null, ...(given.HOME ?? {}) };
  let source = home.source ?? null;
  if (source === "auto") source = isFile("README.md") && firstTitle("README.md") ? "README.md" : null;
  else if (source !== null && !isFile(source)) fail(`HOME.source names ${source}, which is not in the repository`);
  const tagline = home.tagline ?? null;
  if (tagline && typeof tagline === "object" && !isFile(tagline.boldLineOf ?? "")) {
    fail("HOME.tagline.boldLineOf names a file that is not in the repository");
  }
  return { source, tagline, actions: home.actions ?? defaultActions() };
})();

// ---- the bundle and the docs, as folders and files -------------------------

/** The bundle's concept groups: its top-level folders, in name order. */
export function bundleGroups() {
  return readdirSync(BUNDLE_DIR)
    .filter((name) => !name.startsWith(".") && statSync(resolve(BUNDLE_DIR, name)).isDirectory())
    .sort();
}

/** A group's folder name as words, so young-readers reads "Young readers". */
export function groupLabel(group) {
  const words = group.replace(/[-_]+/g, " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
}

/** Every concept's ID: its path in the bundle without `.md`, index and log files left out. */
export function conceptIds() {
  const ids = [];
  const walk = (dir, prefix) => {
    for (const name of readdirSync(dir).sort()) {
      if (name.startsWith(".")) continue;
      const full = resolve(dir, name);
      if (statSync(full).isDirectory()) walk(full, prefix + name + "/");
      else if (name.endsWith(".md") && name !== "index.md" && !(prefix === "" && name === "log.md"))
        ids.push(prefix + name.slice(0, -3));
    }
  };
  if (existsSync(BUNDLE_DIR)) walk(BUNDLE_DIR, "");
  return ids;
}

/**
 * Every docs page, as its path under the docs folder without `.md`. The
 * pages are the files git sees there, tracked or untracked but never
 * ignored, so a folder a generator writes stays out. Where there is no git,
 * they are the files a walk of the folder finds.
 * A file PAGES names has a page of its own and is left out here, and so is
 * the schema's folder, which has a topic of its own, and a page mkdocs
 * leaves out of the folder it reads. The list is read once per process,
 * since the home page's buttons, the links and the sync all ask for it.
 */
export function docsPages() {
  if (docsPagesRead) return docsPagesRead;
  if (!DOCS) return (docsPagesRead = Object.freeze([]));
  const dir = DOCS.dir;
  const extra = new Set(PAGES.map((p) => p.source));
  const schema = SCHEMA ? `${SCHEMA.dir}/` : null;
  const mkdocs = MKDOCS && MKDOCS.docs_dir === dir;
  return (docsPagesRead = Object.freeze(
    filesIn(dir)
      .filter((f) => f.endsWith(".md") && !extra.has(f) && !(schema && f.startsWith(schema)) && isFile(f))
      .map((f) => f.slice(dir.length + 1, -3))
      .filter((name) => !(mkdocs && mkdocsExcludes(`${name}.md`)))
      .sort(),
  ));
}

/** The files git sees under a folder, tracked or untracked but never ignored, or the files a walk finds where there is no git. */
function filesIn(dir) {
  const ls = spawnSync("git", ["-C", REPO_ROOT, "ls-files", "--cached", "--others", "--exclude-standard", "--", dir], {
    encoding: "utf8",
  });
  if (ls.status === 0) return ls.stdout.split("\n").filter((f) => f.startsWith(dir + "/"));
  const files = [];
  const walk = (d, prefix) => {
    for (const name of readdirSync(d).sort()) {
      const full = resolve(d, name);
      if (statSync(full).isDirectory()) walk(full, prefix + name + "/");
      else files.push(prefix + name);
    }
  };
  walk(resolve(REPO_ROOT, dir), dir + "/");
  return files;
}

// The site's own top folders and files, which an mkdocs file or address may
// not take. The schema's folder is shared: its pages are folders, and a
// file such as schema/<name>.yaml sits beside them.
const OWN_FOLDERS = new Set(["_astro", "assets", "browse", "changelog", "docs", "graph", "health", "knowledge", "og", "pagefind", "workspace"]);
const OWN_FILES = new Set(["CNAME", "index.md", "llms.txt", "llms-full.txt", "favicon.svg", "favicon.png", "favicon.ico"]);

/**
 * The files mkdocs copied from its docs folder into its site, which this site
 * serves at the same addresses: each file git sees there that is not a page,
 * outside js/ and css/, which held mkdocs' own scripts and styles, outside
 * the schema's folder, and not left out by exclude_docs. A file whose
 * address the site already takes is skipped, with the reason.
 */
export function mkdocsFiles() {
  if (!MKDOCS) return { served: [], skipped: [] };
  const dir = MKDOCS.docs_dir;
  const schema = SCHEMA ? `${SCHEMA.dir}/` : null;
  const served = [];
  const skipped = [];
  for (const file of filesIn(dir)) {
    const path = file.slice(dir.length + 1);
    if (file.endsWith(".md") || /^(?:js|css)\//.test(path) || (schema && file.startsWith(schema)) || mkdocsExcludes(path) || !isFile(file)) continue;
    const top = path.split("/")[0];
    if (top === path ? OWN_FILES.has(path) : OWN_FOLDERS.has(top)) skipped.push({ file, why: `the site writes its own /${top === path ? path : `${top}/`}` });
    else if (path === "index.html" || path.endsWith("/index.html")) skipped.push({ file, why: "a page of the site takes its address" });
    else served.push({ file, path });
  }
  return { served, skipped };
}

// The kinds of page gen-doc writes, by the word that opens its title
// ("# Class: Action"), and the sidebar group each sits in, in the order
// gen-doc's own index lists them.
export const SCHEMA_KINDS = { Class: "Classes", Slot: "Slots", Enum: "Enumerations", Type: "Types", Subset: "Subsets" };

let schemaPagesRead = null;

/**
 * The schema's pages, its index left out: each page's name, the file name
 * without `.md` and so its address under /schema/; its label, the element's
 * name from its title; its kind; and its file from the repository root. A
 * page of no kind, the schema's own, has a page and no place in the sidebar.
 * The folder is read once it exists, since the sync builds it first.
 *
 * The pages are read from one flat folder, as gen-doc writes them by default.
 * Its --subfolder-type-separation option writes each kind to a folder of its
 * own. The topic would then show no element, and the overview's links would
 * point at GitHub, where the folder is not committed, so such a folder stops
 * the sync here.
 */
export function schemaPages() {
  if (schemaPagesRead) return schemaPagesRead;
  if (!SCHEMA || !isDir(SCHEMA.dir)) return [];
  const markdownIn = (dir) => (isDir(dir) ? readdirSync(resolve(REPO_ROOT, dir)).filter((name) => name.endsWith(".md") && isFile(`${dir}/${name}`)) : []);
  const pages = markdownIn(SCHEMA.dir)
    .filter((name) => name !== "index.md")
    .map((name) => {
      const file = `${SCHEMA.dir}/${name}`;
      // A type's title follows its frontmatter's closing line with no line break: "---# Type: String".
      const m = readFileSync(resolve(REPO_ROOT, file), "utf8").match(/^(?:---)?# (Class|Slot|Enum|Type|Subset): *(.+?) *$/m);
      return { name: name.slice(0, -3), label: m ? m[2] : name.slice(0, -3), kind: m ? m[1] : null, file };
    })
    .sort((a, b) => a.label.localeCompare(b.label, "en", { sensitivity: "base" }) || (a.name < b.name ? -1 : 1));
  const nested = ["classes", "slots", "enums", "types", "subsets", "schemas"].filter((sub) => markdownIn(`${SCHEMA.dir}/${sub}`).length > 0);
  if (nested.length > 0 && !pages.some((p) => p.kind)) {
    fail(
      `SCHEMA's folder ${SCHEMA.dir} holds gen-doc's pages in ${nested.map((sub) => `${sub}/`).join(", ")}, as its ` +
        "--subfolder-type-separation option writes them; the site reads one flat folder, gen-doc's default, so build it without that option",
    );
  }
  return (schemaPagesRead = Object.freeze(pages));
}

/**
 * The addresses mkdocs gave the pages, each sent on to the page's address
 * here, so a link or an IRI that names an mkdocs page still reaches it: the
 * schema's pages, which a w3id rule may name, and each docs page. mkdocs
 * served a page at its path under the docs folder, an index or README page
 * at its folder. Astro writes a page per entry that sends the browser on.
 * An address the site takes itself is skipped, with the reason.
 */
export function mkdocsRedirects() {
  if (!MKDOCS || !MKDOCS.use_directory_urls) return { redirects: [], skipped: [] };
  const redirects = [];
  const skipped = [];
  const slugs = new Set(PAGES.map((p) => p.slug));
  const add = (from, to) => {
    const top = from.split("/")[0];
    if (from === "") return;
    if (OWN_FOLDERS.has(top) || top === "schema" || slugs.has(top)) skipped.push({ from: `/${from}/`, why: `the site serves its own /${top}/` });
    else redirects.push({ from: `/${from}`, to: `${BASE}${to}` });
  };
  const docsDir = `${MKDOCS.docs_dir}/`;
  if (SCHEMA && SCHEMA.dir.startsWith(docsDir) && schemaPages().length > 0) {
    const folder = SCHEMA.dir.slice(docsDir.length);
    if (folder !== "schema") {
      add(folder, "/schema/");
      for (const page of schemaPages()) add(`${folder}/${page.name}`, `/schema/${page.name}/`);
    }
  }
  if (DOCS && DOCS.dir === MKDOCS.docs_dir) {
    const names = new Set(docsPages());
    for (const name of names) {
      const at = name.replace(/(?:^|\/)(?:index|README)$/, "");
      if (at !== name && name.endsWith("README") && names.has(name.replace(/README$/, "index"))) continue;
      add(at, docsRoute(name));
    }
  }
  return { redirects, skipped };
}

const DATABASE = /\.(?:sqlite3?|db)$/;
const METADATA = /^metadata\.(?:ya?ml|json)$/;

/**
 * The data's files in BROWSE's folder: each SQLite database, as its file name
 * and the name Datasette gives it, which is the file name without its
 * extension; and the Datasette metadata file, or null. Nothing else in the
 * folder is published. A database with a journal beside it that is not empty
 * stops the sync: a write to it is unfinished or still open, so a copy of the
 * database could be inconsistent. So do two metadata files, since Datasette
 * reads one.
 */
export function browseFiles() {
  if (!BROWSE || !isDir(BROWSE.dir)) return { databases: [], metadata: null };
  const names = readdirSync(resolve(REPO_ROOT, BROWSE.dir))
    .filter((name) => isFile(`${BROWSE.dir}/${name}`))
    .sort();
  const databases = names.filter((name) => DATABASE.test(name)).map((file) => ({ file, name: file.replace(DATABASE, "") }));
  for (const { file } of databases) {
    for (const journal of [`${file}-wal`, `${file}-journal`]) {
      const path = `${BROWSE.dir}/${journal}`;
      if (isFile(path) && statSync(resolve(REPO_ROOT, path)).size > 0) {
        throw new Error(
          `${path} is not empty: a write to ${file} is unfinished or still open, and a copy of it could be torn. ` +
            "Close what has it open, or build it again, then build the site",
        );
      }
    }
  }
  const metadata = names.filter((name) => METADATA.test(name));
  if (metadata.length > 1) throw new Error(`${BROWSE.dir} holds ${metadata.join(" and ")}, and Datasette reads one: keep one`);
  return { databases, metadata: metadata[0] ?? null };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const settled = { REPO, SITE, BASE, TITLE, DESCRIPTION, BRANCH, CUSTOM_DOMAIN, REF, LOGO, ASSETS, DOCS, CHANGELOG, RELEASE_TAG, PAGES, HOME, SCHEMA, BROWSE, WORKSPACE, MKDOCS };
  const mkdocs = MKDOCS ? { mkdocsFiles: mkdocsFiles(), mkdocsRedirects: mkdocsRedirects() } : {};
  console.log(JSON.stringify({ ...settled, docsPages: docsPages(), bundleGroups: bundleGroups(), workspace: workspaceLinks(), ...mkdocs }, null, 2));
}
