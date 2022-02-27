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

function displayMessage() {
  messageGrid.classList.add('active')
}

pullBtn.addEventListener('click', () => displayMessage)

addLetterBtn.addEventListener('click', () => displayPrompt())

