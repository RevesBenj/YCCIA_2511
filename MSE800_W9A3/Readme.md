# -------------------------------------------------------
# Week 9 - Activity 3: Debugging
# Author: Benjelyn Reves Patiag
# Description:
# Review the code, identify and fix any bugs, and clearly # explain what caused the issues.
# -------------------------------------------------------


##  Example 1 – Loop Problem

### Issue
range(1,20) not include 20.  
Loop stop at 19.  

### Fix
Change to:
range(1,21)

### Output
Print:
You got it!

Only one time (when i = 20)



##  Example 2 – List Index Error

### Issue
List index start at 0.  
randint(1,6) can return 6.  
dice_images[6] → index error.

### Fix
Use:
dice_images[dice_num - 1]

### Output
Print random number:
1 or 2 or 3 or 4 or 5 or 6



##  Example 3 – Year Condition Gap

### Issue
1994 not included.  
Year ≤ 1980 no output.

###  Fix
Make condition clear.  
Add else.

### Output Example
Input 1990 →  
You are a Millennial  

Input 2000 →  
You are Gen Z  



## 🔹 Example 4 – Wrong Operator

###  Issue
Used == not =  
Value not saved.  
Total always 0.

### Fix
Use:
word_per_page = int(input())

### Output Example
10 pages, 250 words  
We have 2500 words in total.



## 🔹 Example 5 – Indentation Error

###  Issue
append() outside loop.  
Only last value added once.

### Fix
Move append() inside loop.

###  Output
Return list same size.  
Numbers random because randint().
