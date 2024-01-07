export namespace utils {
    
    // ! PRIME METHODS
    export module primes {

        /**
         * Generates a list of prime numbers up to a given number using the Sieve of Eratosthenes algorithm.
         * 
         * @param n The upper limit of the range to search for prime numbers.
         * @returns A list of prime numbers up to the given number.
         */
        export function prime_sieve(n: number): number[] {
            var numbers: boolean[] = [...Array(n-1).keys()].map((x) => false)
            var primes: number[] = []

            for (var i = 2; i <= n; i++) {

                if (numbers[i-2])
                    continue
                else
                    primes.push(i)

                for(let x = i; x <= n; x+=i)
                    numbers[x-2] = true
            }

            return primes
        }

        /**
         * Factorizes a number into its prime factors.
         * 
         * @param n The number to factorize.
         * @param primes An optional list of prime numbers. If not provided, it will be generated using the prime_sieve function.
         * @returns An array of prime factors of the given number.
         */
        export function prime_factorize(n: number): number[] {
            var factors: number[] = []

            while (n % 2 == 0) {
                n = n / 2
                factors.push(2)
            }

            while (n % 3 == 0) {
                n = n / 3
                factors.push(3)
            }

            for (var i = 5; i <= n; i+=6){

                if (is_prime(i)) {
                    while (n % i == 0) {
                        n = n / i
                        factors.push(i)
                    }
                }

                if (is_prime(i+2)) {
                    while (n % (i+2) == 0) {
                        n = n / (i+2)
                        factors.push(i+2)
                    }
                }
            }

            return factors
        }

        export function is_prime(n: number): boolean {
            if (n % 2 == 0 || n % 3 == 0)
                return false
            for (let x = 5; x < Math.sqrt(n); x+=6) {
                if (n % (x) == 0 || n % (x+2) == 0 ) {
                    return false
                }
            }
            return true
        }
    }

    // ! NUMBER PROPERTIES
    export module properties {

        /**
         * Checks if a number is a palindrome.
         * @param n - The number to check.
         * @returns True if the number is a palindrome, false otherwise.
         */
        export function is_palindrome(n: number): boolean {

            var str_n: string = n.toString()
            
            for (let i = 0; i < str_n.length / 2; i++)
                if (str_n[i] !== str_n[str_n.length-1-i])
                    return false

            return true
        }

        /**
         * Generates the nth triangular number.
         * 
         * @param n - The index of the triangular number to generate.
         * @returns The nth triangular number.
         */
        export function gen_tri_num(n: number): number {
            return ((n * (n+1)) / 2) >> 0
        }

        export function is_tri_num(n: number): boolean {
            return ((Math.sqrt(8*n+1) - 1) / 2) % 1 == 0
        }
    }
}
// import os
// import math as m

// def divisible(n: int, primes: list[int]) -> bool:
//     """
//     Check if a number is divisible by any of the given primes.

//     Args:
//         n (int): The number to check for divisibility.
//         primes (list[int]): The list of prime numbers to check against.

//     Returns:
//         bool: True if the number is not divisible by any of the primes, False otherwise.
//     """
//     for i in primes:
//         if (n // i) * i == n:
//             return False
//     return True

// # ! Number Property Methods

// def isPan(n: int, upto: int=9) -> bool:
//     """
//     Check if a number is a pandigital number.

//     Args:
//         n (int): The number to check.
//         upto (int, optional): The maximum digit to consider. Defaults to 9.

//     Returns:
//         bool: True if the number is pandigital, False otherwise.
//     """
//     n = str(n)
//     if len(n) != upto:
//         return False
//     for i in range(1, upto+1):
//         if str(i) not in n:
//             return False
//     return True

// def gen_tri(n: int) -> int:
//     """
//     Generate the nth triangular number.
    
//     Parameters:
//     n (int): The index of the triangular number to generate.
    
//     Returns:
//     int: The nth triangular number.
//     """
//     return n*(n+1)//2

// def is_tri(n: int) -> bool:
//     """
//     Check if a number is a triangular number.
    
//     A triangular number is a number that can be represented in the form of a triangle with dots.
//     It is the sum of the natural numbers up to a certain number.
    
