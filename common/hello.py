def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)


res = []
for i in range(int(input())):
    res.append(f(i))
print(res)

res = "".join(map(str, res))
count = res.count("1")
print(count)
