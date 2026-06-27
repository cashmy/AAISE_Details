const minutesInput = document.querySelector("#minutesInput");
const planButton = document.querySelector("#planButton");
const planResult = document.querySelector("#planResult");
const loadResourcesButton = document.querySelector("#loadResourcesButton");
const resourceStatus = document.querySelector("#resourceStatus");
const resourceList = document.querySelector("#resourceList");

function chooseStudyPlan(minutes) {
  if (minutes < 20) {
    return "Plan: choose one tiny task and finish that first.";
  }

  if (minutes < 45) {
    return "Plan: work for 25 minutes, then take a short break.";
  }

  return "Plan: split the time into two focused sessions with a break.";
}

function handlePlanButtonClick() {
  const minutesText = minutesInput.value.trim();
  const minutes = Number(minutesText);

  if (minutesText === "" || minutes <= 0) {
    planResult.textContent = "Enter a positive number of minutes.";
    return;
  }

  planResult.textContent = chooseStudyPlan(minutes);
}

function createResourceCard(resource) {
  const card = document.createElement("article");
  card.className = "resource-card";

  const title = document.createElement("h3");
  title.textContent = resource.name;

  const category = document.createElement("p");
  category.textContent = `Category: ${resource.category}`;

  const bestFor = document.createElement("p");
  bestFor.textContent = `Best for: ${resource.bestFor}`;

  card.append(title, category, bestFor);
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

planButton.addEventListener("click", handlePlanButtonClick);
loadResourcesButton.addEventListener("click", loadResources);

