"안녕안녕하세요".count(2)

for i in range(1, 101):
    print(f'{i}====>{"{:b}".format(i).count("0")}')



sum([ i for i in range(1, 101) if "{:b}".format(i).count("0") == 1])

print("hello")
print("hello")
print("hello")


