num = list(map(int, input("Enter the Number For Getting The Table : ").split()))

with open('file.txt', "a") as file:
    for n in num:
        file.write("=" * 25 + "\n")
        file.write(f"      Table of {n}\n")
        file.write("=" * 25 + "\n")

        for i in range(1, 11):
            file.write(f"{n} * {i} = {n*i}\n")

        file.write("\n")