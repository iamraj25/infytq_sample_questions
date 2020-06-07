def build_index_grid(rows, columns):
    result_list = []
    for i in range(rows):
        result_list.append([])
        for j in range(columns):
            result_list[i].append('{},{}'.format(i,j))
    return result_list


rows = int(input())
columns = int(input())
result = build_index_grid(rows, columns)
print(result)