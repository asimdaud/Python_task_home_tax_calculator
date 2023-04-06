# x = input("Type a number: ")
# y = input("Type another number: ")

# sum = int(x) + int(y)

# print("The sum is: ", sum)


# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

# def solution(A):
#     # Implement your solution here
#     pass

def stamp_duty_calculator(property_worth, first_property, residential_property, only_property, non_uk_resident):
    tiers = [250000, 925000, 1500000]
    rates = [0.05, 0.10, 0.12]
    first_property_threshold = 425000 
    first_property_threshold2 = 625000 
    tax = 0
    tax2 = 0
    tax3 = 0

    if((first_property == True and property_worth < first_property_threshold) or (property_worth < 250000)):
        print("Zero")
        return tax 
    else:   
        print(first_property, property_worth)
        for key,val in enumerate(tiers):
            if(property_worth < val and property_worth > tiers[key-1] and key > 0):
                tax += (property_worth - tiers[key-1]) * rates[key-1]
                print("here,  ", tax , "= (",property_worth, "-", tiers[key-1], ") * ",rates[key-1], "Whennnn :::::  ", property_worth ,"is worth and value is", val , " and key is ", key)
                # return tax
            elif(property_worth > val and key > 0):
                print("taxx before" , tax)
                tax += (val - tiers[key-1]) * rates[key-1]
                # print("theerre ",val, " - ", tiers[key-1] , " * ", rates[key-1], " = ", tax)
                print("TheRe,  ", (val - tiers[key-1]) * rates[key-1] , "= (",val, "-", tiers[key-1], ") * ",rates[key-1], "Whennnn :::::  ", property_worth ,"is worth and value is", val , " and key is ", key)
                print("taxx after" , tax)
                # if(property_worth > tiers[len(tiers)-1] and key < len(tiers)):
                if(property_worth > 1500000 and key == len(tiers)-1):
                    print(key,val,"last")

                    tax += (property_worth - 1500000) * 0.12


    # print("Tax-One",tax)
    # return tax




    # # if(property_worth <= tiers[0]):
    # #     return 0
    
    # # for key, tier in enumerate(tiers):
    # # if(property_worth>250000):
    #     # print("a",property_worth,tax)
    #     if(property_worth<925000):
    #         value_to_be_taxed = property_worth - 250000
    #         tax2 += value_to_be_taxed * 0.05
    #         # print("b",property_worth,tax)
    #     elif(property_worth > 925000):
    #         value_to_be_taxed = 925000 - 250000
    #         tax2 += value_to_be_taxed * 0.05
    #         # print("c",property_worth,tax)
    #         if(property_worth<1500000):
    #             value_to_be_taxed = property_worth - 925000
    #             tax2 += value_to_be_taxed * 0.10
    #             # print("d",property_worth,tax)
    #         elif(property_worth>1500000):
    #             # print("leee",property_worth, value_to_be_taxed,value_to_be_taxed * 0.12,tax)
    #             value_to_be_taxed = property_worth - 1500000
    #             tax2 += value_to_be_taxed * 0.12
    #             # print("e",property_worth, value_to_be_taxed,value_to_be_taxed * 0.12,tax)





    #     value_to_be_taxed = 0
    #     for key, tier in enumerate(tiers):

    #     # value_to_check = property_worth - tier
    #     # if(property_worth > tiers[0]):
    #         # print(property_worth, key, tier, len(tiers))
    #         if(key > 0):
    #             if(property_worth <= tier and (property_worth>tiers[key-1])):
    #                 # print("checking vlaues :: ",property_worth , tier, tax)
    #                 value_to_check = property_worth - tiers[key-1]
    #                 tax3 += value_to_check * rates[key-1]
    #                 # print( key ,property_worth, "-", tiers[key-1],"=" ,value_to_check," :: ", rates[key-1] ,":: ::tax::" , tax , "----",  value_to_check * rates[key-1])

    #             elif(property_worth > tier):
    #                 if(key+1 < len(tiers)):
    #                     # print( tier , tiers[key-1])
    #                     value_to_check = tier - tiers[key-1]
    #                     tax3 += value_to_check * rates[key-1]
    #                     # print( key ,property_worth, "-", tiers[key-1],"=" ,value_to_check," :: tax::" , tax)
    #                 value_to_check = tier - tiers[key-1]
    #                 tax3 += value_to_check * rates[key-1]
    #                 # print( key ,property_worth, "-yeet-", tiers[key-1],"=" ,value_to_check," :: tax::" , tax)

    #             # else:
    #             #     value_to_check = tiers[key+1] - tier
    #             #     tax += value_to_check * rates[key]
    #             #     print( key ,property_worth, "-", tier,"=" ,value_to_check," :: tax::" , tax)
    print("Tax1:",tax," -----    Tax2: ", tax2,"  ------  Tax3:",tax3)

    return tax
    pass

property_worth = 260000
# property_worth = 1800000
first_property = True
residential_property = True
only_property = True
non_uk_resident = False
print(stamp_duty_calculator(property_worth, first_property, residential_property, only_property, non_uk_resident))


