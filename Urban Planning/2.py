from subprocess import call


if __name__ == "__main__":
    n = (input("Enter A for Genetic Algorithm and B for Hill Climbing"))
    if n== "A":
        call(["python3", "gentic_alogorithm.py"])

    elif n=="B":
        call(["python3", "Hill_climbing.py"])

    else:
        print("Invalid argument")
