// const a = 4 //a is a global variable, it can be accessed by the functions below

// function foo() {
//     const b = a * 3; //b cannot be accessed outside foo function, but can be accessed by functions defined inside foo function
//     function bar (c) {
//         const b = 2 //another 'b' variable is created inside bar function scope. The change to this new b variable don't affect the old b variable
//         console.log(a,b,c);
//     }

//     bar(b*4);
// }

// foo() //4,2,48

//-----------------------------------------------

//IIFE:
// (function () { //the function expressiion is  surrounded by parenthesis. Variable defined here cant be accessed outside

// })() //the function is immidiately invoked

//----------------------------------------------------

//CHALLENGE
const a =1, b = 2, c =3;

(function firstFunction() {
    const b = 5, c =6;
    (function secondFunction () {
        const b=8;
        console.log(`a: ${a}, b: ${b}, c: ${c}`);
        (function thirdFunction () {
            const a =7; const c = 9;
            (function fourthFunction () {
                const a = 1; const c =8;
            })()
        })()
    })()
})()
