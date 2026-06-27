const minutesInput = document.querySelector("#minutesInput");
const planButton = document.querySelector("#planButton");
const planResult = document.querySelector("#planResult");

function createStudyPlan(minutes) {
  if (minutes <= 0) {
    return "Enter a positive number of minutes.";
  }

  if (minutes < 20) {
    return "Choose one tiny task and finish that first.";
  }

  if (minutes < 45) {
    return "Work for 25 minutes, then take a short break.";
  }

  return "Split the time into two focused sessions with a break.";
}

function showStudyPlan() {
  const minutes = Number(minutesInput.value);
  planResult.textContent = createStudyPlan(minutes);
}

planButton.addEventListener("click", showStudyPlan);

