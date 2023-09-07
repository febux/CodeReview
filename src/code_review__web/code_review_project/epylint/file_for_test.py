def auto_launch_coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


@auto_launch_coroutine
def bare_bones():
    print("My first Coroutine!")
    try:
        while True:
            value = (yield)
            print(value)
    except GeneratorExit:
        print("Exiting coroutine...")


@auto_launch_coroutine
def joint_print():
    try:
        while True:
            part_1 = (yield)
            part_2 = (yield)
            print("{} {}".format(part_1, part_2))
    except GeneratorExit:
        print("Exiting coroutine...")


coroutine_bare = bare_bones()
coroutine_bare.send("First Value")
coroutine_bare.send("Second Value")
coroutine_bare.close()

coroutine_joint = joint_print()
coroutine_joint.send("First Value")
coroutine_joint.send("Second Value")
coroutine_joint.close()
