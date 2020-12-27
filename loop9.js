function dump_props(obj, obj_name) {
    let result = '';
    for (let i in obj) {
        result += obj_name + '.' + i + '=' + obj[i] +'<br>';
    }
    result += '<hr>';
    return result;
}

let carprops = {
    make: 'Ford',
    model: 'mustang',
    year: 1969
};

console.log(dump_props(carprops, 'car'));


//jangan dipake di ARRAY