def kToF(k):
    return (k - 273.15) * 9 / 5 + 32

def main():
    print("Kelvin\tFahrenheit")
    print("------------------")

    for k in range(0, 301, 20):
        f = kToF(k)
        print(k, "\t", round(f, 2))

main()
