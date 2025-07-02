def conditional_series(a):
    series = []
    for i in range(1, a + 1):
        if i % 2 != 0:
            series.append(2 * (len(series)) + 1)
    print(", ".join(map(str, series)))


a = int(input("Enter a number: "))
conditional_series(a)