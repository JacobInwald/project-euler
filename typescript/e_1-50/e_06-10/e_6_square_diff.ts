var n: number = 100

let sum_square: number = [...Array(n+1).keys()].map((x) => x*x).reduce((a, b) => a+b)
let square_sum: number = [...Array(n+1).keys()].reduce((a, b) => a+b)**2

console.log(square_sum - sum_square)
