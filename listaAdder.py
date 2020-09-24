def checknumber(usernumbers):
    for numbers in usernumbers:
        if numbers.isdigit():
            return True
            
        else:
            return False
        
    
userinput = input('Please input your numbers separated by commas: \n')
userinput = userinput.split(',')

while True:
    if checknumber(userinput) == True:
        newlist_numbers = [int(i) for i in userinput]
        sumnumbers = sum(newlist_numbers)
        print(sumnumbers)
        break
    else:
        userinput = input('Please input your numbers separated by commas: \n')
        userinput = userinput.split(',')

