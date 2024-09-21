nmr1 = int(input("Enter 1st number:"))
nmr2 = int(input("Enter 2nd number:"))
sum_result = nmr1 + nmr2
print ("Sum of the two numbers is: ", sum_result)

answer = ""
answer2 = ""
answer3 = ""
answer4 = ""
while answer.lower() not in ["yes" , "no"]:
        answer = input("Do you want to * or / the result, yes or no?")
        if answer.lower() ==  "yes":
            answer2 = input("* or /?")
            if answer2.lower() == "*":
                answer3= float(input("By how much?:"))
                print ("The result is:", sum_result * answer3)

            elif answer2.lower() == "/":
                answer4= float(input("By how much?:"))
                while answer4 ==0:
                    print("You can't divide by zero!, try  again:")
                    answer4= float(input("By how much?:")) 
                    print("You can't divide by zero!, try  again:")
                if  answer4 != 0:
                    print ("The result is:", sum_result / answer4)
                  

        if answer.lower () == "no":
                print("Goodbye!")


                        




























