"""A program to suggest a gift for a person based on their social status"""
#Programmer: Toni Lachmaniucu
#Date: 2017-10-03

def main():
    group = input("Are they a friend or a family member?: ")
    if group == "Family" or group == "Fam" or group == "Fm":
        budget = int(input("Please enter your budget for purchase of gift: "))
        familyGift(budget)
    elif group == "Friend" or group =="Fr" or group == "Frien":
        budget = int(input("Please enter how much you are willing to spend on your friend."))
        friendGift(budget)

def familyGift(amount):
    if amount > 0 and amount < 10:
        print("You can buy them some candy, or make them something special!")
    elif amount > 10 and amount < 50:
        print("You can buy them some article of clothing!")
    else:
        print("Error 709")

def friendGift(amount):
    if amount > 0 and amount < 10:
        print("You can buy them some candy, or take them out to Tims")
    elif amount > 10 and amount < 50:
        print("You can buy them some books")
    else:
        print("Error 709")


main()
