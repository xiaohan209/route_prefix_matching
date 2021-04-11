class TreeNode:
    net_mask = 0
    net_number = 0
    is_node = False

    def __init__(self,net_mask,prefix_length,net_number):
        self.net_mask = net_mask
        self.prefix_length = prefix_length
        self.net_number = net_number

