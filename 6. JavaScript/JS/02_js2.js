const minusBtn = document.querySelector('#minusBtn')
const plusBtn = document.querySelector('#plusBtn')
const number = document.querySelector('#number')

minusBtn.addEventListener('click', function() {
  console.log('minus');
  number.textContent --
})

plusBtn.addEventListener('click', function() {
  console.log('plus');
  number.textContent ++
})