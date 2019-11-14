from datetime import datetime
import sys

code = """
from src import problem{}
problem{}.problem{}(args)
"""

# Runs a problem number and returns execution time
def run(p, args):
    start = datetime.now()
    print('START PROBLEM', p)
    try:
        if len(args) == 0:
            args = ''
        exec(code.replace('{}', p).replace('args', str(args)))
    except KeyboardInterrupt:
        print('!!! CANCELLED EXECUTION AFTER', datetime.now() - start)
    return datetime.now() - start

if __name__ == "__main__":
    try:
        problemNumber = sys.argv[1]
        problemArgs = sys.argv[2:]
    except:
        print('Invalid problem number given!')

    timer = run(problemNumber, problemArgs)
    print(timer, 'ELAPSED')