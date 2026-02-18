# use buble sort algorithm to sort a list

a = [1,4,5,64,3,3, -3,2343,22,89,34,122234334,22]

def pai_xu(number_set):
    
    for num_1 in range(len(number_set)-1):
        for num_2 in range(len(number_set)- num_1-1):
            if number_set[num_2] > number_set[num_2 +1]:
            
                ref_num = number_set[num_2 +1]
                number_set[num_2 +1] = number_set[num_2]
                number_set[num_2] = ref_num
        
    return number_set

print(pai_xu(a))
            
        
        
