import time

# start_time = time.time()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# # # Replace the nested for loops below with your improvements
# # for name_1 in names_1:
# #     for name_2 in names_2:
# #         if name_1 == name_2:
# #             duplicates.append(name_1)

# from binary_search_tree import BSTNode
# names1 = BSTNode(names_1[0])
# [names1.insert(name) for name in names_1]
# [duplicates.append(name) for name in names_2 if names1.contains(name)]
# # duplicates = [names1[first.contains(name) == True] for name in names_2]

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# allnames=names_2 + names_1

# def dupe_deriver(input):
#     seen = set()
#     seen_add = seen.add
#     return [x for x in allnames if x in seen and not seen_add(x)]  # Return the list of duplicates in this data structure

# duplicates = dupe_deriver(allnames)

############# fastest time at 0.005 seconds

def dupe_deriver(List1, List2):
    unique_set = set()
    duplicates = []
    for n in List1:
        unique_set.add(n)
    for n in List2:
        if n in unique_set:
            duplicates.append(n)

    return duplicates

duplicates = dupe_deriver(names_1, names_2)
# 0.005 secs

# duplicates = [x for ix, x in enumerate(allnames) if allnames.index(x) != ix]


# from binary_search_tree import BSTNode
# names1 = BSTNode(names_1[0])
# [names1.insert(name) for name in names_1]
# [duplicates.append(name) for name in names_2 if names1.contains(name)]
# 0.11 secs

# duplicates = [name for name in names_1 if(name in names_2)]  # Return the list of duplicates in this data structure
# 1.41 secs


# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")