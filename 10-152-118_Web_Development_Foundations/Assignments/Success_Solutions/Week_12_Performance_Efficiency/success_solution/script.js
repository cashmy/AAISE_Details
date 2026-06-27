const searchInput = document.querySelector("#searchInput");
const status = document.querySelector("#status");
const resourceList = document.querySelector("#resourceList");

const resources = [
  "Library Research Help",
  "Tutoring Center",
  "Weekly Planning Template",
  "Technology Support Desk",
  "Writing Center Appointment",
  "Study Group Signup"
];

let filterTimer = null;
let filterRunCount = 0;

function renderResources(items) {
  resourceList.textContent = "";

  for (const item of items) {
    const listItem = document.createElement("li");
    listItem.textContent = item;
    resourceList.appendChild(listItem);
  }
}

function filterResources() {
  filterRunCount += 1;
  const searchTerm = searchInput.value.trim().toLowerCase();
  const matches = resources.filter(function (resource) {
    return resource.toLowerCase().includes(searchTerm);
  });

  status.textContent = `Showing ${matches.length} result(s). Filter ran ${filterRunCount} time(s).`;
  renderResources(matches);
}

function handleSearchInput() {
  clearTimeout(filterTimer);
  filterTimer = setTimeout(filterResources, 300);
}

searchInput.addEventListener("input", handleSearchInput);
renderResources(resources);

