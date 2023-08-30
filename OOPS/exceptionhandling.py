import sys
import traceback

try:
    a = 100
    b = 'a'
    print(a/b)

except (ZeroDivisionError, TypeError) as msg:
    print(msg)
    # raise " you are dividing by 0"
    print(traceback.format_exc())   #--> prints complete exception detail

else: #else block executes only when no exceptions are found in try block
    print("got no exceptions")

finally:
    print("finally!")

# example 2