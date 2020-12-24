let x = 0;
let z = 1;
testLoop: while (z < 10 && x < 10) {
    console.log ('Outer Loops:' + x);
    x += 1;
    z = 1;
    while (z < 10) {
        console.log('Inner Loops:' + z);
        z +=1;
    }
}

// loopnya ga jalan
// requirement:  dipenginin setiap outer loop nambah, inner loop muter dari 0 ke 9 juga. trus knp pake while (true) ?
// pelan2. outer loop print (0) --> outer loop nambah (1) --> inner loop jalan (0 - 9 ) --> outer loop print (1) --> outer loop nambah (2) --> dst
// artinya, biar kondisi outer loop z < 10 AND x < 10 terpenuhi, nilai x harus naik terus. biar nilai x naik terus, inner loop harus jalan terus sampe kondisi terpenuhi.
// Kalo pake while (condition) langsung: inner loop emg memenuhi. Tp begitu nilai z nyampe 10, kondisi outer loop langsung terpenuhi (ingat AND, 1 x 0 = 0). X belum sempet naik ke 2 udh selesai
// Kalo pake while (true) di inner loop dipadukan sama break: inner loop memenuhi sampe z nilenya (10). Tapi kl outer loop ga diapa2in? tetep AND 1 x 0 = 0 nya memenuhi. Makanya, nilai kondisi outer loop yg memenuhi AND = true, DIPINDAH ke break. Outer loop bakal tetep jalan terus dengan while (true), sampe kondisi di break terpenuhi. Break dikasih label biar ketauan mana LOOP yg diterminate pas kelar
