const minutesAvailable = 45;
const tasksRemaining = 3;
const assignmentDueToday = false;

function chooseFocusLevel(minutes, taskCount) {
  if (minutes < 20) {
    return "quick focus";
  }

  if (minutes >= 45 && taskCount >= 3) {
    return "deep focus";
  }

  return "steady focus";
}

function createStudyRecommendation(minutes, taskCount, dueToday) {
  const focusLevel = chooseFocusLevel(minutes, taskCount);

  if (dueToday && taskCount > 0) {
    return `Use ${focusLevel}: complete the highest-priority task first.`;
  }

  if (taskCount === 0) {
    return "No tasks are listed. Use the time to review or organize notes.";
  }

  return `Use ${focusLevel}: choose one task and work for ${minutes} minutes.`;
}

const recommendation = createStudyRecommendation(
  minutesAvailable,
  tasksRemaining,
  assignmentDueToday
);

console.log("Minutes available:", minutesAvailable);
console.log("Tasks remaining:", tasksRemaining);
console.log("Assignment due today:", assignmentDueToday);
console.log("Recommendation:", recommendation);

