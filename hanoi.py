def move(f, t):
    print("Move {} to {}".format(f, t))


# def moveVia(f, v, t):
#     move(f, v)
#     move(v, t)
#     NOT NEEDED BUT FOR EXPLANATION


moveVia("A", "B", "C")


def hanoi(n, f, h, t):
    if n == 0:
        pass
    else:
        hanoi(n - 1, f, t, h)
        move(f, t)
        hanoi(n - 1, h, f, t)


hanoi(4, "A", "B", "C")
#     HOWEVER MANY DISCS AS FIRST ARG.
# Hm. Still in the works, not satisfied.
