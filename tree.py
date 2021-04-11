import time
import match
import random


class TreeNode:
    net_mask = 0
    net_number = 0
    prefix_length = 0
    is_node = False

    def __init__(self, net_mask, prefix_length, net_number):
        self.net_mask = net_mask
        self.prefix_length = prefix_length
        self.net_number = net_number
        self.is_node = True



class Tree:
    numbers = []
    lengths = []
    all_nodes = {}

    def __init__(self, numbers, lengths):
        self.numbers = numbers
        self.netmask = lengths
        self.all_nodes = {}

    def generate(self):
        time_now = time.time()
        for i in range(0, len(self.numbers)):
            index = 1
            now_number = self.numbers[i]
            now_length = self.lengths[i]
            for j in (0, now_length):
                last_number = (now_number >> (31 - j)) & 1
                index = (index << 2) | last_number
            now_mask = match.prefixlength2netmask(now_length)
            self.all_nodes[index] = TreeNode(net_mask=now_mask, prefix_length=now_length, net_number=now_number)
        time_complete = time.time()
        all_time = time_complete - time_now
        return all_time

    def match_all(self, route_count):
        time_begin = time.time()
        for i in range(0, route_count):
            which = random.randint(0, len(self.numbers) - 1)
            route = self.numbers[which]
            [now_number,is_success] = self.match_single_route(route)
        time_end = time.time()
        return time_end-time_begin

    def match_single_route(self, route):
        index = 1
        is_success = False
        now_number = 0
        for i in range(0, 31):
            is_right = (route >> (31 - i)) & 1
            index = (index << 1) | is_right
            if self.all_nodes.__contains__(index):
                and_result = route & self.all_nodes[index].net_mask
                if and_result == self.all_nodes[index].net_number:
                    is_success = True
                    now_number = and_result
        return now_number,is_success

