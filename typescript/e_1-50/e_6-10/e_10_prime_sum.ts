import { utils } from "../utils"

console.log(utils.primes.prime_sieve(2000000).reduce((a, b) => a+b))