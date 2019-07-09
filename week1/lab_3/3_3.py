def func_plural():
    firstLostOf = {1, 2, 25, 667, 65441}
    secondLostOf = {1, 2, 2888, 6121, 65441, 668, 54546}

    return(secondLostOf - firstLostOf) # елементи, що входять до 2 але не входять до 1                

        
print(func_plural())
        
