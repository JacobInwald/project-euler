import { utils } from '../../utils';

/**
 * Returns an array of divisors for a given number.
 * 
 * @param n - The number to find divisors for.
 * @returns An array of divisors for the given number.
 */
function get_divisors(n: number): number[] {
    var factors: number[] = []
    var div: number = 0
    
    for (var i = 1; i < Math.sqrt(n); i++) {
        div = (n / i) >> 0
        if (div * i === n) {
            factors.push(div)
            factors.push(i)
        }
    }
    return factors
}

var num = 0

for (var i = 1; i < 1000000; i++) {
    num = utils.properties.gen_tri_num(i)
    if (get_divisors(num).length > 500) {
        console.log(num)
        break
    }
}