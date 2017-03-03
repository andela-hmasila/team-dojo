from parse_input import parse_input
from collections import defaultdict


def weight_calculator(requests, endpoints):
    weight = defaultdict(dict)
    for ep in endpoints:
        videos = requests[ep]
        for caches in endpoints[ep]:
            for k, v in caches.items():
                cache, value = k, v
            for video in videos:
                n_reqs = videos[video]
                if cache in weight:
                    if video in weight[cache]:
                        weight[cache][video] += (value * n_reqs)
                    else:
                        weight[cache][video] = (value * n_reqs)
                else:
                    weight[cache][video] = (value * n_reqs)
    for value in weight:
        print("{}:{}".format(value, weight[value]))
        # caches = { item[cache],  endpoints[ep])
        # print(caches)
        # for cache in caches:
        #     for video in videos:
        #         if video in weight[cache]:
        #             weight[cache][video]=caches[cache]
    return weight


def cache_optimizer(weight, sizes, capacity):
    for cache in weight:
        print(cache)
        d = weight[cache]
        print("_" * 30)
        for video, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
            video_size = sizes[int(video)]
            print("{}:{}:{}".format(video, video_size, value))


if __name__ == '__main__':
    requests, endpoints, sizes, capacity = parse_input("me_at_the_zoo.in")
    weight = weight_calculator(requests, endpoints)
    cache_optimizer(weight, sizes, capacity)
