a = [5,4,2,2,4,6];
for (let i = 0; i < a.length; i++ ) {
    console.log(a[i], a.length, i)
    if (a[i] === i) {
        break;
    }
}