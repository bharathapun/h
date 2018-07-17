z=int(input())
if(z%400==0):
    print ("leapyear")
elif(z%4==0):
    print ("leapyear")
elif(z%100!=0):
    print ("leapyear")
else:
    print ("not leapyear")
