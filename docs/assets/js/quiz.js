// Basic Quiz Interactivity
document.addEventListener('DOMContentLoaded', () => {
    console.log('Quiz JS loaded');
    
    // Initialize all quiz options with click handlers
    initializeQuizzes();
    
    // Also use a more robust event delegation as fallback
    document.body.addEventListener('click', handleQuizClick);
});

function initializeQuizzes() {
    // Find all quiz options and add direct click listeners
    const allOptions = document.querySelectorAll('.quiz-option');
    allOptions.forEach(option => {
        option.addEventListener('click', function(e) {
            handleOptionClick(this);
        });
    });
}

function handleQuizClick(e) {
    // Fallback event delegation
    const option = e.target.closest('.quiz-option');
    if (option) {
        handleOptionClick(option);
    }
}

function handleOptionClick(option) {
    // Prevent if disabled
    if (option.classList.contains('disabled')) return;

    const container = option.closest('.quiz-item');
    if (!container) return;

    // Allow changing answer: Remove state from siblings
    container.querySelectorAll('.quiz-option').forEach(opt => {
        opt.classList.remove('selected', 'correct', 'incorrect', 'disabled');
    });

    // Add selected class first
    option.classList.add('selected');

    // Check answer
    const isCorrect = option.getAttribute('data-correct') === 'true';
    const feedbackText = option.getAttribute('data-feedback') || '';
    const feedbackEl = container.querySelector('.quiz-feedback');

    // Apply visual state to the option
    option.classList.add(isCorrect ? 'correct' : 'incorrect');

    if (feedbackEl) {
        const prefix = isCorrect ? '<strong>✅ Correto!</strong> ' : '<strong>❌ Incorreto.</strong> ';
        feedbackEl.innerHTML = prefix + feedbackText;
        feedbackEl.className = 'quiz-feedback ' + (isCorrect ? 'correct' : 'incorrect');
        feedbackEl.style.display = 'block';
    }
}
