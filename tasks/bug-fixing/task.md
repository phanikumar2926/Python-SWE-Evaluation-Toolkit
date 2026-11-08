\# Bug Fix Challenge: Discount Calculator



\## Problem Description



The discount calculator returns incorrect final prices because the discount percentage is not converted into a decimal value.



\## Objective



Fix the `calculate\_discount()` function so that it correctly calculates the final price after applying a discount.



\## Expected Behaviour



Formula:



discount\_amount = price \* (discount\_percent / 100)



final\_price = price - discount\_amount



\## Requirements



1\. Accept the original price.

2\. Accept the discount percentage.

3\. Calculate the discount correctly.

4\. Support zero and full discounts.

5\. Support decimal prices.

6\. Reject negative prices.

7\. Reject discount percentages outside 0 to 100.

8\. Return the final price.



\## Example



Input:



\- price = 100

\- discount\_percent = 10



Expected output: `90`



\## Acceptance Criteria



\- A 10% discount on 100 returns 90.

\- A 25% discount on 100 returns 75.

\- A zero discount returns the original price.

\- A 100% discount returns zero.

\- Decimal prices are calculated correctly.

\- Invalid inputs raise `ValueError`.



\## Testing



Run the automated tests using:



```bash

python -m pytest -v

