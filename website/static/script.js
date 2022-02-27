var lettersGrid = document.getElementById('letterGrid')
var addLetterBtn = document.getElementById('letterBtn')

function displayPrompt() {
  lettersGrid.classList.add('active')
}

addLetterBtn.addEventListener('click', () => displayPrompt())