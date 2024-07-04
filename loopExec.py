import datetime
import sys
import os

n1=os.environ.get('Num1')
n2=os.environ.get('Num2')
def loopExecution():
    n=datetime.datetime.now()
    print("We've executed program at ")
    print(n)

loopExecution()
print(n1+n2)
