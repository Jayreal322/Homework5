def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)

def main():
    k = float(input("Enter k value: "))
    x = float(input("Enter starting x value: "))
    n = int(input("Enter number of times to loop: "))

    chaos(k, x, n)

main()
