import queue
from LoadBalancer import *


class Server:
    def __init__(self, queue_size, mu):
        self.queue = queue.Queue()
        self.max_size = queue_size
        self.proc_rate = 1 / mu
        self.is_working = False
        self.failed = 0
        self.packets_processed = 0
        self.total_waiting_time = 0
        self.total_process_time = 0
        self.last_processed = 0



