def test1():
    a = {}
    for i in range(0, 100):
        a[i] = 'hello ' + str(i)

    for key, value in a.items():
        print(key)


def test2():
    a = set()
    for i in range(0, 100):
        a.add(i)



if __name__ == '__main__':
    test1()
