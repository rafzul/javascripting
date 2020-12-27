let i = 0,
    n = 0;
while (i < 5) {
    console.log(i)
    i++;
    if (i === 3) {
        continue;
    }
    n += i;
    console.log('loop pake continue', i, n);
}
console.log('selese loop pake continue')
//1,3,7,12

let x = 0,
    y = 0;
while (x < 5) {
    console.log(x)
    x++;
    if (x == 3) {
        //continue;
    }
    y += x;
    console.log('loop gapake continue', x, y);
}
console.log ('selese loop gapake continue')
// 1,3,6,10,15