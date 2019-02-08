#try:
#except:
#else:
#finally

while True:
    try:
        num = int(input("Please enter a number:"))
    except:
        print("Thats not a number!")
    else:
        print("great you enetered a number")
        break
    finally:
        print ("RUNS NO MATTER WHAT")
print ("Rest of the logic runs")