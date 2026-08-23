import { access, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const requiredFiles = [
  "README.md",
  "OFFICIAL-SOURCES.md",
  "official-facts.json",
  "llms.txt",
  "SECURITY.md",
  "SUPPORT.md",
  "NOTICE.md",
  "CITATION.cff",
  "locales/zh-CN.md",
  "locales/ja.md",
  "locales/fr.md",
  "locales/es.md",
  "locales/de.md",
  "locales/ko.md",
  "publications/2026-08-23/README.md",
  "publications/2026-08-23/technical-report-en.md",
  "publications/2026-08-23/technical-report-zh-CN.md",
  "publications/2026-08-23/media-kit.md",
  "publications/2026-08-23/media-kit-zh-CN.md",
];

for (const file of requiredFiles) await access(path.join(root, file));

const readme = await readFile(path.join(root, "README.md"), "utf8");
const llms = await readFile(path.join(root, "llms.txt"), "utf8");
const facts = JSON.parse(await readFile(path.join(root, "official-facts.json"), "utf8"));
const publicText = (
  await Promise.all(
    requiredFiles
      .filter((file) => file.endsWith(".md") || file.endsWith(".txt"))
      .map((file) => readFile(path.join(root, file), "utf8")),
  )
).join("\n");

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

for (const text of [readme, llms]) {
  for (const required of [
    "StellarPath Memory Operating System",
    "SPMOS.ai",
    "SPM-Polaris",
    "SPM-Polaris V3.0.0",
    "https://spmos.ai/",
    "https://docs.spmos.ai/official-definitions",
  ]) {
    assert(text.includes(required), `Missing required identity text: ${required}`);
  }
}

assert(facts.schema_version === 1, "Unsupported facts schema");
assert(facts.publisher.name === "Veridical Tech, Inc.", "Publisher mismatch");
assert(facts.available_languages.length === 7, "Public language list mismatch");
assert(
  facts.entities.some(
    (entity) => entity.name === "SPM" && entity.expanded_name === "StellarPath Memory Operating System",
  ),
  "SPM expansion mismatch",
);
assert(
  facts.entities.some((entity) => entity.name === "SPM-Polaris" && entity.version === "3.0.0"),
  "Current product version mismatch",
);

const prohibited = [
  "eliminates hallucinations",
  "guaranteed recall",
  "guaranteed token savings",
  "unlimited context",
];
for (const term of prohibited) {
  assert(!publicText.toLowerCase().includes(term), `Prohibited unbounded claim: ${term}`);
}

assert(!publicText.includes("SPM-Core"), "SPM-Core must remain outside this public surface");

const publicationRoot = path.join(root, "publications/2026-08-23");
const englishReport = await readFile(path.join(publicationRoot, "technical-report-en.md"), "utf8");
const internationalKit = await readFile(path.join(publicationRoot, "media-kit.md"), "utf8");
const chineseKit = await readFile(path.join(publicationRoot, "media-kit-zh-CN.md"), "utf8");
const citation = await readFile(path.join(root, "CITATION.cff"), "utf8");

for (const [label, text] of [
  ["English report", englishReport],
  ["international media kit", internationalKit],
]) {
  assert(!/[\u3400-\u9fff]/u.test(text), `${label} must remain English-only`);
}

assert(internationalKit.includes("Language: English"), "Zenodo metadata must declare English");
assert(chineseKit.includes("知乎文章"), "Chinese media kit must include Zhihu copy");
assert(chineseKit.includes("中国媒体"), "Chinese media kit language scope is missing");
assert(
  englishReport.includes("not peer reviewed or independently evaluated"),
  "English report must disclose first-party review status",
);
assert(citation.includes('name: "Veridical Tech, Inc."'), "Citation publisher is missing");
assert(citation.includes('url: "https://docs.spmos.ai/technical-report"'), "Citation canonical URL is missing");

const withdrawnNumericPatterns = [
  /99\.7\s*%/i,
  /99\.507\s*%/i,
  /(?:^|\D)8\.4\s*x/i,
  /67\.9\s*(?:-|–|to)\s*69\.2\s*%/i,
  /74\.1\s*%/i,
];
for (const pattern of withdrawnNumericPatterns) {
  assert(!pattern.test(publicText), `Withdrawn historical metric remains public: ${pattern}`);
}

for (const file of requiredFiles.filter((candidate) => candidate.endsWith(".md"))) {
  const markdown = await readFile(path.join(root, file), "utf8");
  const localLinks = [...markdown.matchAll(/\[[^\]]+\]\((?!https?:|mailto:|#)([^)]+)\)/g)].map(
    (match) => match[1],
  );
  for (const link of localLinks) await access(path.resolve(root, path.dirname(file), link));
}

console.log(`PASS ${requiredFiles.length} public information files, canonical identity, claim boundaries, JSON facts, and local links verified`);
