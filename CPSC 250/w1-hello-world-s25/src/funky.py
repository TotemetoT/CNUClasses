# Write your funky method here

# Note: You will have a 0 for HW grade until this is defined!

def funky_factor(num):
    if num >= 0:
        if num == 0:
            return 1
        if num % 2 == 0:
            fact = 1
            for i in range(num):
                fact = fact * (i+1)
            return fact
        else:
            return num * 100
    else:
        return None


# Do not put while loop or input() above here!
if __name__ == '__main__':
    num = 1
    while num >= 0:
        num = int(input("Enter an Integer "))
        dummy = funky_factor(num)
        if dummy != None:
            print("funky_factor() = ", dummy)
        else:
            print("Must not be negative")

# You can delete, just place holder
