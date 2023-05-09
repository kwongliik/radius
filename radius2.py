def read_input(): 
    r = float(input("key in radius: "))
    return r

def calculate(r):
    pi = 3.142
    area = pi * r ** 2
    return area

def main():
    r = read_input()
    area = calculate(r)
    print(f"Area: {area}")

if __name__ == "__main__":
    main()

