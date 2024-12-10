console.time('pe16')

// Answer: 1366
// 2^15 is 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
// What is the sum of the digits of the number 2^1000

// const two_fact = (2 ** 1000).toString()
// console.log(two_fact)
// console.log(Math.pow(2,1000))
let bits = 1000
let number = [1]

for(let i = 1; i <= bits; i++) {
    let overflow = 0
    let count = number.length

    for(let j = 0; j < count; j++) {
        let digit = number[j] || 0;
        digit = 2 * digit + overflow;

        if(digit > 9) {
            digit -= 10;
            overflow = 1;
            if (j == count - 1) {
                count += 1;
            }
        } else {
            overflow = 0;
        }
        number[j] = digit;
    }
}

console.log("number array", number)

let sum = number.reduce((count, digit) => count + digit, 0)

console.log(sum);

console.timeEnd('pe16')