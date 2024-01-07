import { utils } from "../../utils"

let factors: number[] = utils.primes.prime_factorize(600851475143)
let max: number = 0

for (let i = 0; i < factors.length; i++) {
    if (max < factors[i])   max = factors[i]
}

console.log(max)