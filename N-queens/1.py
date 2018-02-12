from subprocess import call
if __name__ == "__main__":
    n = int(input("Enter 1 for Astar and 2 for Hill Climbing:"))
    if n== 1:
        call(["python3", "astar.py"])
    elif n==2:
        call(["python3", "nqueens.py"])
    else:
        print("Invalid argument")
