// ga akan berubah, karena https://stackoverflow.com/questions/48514532/using-for-of-loop-to-change-an-array

//The problem here is that the the identifier i is being overwritten.With another integer and val is just a temp variable invoked each iteration of the loop. If you used an object, and did not reassign the variable, your values would remain intact

//yg direassign cuma temp variable yg jadi placeholdernya doang 

let pets = ['cat', 'dog', 'rat'];
for (let i of pets) {
    //no object reassignment, only reassigning the identifier i. The value in pets stay intact
    i = i + 's';
}
console.log(pets) //the value in pets stay intact