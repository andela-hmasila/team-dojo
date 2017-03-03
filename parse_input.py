from operator import itemgetter
from collections import defaultdict


def parse_input(filename):
    file = open(filename, 'r')
    data = [line.strip("\n") for line in file.readlines()]

    count_data = [int(count) for count in data[0].split(" ")]
    video_sizes = [int(size) for size in data[1].split(" ")]

    videos, endpoints, requests, caches, capacity = [
        int(count) for count in data[0].split(" ")]
    endpoints_ = [0 for i in range(int(endpoints))]
    video_matrix = [endpoints_ for i in range(videos)]

    endpoint_data = defaultdict(list)
    current_line = 2
    for endpoint in range(0, endpoints):
        dc_latency, cache_servers = data[current_line].split(" ")
        current_line += 1
        cache_data = []
        for cache in range(0, int(cache_servers)):
            cs_id, cache_latency = data[current_line].split(" ")
            current_line += 1
            endpoint_data[endpoint].append(
                {cs_id: int(dc_latency) - int(cache_latency)})
    current_line += 1

    requests_data = defaultdict(dict)

    for line in range(current_line, len(data)):
        video_id, endpoint_id, end_requests = [
            int(n) for n in data[line].split(" ")]
        if endpoint_id in requests_data:
            if video_id in requests_data[endpoint_id]:
                requests_data[endpoint_id][video_id] += end_requests
            else:
                requests_data[endpoint_id][video_id] = end_requests
        else:
            requests_data[endpoint_id][video_id] = end_requests

    # for item in endpoint_data:
    #     print("{}:{}".format(item, endpoint_data[item]))
    #
    # for request in requests_data:
    #     print("{}:{}".format(request, requests_data[request]))
    return requests_data, endpoint_data, video_sizes, capacity

parse_input("me_at_the_zoo.in")
