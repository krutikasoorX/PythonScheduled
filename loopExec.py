import datetime
import sys

def loopExecution():
    n=datetime.datetime.now()
    print("We've executed program at ")
    print(n)

loopExecution()
print(sys.argv[1]+sys.argv[2])

