const minutesInput = document.querySelector("#minutesInput");
const planButton = document.querySelector("#planButton");
const planResult = document.querySelector("#planResult");

function createStudyPlan(minutes) {
  if (minutes < 20) {
    return "Plan: choose one tiny task and finish that first.";
  }

  if (minutes < 45) {
    return "Plan: work for 25 minutes, then take a short break.";
  }

  return "Plan: split the time into two focused sessions with a break.";
}

function showStudyPlan() {
  if (minutesInput.value.trim() === "") {
    planResult.textContent = "Enter your available study time first.";
    return;
  }

  const minutes = Number(minutesInput.value);

  if (minutes <= 0) {
    planResult.textContent = "Enter a positive number of minutes.";
    return;
  }

  planResult.textContent = createStudyPlan(minutes);
}

planButton.addEventListener("click", showStudyPlan);

