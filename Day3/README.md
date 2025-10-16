#  Day 3: Diving into Booleans & Operators in Python

Welcome back to our Python journey! Today’s focus is on two foundational concepts that power decision-making and logic in your code: Booleans and Operators.
Booleans help your programs make choices—like answering yes/no questions or checking if something is true. Operators, on the other hand, are the tools that let you assing values, compare things, and perfom calculations. When you're debugging a loop or mapping logic to a spreadsheet, understanding these elements will make your chode smarter and more expressive. Now let's explore how they work and how we can use them. 

--- 
# Boolean Data Types 
A Boolean is a data type that represents one of two values: True or False. These are used to express logical conditions like something is correct, matches a rule , or passes a test. 

 ```print(True)  ```
 
  ```print(False) ```
  
  Booleans often appear in comparisons and conditionals:
  
   ```print(5 > 3)     # True ```
   
 ```print("cat" == "dog")  # False ```

 ---
 # Operators in Python 
Assignment operators are used to assign vaules to variables. In python the sign = is used to store a vaule inside a variable- this process is called assignment.For example:

 ``score = 100  # assigns the value 100 to the variable score  ``
This tells python: " Hey, remember that score means 100 from now on."
Assigment operators are just one category of Python operators. The table below shows the differen types of Python operators, adapted from W3Schools, and how they're used to perfrom actions like comparisons,logic and more.

 <img width="1125" height="698" alt="image" src="https://github.com/user-attachments/assets/933756c7-b54d-426d-8084-773450675c99" />
Arithmetic operators as we see use basic mathematical operations in python. These are the essential for calcations, data analysis, and logic building in your programs.Here’s a breakdown of each operator:
- Addition(+): a + b
  
- Subtraction(-): a - b
  
- Multiplication(*): a * b
  
- Division(/): a / b
  
- Modulus(%): a % b
  
- Floor division(//): a // b
  
- Exponentiation(**): a ** b

And now let's do some example's of Arithemetic Operations in Python :

```print('Addition:', 1 + 2)               # 3```

```print('Subtraction:', 2 - 1)            # 1```

```print('Multiplication:', 2 * 3)         # 6```

```print('Division:', 4 / 2)               # 2.0 (returns float)```

```print('Floor Division:', 7 // 2)        # 3 (no decimal)```

```print('Floor Division:', 7 // 3)        # 2```

```print('Modulus:', 3 % 2)                # 1 (remainder)```

```print('Exponentiation:', 2 ** 3)        # 8 (2 * 2 * 2) ```


 
 
 ---
 # Exercises- Day 3

---

1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10)
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use *and* operator to check if 'on' is found in both 'python' and 'dragon'
14. *I hope this course is not full of jargon*. Use *in* operator to check if *jargon* is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text *python* and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
23.  Write a Python script that displays the following table
