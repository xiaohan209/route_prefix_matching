def prefix2netmask(netmask):
    if netmask < 0:
        return 0
    elif netmask >= 1<<32:
        return 0
    else:
        return 1<<32 - 1<<(32-netmask)


def prefix2string(prefix):
    n_4 = prefix & 255
    n_3 = (prefix >> 8) & 255
    n_2 = (prefix >> 16) & 255
    n_1 = (prefix >> 24) & 255
    return str(n_1) + "." + str(n_2) + "." + str(n_3) + "." + str(n_4)



def string2prefix(prefix):
    all_segment = prefix.split('.')
    sum_prefix = 0
    for segment in all_segment:
        sum_prefix = sum_prefix << 8 | int(segment)
    return sum_prefix




