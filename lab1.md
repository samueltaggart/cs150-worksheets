# Lab 1 worksheet

## Part 1 - Setup and the Command Line
## Part 2 - Create your first Python program

As your first task, you're going to continue a ritual that has been around since the early 1970's -- starting to explore a programming language by first creating a program that prints the words "Hello world!" to the screen. In this course we'll be learning the Python programming language.

In the right hand tab labeled “Console,” type the following and press enter/return afterward.

```python
print("Hello world!")
```

If all went according to plan, it should print "Hello world!" below.

Now, let's make a program that does this.

To start your first program, please click on helloworld.py in the "Files" window on the left side of your screen. Then, type in the following:

```python
# helloworld.py
# This is our first Python program!  It prints hello to the world.

print("Hello, World!")
```

To run the program, click on the "Shell" tab on the right hand side and type
```
python helloworld.py
```

What happened when you ran the program?

## Part 3 - String concatenation

Recall that when we write text between quotation marks `"like this"`, it is a string. We can join two strings together using a `+`. Let's try it out!

In the Console tab, enter `print("one" + "two" + "three")` and press enter. Notice how it joined--or concatenated--the strings into a single string and printed `onetwothree`.

Now, enter `print("one", "two", "three")`. Notice that this one has commas rather than a `+` between each time. Compare the output to the previous print.

What's happening here is that Python's `print()` will print each of the items given to it with spaces between them. Handy!

With your partner, predict what each of the following lines prints out. Then run them and try them. Note carefully which ones have pluses and which ones have commas. Pay careful attention to the spaces in each line and in the output.

```python
print("Computer", "Science", "is", "great", "!")
print("Computer",      "Science",      "is","great","!")
print("Computer", "Science" + "is", "great" + "!")
print("Computer ", "Science " + "is ", "great" + "!")
```

Finally, write a `print()` line that uses `"Computer"`, `"Science"`, `"is"`, `"great"`, and `"!"` with some commas and `+` to print out
```
Computer Science is great!
```

## Part 4 - Modulus

Recall that we can compute the remainder of dividing x by y using the modulus operator: `x % y`. For each of the following, work with your partner to figure out what the result will be. Then use the Python interpreter in the Console tab to compute them and check your work. 

- 25 mod 4
- 12 mod 3
- 5 mod 13
- 0 mod 10

One thing we can do with a modulus is compute the ones digit of a number. For example, the ones digit of 123 is 3. Given any integer x, what number m should you mod x by to get the ones digit? For example, 123 % m should give you 3.

Test that your value of m works by checking that 51 % m gives 1 and 1028 % m gives 8.

We can do a similar thing with time. For example, if working on this worksheet takes 5000 seconds, then we can divide by 60 to figure out how many full minutes it takes and we can mod by 60 to figure out how many additional seconds it takes. In other words, 5000 seconds is `5000 // 60` minutes and `5000 % 60` seconds. Go ahead and compute those expressions using the Console tab.

We can do something similar with hours and minutes. With your partner, work out how to compute the number of hours and minutes there are in 83 minutes.

Assuming this whole lab takes 15000 seconds, how many hours, minutes, and seconds is that?
