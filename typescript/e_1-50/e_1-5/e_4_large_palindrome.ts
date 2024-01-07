import { utils } from "../../utils"

let max: number = 0

for (let i = 999; i >= 100; i--) {
    for (let j = 999; j >= 100; j--) {
        if (i*j > max && utils.properties.is_palindrome(i*j))
            max = i*j
    }
}

console.log(max)
