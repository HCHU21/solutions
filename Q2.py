check_valid(file):
    with open(file) as f:
        allValid = true
        errorCodes =[]
        for line in f:
            count = 0
            allValid = line.isValid()
            if line.isValid != true:
                errorCodes.appned(error)

            if allValid == true:
                print("Yes")
            else:
                a = "No"+ errorCodes[count]
            count+=1
