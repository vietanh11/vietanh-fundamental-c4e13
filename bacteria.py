b  = int(input("how many bacteria are there: "))
time  = int(input("how much time in minute will we wait :"))
if (time%2) ==0 :
    total = b *2 * (time // 2)

    print("after", time ,"mintues we would have ", total,"minutes")

else :
    total = b *2 * ((time-1)//2)

    print("after", time ,"mintues we would have ", total,"minutes")
