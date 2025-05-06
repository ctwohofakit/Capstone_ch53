document.addEventListener('DOMContentLoaded', () => {
  const textarea = document.getElementById('id_user_answer');
  const submitBtn = document.getElementById('submit-answer');

  textarea.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault(); //stop browser default enter behavior
      submitBtn.click(); //instead, do click on button
    }
  });
});

