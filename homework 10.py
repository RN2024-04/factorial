def test (*params):
    print(*params)

test(2,3,4, "Lena")

def funk(n):
    if n <= 1:
        return 1
    else:
        return (n * funk (n-1))
print (funk(5))