# Luhn Algorithm


# Function to verify the validity of a credit card number using the Luhn Algorithm
def verify_card_number(card_number):
    # Initialize sum for odd and even digits separately
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    # Reverse the card number for easier digit extraction
    card_number_reversed = card_number[::-1]

    # Extract and sum the odd digits
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Extract and sum the even digits after doubling them
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        # If doubling results in a number with two digits, add both digits separately
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Calculate the total sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits

    # Check if the total is a multiple of 10 (valid Luhn Algorithm)
    return total % 10 == 0


# Main function to demonstrate the Luhn Algorithm on a sample credit card number
def main():
    # Sample credit card number with spaces and dashes
    card_number = "4211-1111-4555-1141"

    # Remove spaces and dashes from the card number for processing
    card_translation = str.maketrans({"-": "", " ": ""})
    translated_card_number = card_number.translate(card_translation)

    # Verify and print whether the credit card number is valid or not
    if verify_card_number(translated_card_number):
        print("VALID!")
    else:
        print("INVALID!")


# Execute the main function
main()
