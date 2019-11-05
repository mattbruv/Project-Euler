import time
import sys

code = """
from src import problem{}
problem{}.problem{}()
"""

# Runs a problem number and gives execution time
def run(p):
    start = time.time() 
    print('START PROBLEM', p)
    try:
        exec(code.replace('{}', p))
    except:
        print('!!! EXCEPTION IN PROBLEM', p, '!!!')
    finally:
        return round(time.time() - start, 5)

if __name__ == "__main__":
    try:
        problemNumber = sys.argv[1]
    except:
        print('Invalid problem number given!')

    timer = run(problemNumber)
    print(timer, 'SECONDS ELAPSED')