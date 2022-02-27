var lettersGrid = document.getElementById('letterGrid')
var addLetterBtn = document.getElementById('letterBtn')
var pullBtn = document.getElementById('pullBtn')
var messageGrid = document.getElementById('messageGrid')

function displayPrompt() {
  if(messageGrid.classList.contains('active')){
    messageGrid.classList.remove('active')
  }
  lettersGrid.classList.add('active')
}

addLetterBtn.addEventListener('click', () => displayPrompt())