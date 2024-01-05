import math

def c(a: int, b: int) -> int: 
        """
        Calculates the length of the hypotenuse of a right triangle using the Pythagorean theorem.
        
        Args:
                a (int): The length of one side of the triangle.
                b (int): The length of the other side of the triangle.
        
        Returns:
                int: The length of the hypotenuse.
        """
        return math.sqrt((a**2)+(b**2))

def isTriplet(a: int, b: int, c: int) -> bool:
        """
        Check if three numbers form a Pythagorean triplet.

        Args:
                a (int): The first number.
                b (int): The second number.
                c (int): The third number.

        Returns:
                bool: True if the numbers form a Pythagorean triplet, False otherwise.
        """
        return a**2 + b**2 == int(c)**2


for a in range(0,1000):
    for b in range(a,1000):
        c1 = c(a, b)
        if(isTriplet(a,b,c1) and a+b+c1 == 1000):
             print(a,b,c1)
