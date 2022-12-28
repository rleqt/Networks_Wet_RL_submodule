import sched
import time

t = 0


def Time():
    global t
    return t


def zero(arg):
    global t
    t += arg
    print(f"argument is {arg} and time is {t}")


def printer(arg):
    print(arg)
    pass


def main():
    print("hello")
    s = sched.scheduler(Time, zero)
    s.enterabs(10, 1, printer, argument=("first",))
    s.enterabs(3, 2, printer, argument=("second",))
    s.run()


if __name__ == "__main__":
    main()
