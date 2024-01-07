var n: number = 1000
var end: boolean = false
var c: number = 0

for (var a = 1; a < n; a++) {
    for (var b = 1; b < n; b++) {
        c = Math.sqrt(a**2 + b**2)
        if (a + b + c === n) {
            console.log(a*b*c)
            end = true
            break
        }
    }
    if (end)    break
}
