# Case Converter - List comprehension


# Define a function to convert a PascalCase or camelCase string to snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    # Use a list comprehension to create a list of characters for the snake_case string
    snake_cased_char_list = [
        "_" + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the list of characters into a string and remove leading and trailing underscores
    return "".join(snake_cased_char_list).strip("_")


# Define the main function to run an example
def main():
    # Call the convert_to_snake_case function with an example string
    print(convert_to_snake_case("aLongAndComplexString"))


# Run the main function if the script is executed
if __name__ == "__main__":
    main()
