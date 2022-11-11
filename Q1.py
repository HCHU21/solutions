def Q1():
    num_tee_shop = int(input())
    size_tee_shop= input().split()
    num_req= int(input())
    size_request= input().split()
    req_fullfil = []
    for i in size_request:
        req_fullfil1 = []
        for j in size_tee_shop:
            if i == j:
                req_fullfil1.append(1)
            elif i in j:
                req_fullfil1.append(1)

            else:
                req_fullfil1.append(0)
        if 1 in req_fullfil1:
            req_fullfil.append(1)
        else:
            req_fullfil.append(0)

    if 0 in req_fullfil:
        print("No")
    else:
        print("Yes")
