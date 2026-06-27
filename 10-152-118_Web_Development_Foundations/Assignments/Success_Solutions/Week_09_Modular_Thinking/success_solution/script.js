const minutesInput = document.querySelector("#minutesInput");
const planButton = document.querySelector("#planButton");
const planResult = document.querySelector("#planResult");
const reminderButton = document.querySelector("#reminderButton");
const reminderStatus = document.querySelector("#reminderStatus");

function readMinutesText() {
  return minutesInput.value.trim();
}

function convertToMinutes(minutesText) {
  return Number(minutesText);
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

function chooseStudyPlan(minutes) {
  if (minutes < 20) {
    return "Plan: choose one tiny task and finish that first.";
  }

  if (minutes < 45) {
    return "Plan: work for 25 minutes, then take a short break.";
  }

  return "Plan: split the time into two focused sessions with a break.";
}

function showPlanMessage(message) {
  planResult.textContent = message;
}

function showReminderMessage(message) {
  reminderStatus.textContent = message;
}

function handlePlanButtonClick() {
  const minutesText = readMinutesText();
  const minutes = convertToMinutes(minutesText);
  const validationMessage = validateMinutes(minutesText, minutes);

  if (validationMessage !== "") {
    showPlanMessage(validationMessage);
    return;
  }

  showPlanMessage(chooseStudyPlan(minutes));
}

function startDelayedReminder() {
  showReminderMessage("Reminder started. Waiting...");

  setTimeout(function () {
    showReminderMessage("Time to check your next study step.");
  }, 1500);
}

function connectEvents() {
  planButton.addEventListener("click", handlePlanButtonClick);
  reminderButton.addEventListener("click", startDelayedReminder);
}

connectEvents();

