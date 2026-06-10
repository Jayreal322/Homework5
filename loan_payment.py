def calcPmt(P0, r, k, N):
    d = P0 / ((1 - (1 + r / k) ** (-N * k)) / (r / k))
    return d

def main():
    P0 = float(input("Enter amount financed: "))
    r = float(input("Enter annual interest rate as decimal, example 0.05 for 5%: "))
    k = int(input("Enter number of times compounded per year: "))
    N = int(input("Enter number of years: "))

    payment = calcPmt(P0, r, k, N)

    print("Monthly payment is: $", round(payment, 2))

main()
