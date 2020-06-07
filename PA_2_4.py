def diagonal_stars(number):
    for i in range(number):
        for j in range(i):
            print(".", end="")
        print("*")


number = int(input())
diagonal_stars(number)