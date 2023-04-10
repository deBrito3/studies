def maior(*num):
    print("Analisando os valores passados...")
    major = 0
    for i in num:
        print(f"{i} ", end='')
        if i == 0:
            major = i
        else:
            if i > major:
                major = i
    print(f"Foram informados números {len(num)} ao todo")
    print(f"O maior deles foi: {major}")


maior(5, 6, 8, 9, 10)
