const noteInput = document.querySelector("#noteInput");
const previewButton = document.querySelector("#previewButton");
const feedback = document.querySelector("#feedback");

function getNoteText() {
  return noteInput.value.trim();
}

function showFeedback(message) {
  feedback.textContent = message;
}

function previewNote() {
  const note = getNoteText();

  if (note === "") {
    showFeedback("Please enter a note before previewing.");
    return;
  }

  showFeedback(`Preview: ${note}`);
}

previewButton.addEventListener("click", previewNote);

