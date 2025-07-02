def generate_series(a):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    print(", ".join(map(str, series)))


a = int(input("Enter a number: "))
generate_series(a)
