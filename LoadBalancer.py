import Server
import sched
import random as rnd
from numpy import random
import numpy as np

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
        temp_time = 0
        while temp_time < self.total_time:
            server = rnd.choices(self.servers, self.server_probs, k=1)[0]
            time_to_spare = random.exponential(scale=1/self.rate_of_packages)
            self.s.enterabs(temp_time, 1, server.handle_packet, argument=(temp_time, self))
            temp_time += time_to_spare

        # for t_unit in range(self.total_time):
        #     # TODO: if doesn't perform change to constant
        #     # x = random.poisson(lam=self.rate_of_packages, size=1)
        #     x = [self.rate_of_packages]
        #     times = [random.exponential(scale=1/self.rate_of_packages) for ii in range(x[0])]
        #     times[0] = 0
        #     servers = rnd.choices(self.servers, self.server_probs, k=x[0])
        #     temp_time = t_unit
        #     for (server, i) in zip(servers, range(x[0])):
        #         self.s.enterabs(temp_time + times[i], 1, server.handle_packet, argument=(temp_time + times[i], self))
        #         temp_time += times[i]
        #         # print(temp_time)

        self.s.run()

    def print_data(self):
        failed = 0
        packets_processed = 0
        total_waiting_time = 0
        total_proc_time = 0
        last_packet_time = 0

        for server in self.servers:
            failed += server.failed
            packets_processed += server.packets_processed
            total_waiting_time += server.total_waiting_time
            total_proc_time += server.total_process_time

            if last_packet_time < server.last_processed:
                last_packet_time = server.last_processed

        avg_waiting_time = total_waiting_time / packets_processed
        avg_proc_time = total_proc_time / packets_processed
        print(packets_processed, failed, last_packet_time, avg_waiting_time, avg_proc_time)
