# Luhn algorithm
The Luhn algorithm is as follows:

Starting from the rightmost digit (the check digit) and moving left, double the value of every second digit.
If doubling a digit results in a number greater than 9, subtract 9 from the product.
Sum all the digits together, including both the original and modified digits.
If the total is a multiple of 10, the number is valid according to the Luhn algorithm.
Assume an example of an account number "7992739871" that will have a check digit added, making it of the form 7992739871x:

Account number      7   9  9  2  7  3  9   8  7  1  x
Double every other  7  18  9  4  7  6  9  16  7  2  x
Sum 2-char digits   7   9  9  4  7  6  9   7  7  2  x
