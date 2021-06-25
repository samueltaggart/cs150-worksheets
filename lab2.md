# Lab 2 worksheet

## Part 1 - Countdown!

This exercise is going to give you some practice with debugging, the most sacred of programming activities. Our goal will be to write a program that does the following: 1. Asks the user for a number N of minutes. 2. Prints "X minutes are left! N-X minutes have passed!" for each value of X from N down to 0. For example, with N = 4, the program will print:

4 minutes are left! 

0 minutes have passed!<br/><br/>



3 minutes are left! 

1 minutes have passed!<br/><br/>



2 minutes are left! 

2 minutes have passed!<br/><br/>



1 minutes are left! 

3 minutes have passed!<br/><br/>



0 minutes are left! 

4 minutes have passed!<br/><br/>

Note that there are commands to delay execution of code, which could make this printing happen in real time, but we won't do that here for simplicity's sake.

a. Discuss with your partner how you would use a loop to implement this program. What variables would you use? How would they change as your loop runs?


b. Here's one way you could do it: maintain two variables, `i` and `j` through the loop. `i` will track the number of minutes remaining, and `j` will track the number that have elapsed. You use either one as the loop variable. Based on this description, write down how you would expect `i` and `j` to change for the N=4 case above.


c. In the next three parts, you will fix three unsuccessful attempts to implement this program. Open up countdown1.py in the "files" tab, and run it. The output is incorrect. Which variable seems to be the problem, `i` or `j`? In a few sentences, try to explain why, and suggest a fix to the code.


d. Open up countdown2.py in the "files" tab, and run it. The output is incorrect. Which variable seems to be the problem, `i` or `j`? In a few sentences, try to explain why, and suggest a fix to the code.


e. Open up countdown2.py in the "files" tab, and run it. The output is incorrect. This time, notice that the range() function seems to be counting down. Suggest a way of fixing the code without changing the inputs to `range()`.


## Part 2 - Pattern Practice


In Part 2 of this week's lab, you will be using for loops to print interesting patterns of numbers and "*" signs. This exercise will give you some practice breaking these patterns down.

Here, we'll consider patterns that look like this:

1 2 3

1 2 3

1 2 3<br/><br/>


1 2 3 4

1 2 3 4

1 2 3 4

1 2 3 4<br/><br/>


1 2 3 4 5

1 2 3 4 5

1 2 3 4 5

1 2 3 4 5

1 2 3 4 5<br/><br/>

a. With your partner, briefly describe in words what's going on with these patterns. If there are N rows, what is in each row?

b. Open patternA.py in the "files" tab. The program asks the user for a number `N`. Add code to the for loop which builds up the string `line` until it contains the numbers 1 through N, separated by spaces. Recall that `str(i)` will convert the number `i` into a string. You'll need to do this for `+` to concatenate rather than add.

c. Now add code to what you did in the previous part so that you print the line of numbers `N` times. (You can do this with two nested loops or two loops in sequence. For extra practice, try to figure out how to do it both ways.)


## Part 3 - Square Up

In this exercise, you'll get a little experience drawing pictures in Python.

Open square.py under "files". Note that there is already some code there. `import picture` allows us to use commands from picture.py to draw. (Note that you never need to open picture.py, and in fact probably shouldn't, unless you want to be confused.) We can use functions from picture.py by typing `picture.`, followed by the name of the function we want to call. You can see this done in square.py with the starter code. Notice the comments which describe what each line does.

The pen works in the following way: at all times, it has a position and a direction. The two important commands to know are `picture.drawforward()` and `picture.rotate()`.  Calling `picture.drawforward(x)` will move the pen's position `x` pixels in whatever direction it is facing leaving a line between the start and finish. Calling `picture.rotate(t)` will rotate the pen `t` degrees clockwise (e.g. `picture.rotate(90)` is a right-angle turn).

To show you how the pen works, the starter code has a few lines which will move the pen around, and rotate it. Make sure you understand what the starter code is doing.

Now change the drawing portion of the starter code to draw a square. You should need to use `picture.rotate()` three times, and `picture.drawforward()` four times.
