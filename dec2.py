def second(textfile):
    arr=[]

    f=0
    d=0
    u=0
    a=0

    doc= open(textfile)
    for line in doc:
        strrp=line.strip("\n")
        nu = strrp.split(" ")
        entry=(nu[0], int(nu[1]))
        arr.append(entry)

    for item in arr:
        # print(item[0])
        if item[0] == "down":
            # print("down")
            # d=d+item[1]
            a = a + item[1]
            # print(f, d, a)
        if item[0] == "up":
            # print("up")

            a = a - item[1]
            # print(f, d, a)
        if item[0]=="forward":
            # print("forward")
            f=f+item[1]
            d=d+(a*item[1])

            # print(f, d, a)



    vertical= d -u
    print(f"The forward is {f}, (the down is {d}, and the up is {u} moves, the total aim is {a}), the total y movement is {vertical}.The "
          f"product of the forward * depth is {vertical * f}")






