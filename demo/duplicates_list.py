
list1 = [100,110,120,100,130,100,140,110,120]

set1 = set()
dup = list()

for item in list1:

    if item in set1:
        dup.append(item)
    else:
        set1.add(item)

print(dup)


duplicate_list = []
#
# total_items = len(list1)  #7
#
# for i in range(0,total_items):
#     for item in list1:
#         if item == list1[i+1]:
#             duplicate_list.append(item)
#         else:
#             pass
#
# print(duplicate_list)
# print(len(duplicate_list))



