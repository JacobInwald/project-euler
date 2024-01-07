let n: number = 1000
let sum: number = 0

for (let i = 1; i < n; i++) {
    if (i % 3 === 0 || i % 5 === 0)
        sum += i
}

console.log(sum)