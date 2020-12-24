const person = [];
person.push('John'); // this will work ! person variable is not completely reassigned, but mutated
console.log(person[0]) // "John"
person = ["Nick"] 