s = "anagram"
t = "nagaram"

if len(s)==len(t):
    s_count={}
    t_count={}

    for i in s:
        s_count[i] = s_count.get(i, 0) + 1

    for i in t:
        t_count[i] = t_count.get(i, 0) + 1


    if s_count == t_count:
        print(True)
    else:
        print(False)

else:
    print(False)

