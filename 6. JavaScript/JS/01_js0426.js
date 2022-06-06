// let i = 1
// while (i < 11) {
//   console.log(i)
//   i += 1
// }

// for (let i = 1; i < 11; i += 1 ) {
//   console.log(i);
// }


// lodash
const myArr = [1, 2, 3, 4, 5]
console.log(_.sample(myArr))
console.log(_.sampleSize(myArr, 2))

// lodash range
const myRange = _.range(10)
console.log(myRange)

// lodash cloneDeep
const myArr2 = [1, 2, 3, 4, 5, [6, 7, 8]]
const copyArr = _.cloneDeep(myArr2)
console.log(copyArr)

myArr2[5][1] = 9999     // 원본 배열 변경
console.log(myArr2);    // 원본
console.log(copyArr);   // 깊은복사