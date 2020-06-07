subject = list(input().split(","))
verb = list(input().split(","))
obj = list(input().split(","))
for s in subject:
    for v in verb:
        for o in obj:
            print(s, v, o)
