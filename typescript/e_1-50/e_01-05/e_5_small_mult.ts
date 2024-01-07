let divisors: number[] = [...Array(20).keys()].map((x) => x+1)

for (let i = 20; i < 1000000000; i += 20) {
    if (divisors.map((x) => i % x == 0).reduce((a, b) => a && b)) {
        console.log(i)
        break
    }
}
