# from collections import Counter
# from collections import defaultdict
#
# def anagram_checker(S, P):
#     P_len = len(P)
#     S_len = len(S)
#
#     # Corner Cases
#     # if P_len > S_len:
#     #     return []
#
#     output = []
#     # Approach 1
#     # p_count = defaultdict(int)
#     # for char in P:
#     #     p_count[char] += 1
#
#     # Approach 2
#     p_count = Counter(P)
#
#
#     for i in range(S_len - P_len + 1):
#         tmp_string = S[i:i+P_len]
#         tmp_string_count = Counter(tmp_string)
#         if tmp_string_count == p_count:
#             output.append(i)
#
#     return (output)
#
#
# S = "aabccab"
# P = "abc"
# print(anagram_checker(S=S, P=P))











import threading

def connect():
    ....

def computation():
    ...

for i in range(1000):
    p1 = threading.Thread(connect, args=[])

# p1 = threading.Thread(connect, args=[])
# p2 = threading.Thread(connect, args=[])
# ...
#
#
# p1.start()
# p2.start()
#
#
# p1.wait()
# p2.wait()


import requests

def planet_search(climate, terrain):
    planets = []
    total_count = json_output["count"]
    current_count = 0
    for 
    json_output = requests.get(url="https://swapi.dev/api/planets/")
    results_list = json_output["results"]
    for entity_dict in results_list:
        if entity_dict["climate"] == climate and entity_dict["terrain"] == terrain:
            planets.append(entity_dict["name"])
    return planets