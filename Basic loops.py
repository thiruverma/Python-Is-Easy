for num in range(1,101):
    if num>1:
        for i in range(2,num):
              if num%i==0:
                break
        else:
            print("Prime")
            continue

    if num%3==0 and num%5==0:
        print("Fizzbuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)     

        
        
        

    

 

                              
        
            



             
            






    