str_list = [["some", "special"], ["text", "for", "you"], ["-", 50]]

result_str = ''

for i in str_list:
    for j in i:
        result_str+= str(j) + ' '


print(result_str)