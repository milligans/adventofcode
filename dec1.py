def first():

    arr=[]
    i=0
    doc= open("1dec.txt")
    for line in doc:
        strrp=int(line.rstrip())
        arr.append(strrp)

    length_of_arr=len(arr)
    print(length_of_arr, " the length of the array is " , arr)
    for index in range(0,length_of_arr-1):

        if arr[index+1]>arr[index]:
            # print("the next one in the array is higher")
            # print(arr[index])
            i+=1
            # print(i)
        else:
            print("The next one in the array is lower or the same ", arr[index])
    print(i)
    first=(arr[0])
    second=(arr[1])
    third=(arr[2])
    sum=first+second+third
    j=0
    for index in range(1,length_of_arr-2):
        first=arr[index]
        second=arr[index+1]
        third=arr[index+2]
        next=sum
        sum= first+second+ third
        if sum-next>0:
            # print("The window is higher")
            j=j+1
        # print(sum, next)
        # print(first, second, third, " and the sum of these buggers is ", sum)

    print(j)

