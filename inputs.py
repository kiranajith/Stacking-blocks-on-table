def prompt_user():
    """ function to propmt the user for input. also checks the validity of the inputs in terms of number and types of inputs
   
    Returns:
        a string with user inputs 
    """
    while True:                                             
        print('Provide three blocks to stack :')
        inp = input()
        str = "".join(list(inp))
        str=inp.replace(" ","")
    # Check for number of characters
        if len(str)!=3:                                     
            print('\nWrong number of inputs...retry\n--------------------------------------------------')   
    # Check for invalid input types      
        else:
            for i in range(len(str)):
                if str[i] not in ['r','g','b']:
                    print('\nInvalid input.Try again\n') 
                    break
    # check for duplicates
                if str[i] in str[i+1:]:
                    print('\nDuplicates...retry\n')
                    break
            if i==len(str)-1:
                break    
    return str