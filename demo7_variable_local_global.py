value = 100


def foo():
    global value
    # value = 100
    print("[foo]value=", value)
    value += 50
    print("[foo]value=", value)


print("value=", value)

foo()

value2 = 100
print(f"value2={value2}, id={hex(id(value2))}")

value2 += 50
print(f"value2={value2}, id={hex(id(value2))}")
