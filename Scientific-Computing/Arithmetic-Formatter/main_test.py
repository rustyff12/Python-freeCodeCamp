from main import *

# List of test cases
test_cases = [
    (["3801 - 2", "123 + 49"], "  3801      123\n-    2    +  49\n------    -----"),
    (["1 + 2", "1 - 9380"], "    1         1\n+   2    - 9380\n----    ------"),
]

def test(input_data, expected_output):
    print("---------------------------------")
    print(f"Input: {input_data}")
    print(f"Expected:\n {expected_output}")
    result = arithmetic_arranger(input_data)
    if result == expected_output:
        print("Pass")
        return True
    else:
        print("Fail")
        return False
    
def main():
    passed = 0
    failed = 0
    for input_data, expected_output in test_cases:
        correct = test(input_data, expected_output)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


if __name__ == "__main__":
    main()