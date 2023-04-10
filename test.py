import datetime

# x = input("Type a number: ")
# y = input("Type another number: ")

# sum = int(x) + int(y)

# print("The sum is: ", sum)


# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

def calculator_loop(tiers, rates , property_worth):
    calculated_tax = 0
    for key,val in enumerate(tiers):
        if(property_worth < val and property_worth > tiers[key-1] and key > 0):
            calculated_tax += (property_worth - tiers[key-1]) * rates[key-1]
            print("here,  ", calculated_tax , "= (",property_worth, "-", tiers[key-1], ") * ",rates[key-1], "Whennnn :::::  ", property_worth ,"is worth and value is", val , " and key is ", key)
        elif(property_worth > val and key > 0):
            print("taxx before" , calculated_tax)
            calculated_tax += (val - tiers[key-1]) * rates[key-1]
            print("TheRe,  ", (val - tiers[key-1]) * rates[key-1] , "= (",val, "-", tiers[key-1], ") * ",rates[key-1], "Whennnn :::::  ", property_worth ,"is worth and value is", val , " and key is ", key)
            print("taxx after" , calculated_tax)
            if(property_worth > tiers[len(tiers)-1] and key == len(tiers)-1):
                print(key,val,"last")
                calculated_tax += (property_worth - tiers[len(tiers)-1]) * rates[len(rates)-1] 
                
    return calculated_tax
    # pass



def stamp_duty_calculator(property_worth, first_property, residential_property, only_property, d1, d2, non_uk_resident):
    residential_tiers = [250000, 925000, 1500000]
    residential_rates = [0.05, 0.10, 0.12]
    
    non_residential_tiers = [150000, 250000]
    non_residential_rates = [0.02, 0.05]
    
    first_property_threshold = 425000 
    first_property_threshold2 = 625000 
    tax = 0


    if((first_property == True and property_worth < first_property_threshold) or (property_worth < 250000)):
        print("Zero")
        return tax
    elif((first_property == True and property_worth < first_property_threshold2 )):
        print("Only 5 %")
        tax = (property_worth - first_property_threshold) * 0.05
        return tax         
    else:  
        if(residential_property):
            print("tax beforee",tax)
            tax += calculator_loop(residential_tiers, residential_rates , property_worth)
            print("tax afterrr",tax)
        else:
            print("tax beforee",tax)
            tax += calculator_loop(non_residential_tiers, non_residential_rates , property_worth)
            print("tax afterrr",tax)
        # print(first_property, property_worth)
        # for key,val in enumerate(residential_tiers):
        #     if(property_worth < val and property_worth > residential_tiers[key-1] and key > 0):
        #         tax += (property_worth - residential_tiers[key-1]) * residential_rates[key-1]
        #         print("here,  ", tax , "= (",property_worth, "-", residential_tiers[key-1], ") * ",residential_rates[key-1], "Whennnn :::::  ", property_worth ,"is worth and value is", val , " and key is ", key)
        #     elif(property_worth > val and key > 0):
        #         print("taxx before" , tax)
        #         tax += (val - residential_tiers[key-1]) * residential_rates[key-1]
        #         # print("theerre ",val, " - ", residential_tiers[key-1] , " * ", residential_rates[key-1], " = ", tax)
        #         print("TheRe,  ", (val - residential_tiers[key-1]) * residential_rates[key-1] , "= (",val, "-", residential_tiers[key-1], ") * ",residential_rates[key-1], "Whennnn :::::  ", property_worth ,"is worth and value is", val , " and key is ", key)
        #         print("taxx after" , tax)
        #         # if(property_worth > residential_tiers[len(residential_tiers)-1] and key < len(residential_tiers)):
        #         if(property_worth > 1500000 and key == len(residential_tiers)-1):
        #             print(key,val,"last")

        #             tax += (property_worth - 1500000) * 0.12
        
        
        
    # + 3 % for additional property                
    if(not only_property and d2 > d1):
        tax += tax * 0.03
    
    print("Tax1:",tax)

    return tax
    pass

property_worth = 724000
first_property = True
residential_property = True
only_property = False
d1 = datetime.datetime(2023, 4, 13) # current property sold on
d2 = datetime.datetime(2023, 4, 13) # new property bought on
non_uk_resident = False
print(stamp_duty_calculator(property_worth, first_property, residential_property, only_property, d1,d2, non_uk_resident))

