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
  "locales/zh-CN.md",
  "locales/ja.md",
  "locales/fr.md",
  "locales/es.md",
  "locales/de.md",
  "locales/ko.md",
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

for (const file of requiredFiles.filter((candidate) => candidate.endsWith(".md"))) {
  const markdown = await readFile(path.join(root, file), "utf8");
  const localLinks = [...markdown.matchAll(/\[[^\]]+\]\((?!https?:|mailto:|#)([^)]+)\)/g)].map(
    (match) => match[1],
  );
  for (const link of localLinks) await access(path.resolve(root, path.dirname(file), link));
}

console.log(`PASS ${requiredFiles.length} public information files, canonical identity, claim boundaries, JSON facts, and local links verified`);
