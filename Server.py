import queue


class Server:
    def __init__(self, queue_size, mu):
        self.queue = queue.Queue()
        self.size = queue_size
        self.proc_rate = mu



