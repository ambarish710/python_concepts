import collections

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]

def accountsMerge(accounts):
    em_to_name = {}
    graph = collections.defaultdict(set)

    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            em_to_name[email] = name

    print(graph)

    seen = set()
    ans = []
    for email in graph:
        if email not in seen:
            seen.add(email)
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            ans.append([em_to_name[email]] + sorted(component))
    return ans

print(accountsMerge(accounts=accounts))

# from collections import defaultdict
#
# accounts_list = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# names_dict = defaultdict(set)
#
# #print(names_dict)
# for account in accounts_list:
#     names_dict[account[0]].update(account[1:])
#
# print(names_dict)


# #a = [1,2,3,4,5,6,7,8]
# a = [0,0,0,0,1,1,1,1]
#
# def find_index(some_list, target):
#     low = 0
#     high = len(some_list)
#
#     while low < high:
#         mid = int((low+high)/2)
#
#         if some_list[mid] >= target:
#             high = mid
#         else:
#             low = mid + 1
#
#     return low if low < len(some_list) else None
#
# print(find_index(some_list=a, target=1))