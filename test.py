import datetime

# x = input("Type a number: ")
# y = input("Type another number: ")

# sum = int(x) + int(y)

# print("The sum is: ", sum)


def calculator_loop(tiers, rates , property_worth):
    calculated_tax = 0
    for key,val in enumerate(tiers):
        if(property_worth < val and property_worth > tiers[key-1] and key > 0):
            calculated_tax += (property_worth - tiers[key-1]) * rates[key-1]
            # print("here,  ", calculated_tax , "= (",property_worth, "-", tiers[key-1], ") * ",rates[key-1], "Whennnn :::::  ", property_worth ,"is worth and value is", val , " and key is ", key)
        elif(property_worth > val and key > 0):
            calculated_tax += (val - tiers[key-1]) * rates[key-1]
            # print("TheRe,  ", (val - tiers[key-1]) * rates[key-1] , "= (",val, "-", tiers[key-1], ") * ",rates[key-1], "Whennnn :::::  ", property_worth ,"is worth and value is", val , " and key is ", key)
            if(property_worth > tiers[len(tiers)-1] and key == len(tiers)-1):
                calculated_tax += (property_worth - tiers[len(tiers)-1]) * rates[len(rates)-1] 
                
    return calculated_tax
    # pass



def stamp_duty_calculator(property_worth, first_property, residential_property, only_property, d1, d2, uk_resident):
    residential_tiers = [250000, 925000, 1500000]
    residential_rates = [0.05, 0.10, 0.12]
    
    non_residential_tiers = [150000, 250000]
    non_residential_rates = [0.02, 0.05]
    
    first_property_threshold = 425000 
    first_property_threshold2 = 625000 
    
    tax = 0

    message=""

    if((first_property == True and property_worth < first_property_threshold) or (property_worth < 250000)):
        message = "Zero"
        return tax
    elif((first_property == True and property_worth < first_property_threshold2 )):
        tax = (property_worth - first_property_threshold) * 0.05
        message = "Only 5 %"
        return tax         
    else:  
        if(residential_property):
            tax += calculator_loop(residential_tiers, residential_rates , property_worth)
        else:
            tax += calculator_loop(non_residential_tiers, non_residential_rates , property_worth)
        
        
    # + 3 % for additional property                
    if(not only_property and d2 > d1):
        tax += tax * 0.03
        message = "3 percent surcharge"
    
    if(not uk_resident):
        tax += tax * 0.02
        message = "2 percent surcharge"
    
    
    # print("Tax: ",tax)
    print("message: ",message)
    

    return tax
    pass

property_worth = 724000
first_property = True
residential_property = True
only_property = False
d1 = datetime.datetime(2023, 4, 13) # current property sold on
d2 = datetime.datetime(2023, 4, 13) # new property bought on
uk_resident = False
print("tax calculated: ",stamp_duty_calculator(property_worth, first_property, residential_property, only_property, d1,d2, uk_resident))


