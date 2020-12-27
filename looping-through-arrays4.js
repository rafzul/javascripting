//syntaxt arrow function
let pets = ['cat', 'dog', 'rat'];
pets.forEach((element, index, array) => array[index] = array[index] + 's');
console.log(pets);

//syntax function normal
// let pets = ['cat', 'dog', 'rat'];
// pets.forEach(function (element, index, array) {
//     array[index] = array[index] + 's';
// });
// console.log(pets);