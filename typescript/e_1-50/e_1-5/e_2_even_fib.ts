/**
 * Generates Fibonacci sequence up to a given number.
 * @param n - The number up to which the Fibonacci sequence should be generated.
 * @returns An array containing the Fibonacci sequence up to the given number.
 */
function fib_upto(n: number): number[]{
    let fin: number[] = []
    fin.push(1)
    fin.push(1)
    for (let i = 2; i < n; i++)
        fin.push(fin[i-1] + fin[i-2])
    return fin
}

let fibs: number[] = fib_upto(100)
let s: number = 0
for (let i = 0; i < fibs.length; i ++) {
    if (fibs[i] % 2 === 0 && fibs[i] < 4000000)
        s += fibs[i]
}
console.log(s)
