import sched
import sys
import Server
import LoadBalancer


def main():
    print("hello")
    s = sched.scheduler(Time, zero)
    s.enterabs(10, 1, printer, argument=("first",))
    s.enterabs(3, 2, printer, argument=("second",))
    s.run()



if __name__ == "__main__":
    main()
