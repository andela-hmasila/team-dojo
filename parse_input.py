def parse_input(filename):
    file = open(filename, 'r')
    data = [line.strip("\n") for line in file.readlines()]

    count_data = [int(count) for count in data[0].split(" ")]
    video_sizes = [int(size) for size in data[1].split(" ")]

    videos, endpoints, requests, caches, capacity = [
        int(count) for count in data[0].split(" ")]

    endpoint_data = []
    current_line = 2
    for endpoint in range(0, endpoints):
        dc_latency, cache_servers = data[current_line].split(" ")
        current_line += 1
        cache_data = []
        for cache in range(0, int(cache_servers)):
            cs_id, cache_latency = data[current_line].split(" ")
            current_line += 1
            cache_data.append({cs_id: cache_latency})
        endpoint_data.append([dc_latency, cache_data])
    current_line += 1

    requests_data = []
    for line in range(current_line, len(data)):
        video_id, endpoint_id, end_requests = data[line].split(" ")
        requests_data.append([video_id, endpoint_id, end_requests])

    return(requests_data, endpoint_data)
