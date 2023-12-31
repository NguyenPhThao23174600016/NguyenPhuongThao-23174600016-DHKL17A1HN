#bai_1.6:chia deu so keo
alice_candies=eval(input("Nhap so keo alice : "))
bob_candies=eval(input("Nhap so keo bob : "))
carol_candies=eval(input("Nhap so keo carol : "))
to_smash=(alice_candies+bob_candies+carol_candies)%3
print("to smash=",to_smash)
