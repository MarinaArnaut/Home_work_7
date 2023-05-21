my_list = [15, 17, 16]
my_list3 = list(map(lambda x: str(x)+'\n', my_list))
print(my_list3)
with open('1.txt', 'w') as f:
    f.writelines(my_list3)
