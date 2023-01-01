import Server
import sched
import random as rnd
from numpy import random

t = 0


def Time():
    global t
    return t


def inc_time(arg):
    global t
    t += arg


class LoadBalancer:
    def __init__(self, TT, server_num, probs, lamb, queues, mus):
        self.servers = [Server.Server(queues[i], mus[i]) for i in range(server_num)]
        self.server_num = server_num
        self.total_time = TT
        self.rate_of_packages = lamb
        self.server_probs = probs
        self.s = sched.scheduler(Time, inc_time)

    def run(self):
        for t_unit in range(self.total_time):
            servers = rnd.choices(self.servers, self.server_probs, k=1)
            for server in servers:
                packets_thrown += server.add_message()
