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

17. `create_spend_chart` should print a different chart representation. Check that all spacing is exact. Open your browser console with F12 for more details