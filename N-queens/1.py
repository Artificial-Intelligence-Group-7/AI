from subprocess import call

# import os

# def run(runfile):
#   with open(runfile,"r") as rnf:
#     exec(rnf.read())

if __name__ == "__main__":
    n = (input("Enter A for Astar and B for Hill Climbing"))
    if n== "A":
        call(["python3", "astar.py"])
        # exec('astar.py')
    elif n=="B":
        call(["python3", "nqueens.py"])
        # exec('nqueens.py')
    else:
        print("Invalid argument")
