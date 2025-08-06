let flipped = false;

function handleCardClick() {
  const card = document.getElementById('flip-card');
  const nextButton = document.getElementById('next-button');

  if (!flipped) {
    card.classList.add('flipped');
    flipped = true;
  } else {
    nextButton.click();  // Triggers proper POST with name="next"
  }
}