const minutesInput = document.querySelector("#minutesInput");
const planButton = document.querySelector("#planButton");
const planResult = document.querySelector("#planResult");

function getMinutesText() {
  return minutesInput.value.trim();
}

function isBlank(value) {
  return value === "";
}

function convertToMinutes(value) {
  return Number(value);
}

function validateMinutes(minutesText, minutes) {
  if (isBlank(minutesText)) {
    return "Enter your available study time first.";
  }

  if (minutes <= 0) {
    return "Enter a positive number of minutes.";
  }

  return "";
}

function createStudyPlan(minutes) {
  if (minutes < 20) {
    return "Plan: choose one tiny task and finish that first.";
  }

  if (minutes < 45) {
    return "Plan: work for 25 minutes, then take a short break.";
  }

  return "Plan: split the time into two focused sessions with a break.";
}

function updatePlanResult(message) {
  planResult.textContent = message;
}

function handlePlanButtonClick() {
  const minutesText = getMinutesText();
  const minutes = convertToMinutes(minutesText);
  const validationMessage = validateMinutes(minutesText, minutes);

  if (validationMessage !== "") {
    updatePlanResult(validationMessage);
    return;
  }

  updatePlanResult(createStudyPlan(minutes));
}

planButton.addEventListener("click", handlePlanButtonClick);

