# Case Converter


# Define a function to convert a PascalCase or camelCase string to snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    # Initialize an empty list to store characters of the snake_case string
    snake_cased_char_list = []

    # Iterate through each character in the input string
    for char in pascal_or_camel_cased_string:
        # Check if the character is an uppercase letter
        if char.isupper():
            # If uppercase, add an underscore and the lowercase version of the character
            converted_character = "_" + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            # If not uppercase, add the character as is
            snake_cased_char_list.append(char)

    # Join the list of characters into a string
    snake_cased_string = "".join(snake_cased_char_list)

    # Remove leading and trailing underscores (clean up the snake_case string)
    clean_snake_cased_string = snake_cased_string.strip("_")

    # Return the final snake_case string
    return clean_snake_cased_string


# Define the main function to run an example
def main():
    # Call the convert_to_snake_case function with an example string
    print(convert_to_snake_case("aLongAndComplexString"))


# Run the main function if the script is executed
if __name__ == "__main__":
    main()
