def write(msg):
    print("~" * (len(msg) + 4))
    print(f"  {msg}")
    print("~" * (len(msg) + 4))


word = input("Digite seu texto:")
write(word)

