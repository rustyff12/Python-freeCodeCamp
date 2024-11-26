def arithmetic_arranger(problems, show_answers=False):
    # Length error
    if len(problems) > 5:
        return "Error: Too many problems."
    
    item_count = 0
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""
    longest_string = 0

    for item in problems:
        try:
            divider = ""
            item_count = item_count + 1
            
            # Operator error
            if item.find("/") > -1 or item.find("*") > -1:
                return "Error: Operator must be '+' or '-'."
            
            # Separate list items
            num1, operator, num2 = item.split()
            num1 = num1.strip()
            operator = operator.strip()
            num2 = num2.strip()
            
            # Check num length
            if len(num1) > 4 or len(num2) > 4:
                return 'Error: Numbers cannot be more than four digits.'

            # Answer for case of true
            answer = eval(f"{int(num1)} {operator} {int(num2)}")
            
            # String length for formatting
            longest_string = len(max(num1, num2, key=len))
            
            # add divider
            for _ in range(longest_string + 2):
                divider += "-"
            divider_length = len(divider)
            # Check for item num
            if item_count == len(problems):
                line_1 += add_space(num1, operator, divider_length, 1) + "\n" 
                line_2 += add_space(num2, operator, divider_length, 2) + "\n" 
                if show_answers == True:
                    line_3 += divider + "\n"
                else:
                    line_3 += divider   
                line_4 += add_space(str(answer), "", divider_length, 1)
            else:
                line_1 += add_space(num1, operator, divider_length, 1) + "    " 
                line_2 += add_space(num2, operator, divider_length, 2) + "    "
                line_3 += divider + "    "   
                line_4 += add_space(str(answer), "", divider_length, 1) + "    "
        except:
            return 'Error: Numbers must only contain digits.'
    if show_answers == True:
        # print(repr(line_1 + line_2 + line_3 + line_4))
        return line_1 + line_2 + line_3 + line_4
    else:
        # print(repr(line_1 + line_2 + line_3))
        return line_1 + line_2 + line_3 

# Add correct spacing
def add_space(num, operator, longest_length, pos):
    space = ""
    num_length = len(num) + 1
    if pos == 2:
        for _ in range(longest_length - num_length):
            space += " "
        return operator + space + num
    elif pos == 1:
        for _ in range(longest_length - num_length):
            space += " "
        return " " + space + num
    
    

# print(f"\n{arithmetic_arranger(["3801 - 2", "32 + 698"], True)}")    
# print(f"\n{arithmetic_arranger(["2 - 3801", "32 + 698"], True)}")    
# print(f"\n{arithmetic_arranger(["32 + 698","3801 - 2"])}")    
# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))

# Digit length error
# print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))

# Length error
# print(f"\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}")

# Operator error
# print(f"{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}")
# print(f"{arithmetic_arranger(["3 * 855", "3801 - 2", "45 + 43", "123 + 49"])}")

# type error
# print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))

