def sub_lists (l):
    base = []  
    lists = [base]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists
          
    return lists
  
l1 = [2,7,5]
print(sub_lists(l1))
