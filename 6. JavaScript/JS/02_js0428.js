const elem1 = document.querySelector('#list-1')

// // 1. firstElementChild
// const firstElem = elem1.firstElementChild
// console.log(firstElem)

// // 2. children
// const children = elem1.children
// console.log(children[0])

// // 3. lastElementChild
// const lastElem = elem1.lastElementChild
// console.log(lastElem)


// // 내가 선택한 노드의 부모노드
// const parent = elem1.parentElement
// console.log(parent)

// // 내가 선택한 노드의 형제노드
// const previous = elem1.previousElementSibling
// console.log(previous)

// const next = elem1.nextElementSibling
// console.log(next)


// // 내용 출력하기
// const myText = elem1.textContent
// console.log(myText)


// // 리스트 순서 변경 (다양한 선택방법)
// const targetElem = elem1.querySelectorAll('li')[4]
// console.log(targetElem);

// const changeElem = elem1.children[1]
// console.log(changeElem);

// changeElem.append(targetElem)
// // append, prepend, before, after 도 있음


// // 새로운 노드 추가하기
// const newNode = document.createElement('li')
// newNode.textContent = '플스5'
// console.log(newNode);

// const lastElem = elem1.lastElementChild
// lastElem.append(newNode)


// // css 조작하기
// elem1.className = 'RedBG WhiteFont'
// elem1.classList.add('WhiteFont')
// elem1.classList.toggle('WhiteFont')


// // 이벤트 다루기
// function myClick(e) {
//   console.log(e.target);
// }

// elem1.onclick = function() {
//   myClick()
// }

// // node.addEventListener(event type, handler)  -- handler에 익명 함수를 넣으면 삭제 불가능
// elem1.addEventListener('click', function() {
//   console.log('새로운 익명 함수');
// })

// elem1.addEventListener('click', myClick)