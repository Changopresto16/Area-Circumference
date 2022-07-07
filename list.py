#Queston3

def Merge(l_1, l_2):
    final_list = l_1 + l_2
    final_list.sort()
    return(final_list)
  
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
print(Merge(l_1, l_2))