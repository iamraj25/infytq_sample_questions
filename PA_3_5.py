def slice(string):
    if len(string)<2:
        return -1
    elif len(string)==2:
        return string*2
    else:
        return string[:2]+string[-2:]


string = input()
print(slice(string))