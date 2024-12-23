# Test cases
1. The `deposit` method should create a specific object in the ledger instance variable.

2. Calling the `deposit` method with no description should create a blank description.

3. The `withdraw` method should create a specific object in the `ledger` instance variable.

4. Calling the `withdraw` method with no description should create a blank description.

5. The `withdraw` method should return `True` if the withdrawal took place.

6. Calling `food.deposit(900, 'deposit')` and `food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')` should return a balance of `854.33`.

7. Calling the `transfer` method on a category object should create a specific ledger item in that category object.

8. The `transfer` method should return True if the `transfer` took place.

9. Calling `transfer` on a category object should reduce the balance in the category object.

10. The `transfer` method should increase the balance of the category object passed as its argument.

11. The `transfer` method should create a specific ledger item in the category object passed as its argument.

12. The check_funds method should return False if the amount passed to the method is greater than the category balance.

13. The `check_funds` method should return `True` if the amount passed to the method is not greater than the category balance.

14. The `withdraw` method should return `False` if the withdrawal didn't take place.

15. The `transfer` method should return `False` if the transfer didn't take place.

16. Printing a `Category` instance should give a different string representation of the object.

----

17. Title at the top of `create_spend_chart` chart should say `Percentage spent by category`.

18. `create_spend_chart` chart should have correct percentages down the left side.

19. The height of each bar on the `create_spend_chart` chart should be rounded down to the nearest 10.

20. Each line in `create_spend_chart` chart should have the same length. Bars for different categories should be separated by two spaces, with additional two spaces after the final bar.

21. `create_spend_chart` should correctly show horizontal line below the bars. Using three `-` characters for each category, and in total going two characters past the final bar.

22. `create_spend_chart` chart should not have new line character at the end.

23. `create_spend_chart` chart should have each category name written vertically below the bar. Each line should have the same length, each category should be separated by two spaces, with additional two spaces after the final category.

24. `create_spend_chart` should print a different chart representation. Check that all spacing is exact. Open your browser console with F12 for more details.