//     Args:
//         n (int): The number to check.
        
//     Returns:
//         bool: True if the number is a triangular number, False otherwise.
//     """
//     return ((m.sqrt(8*n+1) - 1) / 2) % 1 == 0

// def gen_pent(n: int) -> int:
//     """
//     Generate the nth pentagonal number.
    
//     Args:
//         n (int): The index of the pentagonal number to generate.
        
//     Returns:
//         int: The nth pentagonal number.
//     """
//     return n*(3*n-1)//2

// def is_pent(n: int) -> bool:
//     """
//     Check if a number is a pentagonal number.
    
//     Args:
//         n (int): The number to be checked.
        
//     Returns:
//         bool: True if the number is a pentagonal number, False otherwise.
//     """
//     return ((m.sqrt(24*n+1) + 1) / 6) % 1 == 0

// def gen_hex(n: int) -> int:
//     """
//     Generate the nth hexagonal number.
    
//     Parameters:
//     n (int): The index of the hexagonal number to generate.
    
//     Returns:
//     int: The nth hexagonal number.
//     """
//     return n*(2*n-1)

// def is_hex(n: int) -> bool:
//     """
//     Check if a number is a hexagonal number.
    
//     Args:
//         n (int): The number to be checked.
        
//     Returns:
//         bool: True if the number is a hexagonal number, False otherwise.
//     """
//     return ((m.sqrt(8*n+1) + 1) / 4) % 1 == 0

// # ! Prime Related Methods

// def is_prime(n: int, primes: list[int]=None) -> bool:
//     """
//     Check if a number is prime.

//     Args:
//         n (int): The number to check.
//         primes (list[int], optional): A list of prime numbers. If not provided, it will be generated using the sieve of Eratosthenes algorithm.

//     Returns:
//         bool: True if the number is prime, False otherwise.
//     """
//     if not primes:
//         primes = sieve_of_eratosthenese(n)
//     return n in primes

// def is_circle_prime(n: int, primes: list[int]=None) -> bool:
//     """
//     Checks if a number is a circular prime.
    
//     Args:
//         n (int): The number to check.
//         primes (list[int], optional): List of prime numbers. Defaults to None.
    
//     Returns:
//         bool: True if the number is a circular prime, False otherwise.
//     """

//     if n < 10:
//         return True

//     for i in range(len(str(n))):
//         if n not in primes:
//             return False
//         n =  int(str(n)[-1] + str(n)[0:-1])

//     return True

// def is_truncate_prime(n: int, primes: list[int]=None) -> bool:
//     """
//     Checks if a number is a truncate prime.

//     Args:
//         n (int): The number to be checked.
//         primes (list[int], optional): List of prime numbers. Defaults to None.

//     Returns:
//         bool: True if the number is a truncate prime, False otherwise.
//     """

//     str_n = str(n)
//     if len(str_n) <= 1 or n not in primes:
//         return False
//     for i in range(1, len(str_n)):
//         if int(str_n[0:i]) not in primes:
//             return False
//         if int(str_n[i:]) not in primes:
//             return False
//     return True
    
// def gen_mill_primes():
//     """
//     Generates and saves a list of prime numbers up to 1,000,000.

//     This function uses the sieve of Eratosthenes algorithm to generate a list of prime numbers
//     up to 1,000,000. The generated list is then saved to a file named 'million_primes.txt'.

//     """
//     mill_primes = sieve_of_eratosthenese(1000000)

//     with open(os.path.join(os.path.dirname(__file__), 'data/million_primes.txt'), 'w') as f:
//         nums = ''
//         for n in mill_primes:
//             nums += str(n) + ','
//         f.writelines(nums)

// def read_mill_primes() -> list[int]:
//     """
//     Reads a list of prime numbers from a file and returns them as a list of integers.
    
//     Returns:
//         list[int]: A list of prime numbers.
//     """
//     with open(os.path.join(os.path.dirname(__file__), 'data/million_primes.txt'), 'r') as f:
//         nums = f.readline().split(',')
//         return [int(n) for n in nums if n != '']
