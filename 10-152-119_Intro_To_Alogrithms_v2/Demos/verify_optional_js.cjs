"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const {test} = require("node:test");

function load(relativePath) {
  const nodes = {
    minimum: {value: "50"}, laptops: {checked: false},
    result: {textContent: ""}, controls: {}, run: {}
  };
  for (const node of Object.values(nodes)) {
    node.events = {};
    node.addEventListener = (name, callback) => { node.events[name] = callback; };
  }
  const context = vm.createContext({document: {getElementById: id => nodes[id]}});
  vm.runInContext(fs.readFileSync(path.join(__dirname, relativePath), "utf8"), context);
  return {nodes, context};
}
const filterPath = "Week_01/Demo_03_Combined_Criteria/optional_js/main.js";
const sortPath = "Week_04/Demo_02_Stable_Record_Sorting/optional_js/main.js";
for (const scriptPath of [filterPath, sortPath]) {
  test(`${path.dirname(scriptPath)}: three separate layers`, () => {
    const folder = path.join(__dirname, path.dirname(scriptPath));
    const html = fs.readFileSync(path.join(folder, "index.html"), "utf8");
    assert.match(html, /<link\s+rel="stylesheet"\s+href="styles\.css"\s*\/?>/);
    assert.match(html, /<script\s+src="main\.js"><\/script>/);
    assert.doesNotMatch(html, /<style\b|\sstyle\s*=/i);
    assert.ok(fs.readFileSync(path.join(folder, "styles.css"), "utf8").trim());
    assert.ok(fs.existsSync(path.join(folder, "main.js")));
  });
}
test("filter: default and empty criteria", () => {
  const {nodes} = load(filterPath);
  const result = JSON.parse(nodes.result.textContent);
  assert.deepEqual(result.selected, ["E01", "E02", "E04"]);
  assert.deepEqual(result.emptyCriteria, ["E01", "E02", "E03", "E04"]);
});
test("filter: checkbox and submit event", () => {
  const {nodes} = load(filterPath);
  nodes.laptops.checked = true;
  let prevented = false;
  nodes.controls.events.submit({preventDefault: () => {prevented = true;}});
  assert.equal(prevented, true);
  assert.deepEqual(JSON.parse(nodes.result.textContent).selected, ["E01", "E04"]);
});
test("filter: changed threshold", () => {
  const {nodes, context} = load(filterPath);
  nodes.minimum.value = "80";
  vm.runInContext("run()", context);
  assert.deepEqual(JSON.parse(nodes.result.textContent).selected, ["E01"]);
});
test("filter: invalid threshold", () => {
  const {nodes, context} = load(filterPath);
  nodes.minimum.value = "101";
  vm.runInContext("run()", context);
  assert.match(nodes.result.textContent, /must be an integer/);
});
test("sorting: stable ties, copy, counts and mutation contract", () => {
  const {nodes} = load(sortPath);
  const result = JSON.parse(nodes.result.textContent);
  assert.deepEqual(result.original, ["A", "B", "C", "D"]);
  assert.deepEqual(result.insertion, ["D", "B", "A", "C"]);
  assert.deepEqual(result.libraryCopy, result.insertion);
  assert.equal(result.comparisons, 5);
  assert.equal(result.shifts, 4);
  assert.equal(result.sortReturnsSameArray, true);
});
test("sorting: button rerun and empty input", () => {
  const {nodes, context} = load(sortPath);
  const before = nodes.result.textContent;
  nodes.run.events.click();
  assert.equal(nodes.result.textContent, before);
  assert.equal(vm.runInContext("insertionSort([], row => row.battery).ordered.length", context), 0);
});
