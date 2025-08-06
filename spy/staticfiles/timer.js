document.addEventListener('DOMContentLoaded', () => {
  const startBtn = document.getElementById('start-btn');
  const timerDisplay = document.getElementById('timer');
  const endGameForm = document.getElementById('end-game-form');

  const duration = parseInt(timerDisplay.dataset.minutes);
  let minutes = duration;
  let seconds = 0;

  startBtn.addEventListener('click', () => {
    // Hide the Start Timer button with animation
    startBtn.style.opacity = '0';
    startBtn.style.pointerEvents = 'none';

    // Delay then show End Game button in the same spot
    setTimeout(() => {
      endGameForm.classList.add('show');
    }, 300); // match CSS transition timing

    // Start countdown
    const interval = setInterval(() => {
      if (seconds === 0) {
        if (minutes === 0) {
          clearInterval(interval);
          alert("Time's up!");
          // Optional: auto-submit the form
          // endGameForm.submit();
          return;
        }
        minutes--;
        seconds = 59;
      } else {
        seconds--;
      }

      timerDisplay.textContent =
        `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }, 1000);
  });
});