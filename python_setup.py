def hello():
    print("hello from inside a file")


hello()


def pack(var1, var2, var3):
    li = [var1, var2, var3]
    print(li)


pack(1, 2, 3)


def eat_lunch(li=[]):
    for i in range(len(li)):
        if i==0:
            print(f"First I eat {li[0]}")
        else:
            print(f"then I eat {li[i]}")
    print("Now my lunchbox is empty")



lunchbox = ['apple', 'sandwich', 'cookies']

eat_lunch(lunchbox)