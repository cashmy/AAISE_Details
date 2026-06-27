const loadResourcesButton = document.querySelector("#loadResourcesButton");
const resourceStatus = document.querySelector("#resourceStatus");
const selectedResource = document.querySelector("#selectedResource");
const resourceList = document.querySelector("#resourceList");

let currentSelection = localStorage.getItem("studySprintSelectedResource") || "";

function renderSelection() {
  if (currentSelection === "") {
    selectedResource.textContent = "No resource selected.";
  } else {
    selectedResource.textContent = `Selected resource: ${currentSelection}`;
  }
}

function saveSelection(resourceName) {
  currentSelection = resourceName;
  localStorage.setItem("studySprintSelectedResource", currentSelection);
  renderSelection();
}

function createResourceCard(resource) {
  const card = document.createElement("article");
  card.className = "resource-card";

  const title = document.createElement("h3");
  title.textContent = resource.name;

  const details = document.createElement("p");
  details.textContent = `${resource.category}: ${resource.bestFor}`;

  const selectButton = document.createElement("button");
  selectButton.textContent = "Select resource";
  selectButton.addEventListener("click", function () {
    saveSelection(resource.name);
  });

  card.append(title, details, selectButton);
  return card;
}

function displayResources(resources) {
  resourceList.textContent = "";

  for (const resource of resources) {
    resourceList.appendChild(createResourceCard(resource));
  }
}

async function loadResources() {
  resourceStatus.textContent = "Loading resources...";

  try {
    const response = await fetch("resources.json");
    const resources = await response.json();
    displayResources(resources);
    resourceStatus.textContent = `Loaded ${resources.length} resources.`;
  } catch (error) {
    resourceStatus.textContent = "Resources could not be loaded.";
  }
}

loadResourcesButton.addEventListener("click", loadResources);
renderSelection();

