def find_target_positions(input_string, target_word):
    target_list=[]
    for i in range(len(input_string)):
        if target_word == input_string[i]:
            target_list.append(i)
    return target_list


input_string = input().split(" ")
target_word=input()
print(find_target_positions(input_string, target_word))