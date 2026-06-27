const minutesInput = document.querySelector("#minutesInput");
const planButton = document.querySelector("#planButton");
const planResult = document.querySelector("#planResult");
const reminderButton = document.querySelector("#reminderButton");
const reminderStatus = document.querySelector("#reminderStatus");

function getMinutesText() {
  return minutesInput.value.trim();
}

function convertToMinutes(value) {
  return Number(value);
}

function validateMinutes(minutesText, minutes) {
  if (minutesText === "") {
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

function handlePlanButtonClick() {
  const minutesText = getMinutesText();
  const minutes = convertToMinutes(minutesText);
  const validationMessage = validateMinutes(minutesText, minutes);

  if (validationMessage !== "") {
    planResult.textContent = validationMessage;
    return;
  }

  planResult.textContent = createStudyPlan(minutes);
}

function startReminder() {
  reminderStatus.textContent = "Reminder started. Waiting...";

  setTimeout(function () {
    reminderStatus.textContent = "Time to check your next study step.";
  }, 1500);
}

planButton.addEventListener("click", handlePlanButtonClick);
reminderButton.addEventListener("click", startReminder);

