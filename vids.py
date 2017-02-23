class Video(object):
    def __init__(self, id, size):
        self.id = id
        self.size = size
    
    def get_id(self):
        return self.id

    def get_size(self):
        return self.size

    def set_id(self, id):
        self.id = id

    def set_size(self, size):
        self.size = size

class CacheServer(object):
    def __init__(self, max_capacity, latency):
        self.max_capacity = max_capacity #MBs
        self.latency = latency

    def get_max_capacity(self):
        return max_capacity

    def get_latency(self):
        return latency

    def set_max_capacity(self, max_capacity):
        self.max_capacity = max_capacity

    def set_latency(self, latency):
        self.latency = latency

class Endpoint(object):
    def __init__(self, data_center_latency, cache_server_latency, requests):
        self.cache_servers = []
        self.data_center_latency = data_center_latency

    def get_cache_servers(self):
        return self.cache_servers

    def get_data_center_latency(self):
        return self.data_center_latency

    def set_cache_servers(self, cache_servers):
        self.cache_servers = cache_servers

    def set_data_center_latency(self, data_center_latency):
        self.data_center_latency = data_center_latency
    
        
class Request(object):
    def __init__(self, video_id, endpoint_id, num_of_reqs):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.num_of_reqs = num_of_reqs

    def get_video_id(self):
        return self.video_id

    def get_endpoint_id(self):
        return self.endpoint_id

    def get_num_of_reqs(self):
        return self.num_of_reqs

    def set_video_id(self, video_id):
        self.video_id = video_id

    def set_endpoint_id(self, endpoint_id):
        self.endpoint_id = endpoint_id

    def set_num_of_reqs(self, num_of_reqs):
        self.num_of_reqs = num_of_reqs
        
def main():
