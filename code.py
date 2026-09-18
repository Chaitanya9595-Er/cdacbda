print("heloo my name is cd")
```bash
#!/bin/bash

# ==========================================
# 1. VARIABLES
# ==========================================

a=10
b=5

echo "a = $a"
echo "b = $b"


# ==========================================
# 2. TAKING INPUT
# ==========================================

read -p "Enter first number: " x
read -p "Enter second number: " y


# ==========================================
# 3. BASIC ARITHMETIC OPERATIONS
# ==========================================

sum=$((x+y))
diff=$((x-y))
prod=$((x*y))
div=$((x/y))
rem=$((x%y))

echo "Sum = $sum"
echo "Difference = $diff"
echo "Product = $prod"
echo "Division = $div"
echo "Remainder = $rem"


# ==========================================
# 4. IF / ELSE
# ==========================================

if [ $x -gt $y ]
then
    echo "$x is greater than $y"
else
    echo "$x is not greater than $y"
fi


# ==========================================
# 5. IF / ELIF / ELSE
# ==========================================

if [ $x -gt 0 ]
then
    echo "$x is positive"
elif [ $x -lt 0 ]
then
    echo "$x is negative"
else
    echo "$x is zero"
fi


# ==========================================
# 6. EVEN / ODD
# ==========================================

if [ $((x%2)) -eq 0 ]
then
    echo "$x is even"
else
    echo "$x is odd"
fi


# ==========================================
# 7. STRING COMPARISON
# ==========================================

read -p "Enter your name: " name

if [ "$name" = "admin" ]
then
    echo "Welcome Admin"
else
    echo "Welcome $name"
fi


# ==========================================
# 8. EMPTY STRING CHECK
# ==========================================

if [ -z "$name" ]
then
    echo "Name is empty"
else
    echo "Name is not empty"
fi


# ==========================================
# 9. FILE CHECK
# ==========================================

read -p "Enter filename: " file

if [ -f "$file" ]
then
    echo "$file is a regular file"
elif [ -d "$file" ]
then
    echo "$file is a directory"
else
    echo "$file does not exist"
fi


# ==========================================
# 10. FOR LOOP
# ==========================================

echo "Numbers from 1 to 10:"

for (( i=1; i<=10; i++ ))
do
    echo $i
done


# ==========================================
# 11. SUM USING LOOP
# ==========================================

read -p "Enter N for sum: " n

sum=0

for (( i=1; i<=n; i++ ))
do
    sum=$((sum+i))
done

echo "Sum from 1 to $n = $sum"


# ==========================================
# 12. PRODUCT / FACTORIAL USING LOOP
# ==========================================

read -p "Enter N for factorial: " n

fact=1

for (( i=1; i<=n; i++ ))
do
    fact=$((fact*i))
done

echo "Factorial = $fact"


# ==========================================
# 13. EVEN NUMBERS USING LOOP
# ==========================================

echo "Even numbers from 1 to 20:"

for (( i=1; i<=20; i++ ))
do
    if [ $((i%2)) -eq 0 ]
    then
        echo $i
    fi
done


# ==========================================
# 14. WHILE LOOP
# ==========================================

i=1

echo "While loop:"

while [ $i -le 5 ]
do
    echo $i
    i=$((i+1))
done


# ==========================================
# 15. UNTIL LOOP
# ==========================================

i=1

echo "Until loop:"

until [ $i -gt 5 ]
do
    echo $i
    i=$((i+1))
done


# ==========================================
# 16. COMMAND LINE ARGUMENTS
# ==========================================

echo "Script name = $0"
echo "First argument = $1"
echo "Second argument = $2"
echo "Number of arguments = $#"


# ==========================================
# 17. SCALE / DECIMAL CALCULATION
# ==========================================

# Shell normally performs integer division.
# bc can be used for decimal calculations.

echo "Decimal division:"

result=$(echo "scale=2; 10/3" | bc)

echo "10 / 3 = $result"


# ==========================================
# 18. CURRENT USER
# ==========================================

echo "Current user = $USER"


# ==========================================
# 19. CURRENT DIRECTORY
# ==========================================

echo "Current directory = $PWD"


# ==========================================
# 20. DATE
# ==========================================

echo "Current date:"
date


# ==========================================
# END
# ==========================================

echo "Script completed."
```
