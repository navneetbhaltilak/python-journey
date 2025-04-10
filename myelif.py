a=int(input("Enter hour ="))
b=int(input("Enter minute ="))
c=int(input("Enter second ="))
e=str(input("Enter your name ="))
d=print("Time is ",a,":",b,":",c,)
if(6<=a<=11 and 0<=b<=59 and 0<=c<=59) :
  print("Good Morning Mr.",e)
elif (17>=a>=12 and 59>=b>=0 and 59>=c>=0):
    print("Good Afteernoon Mr.",e)
elif(19>=a>=18 and 59>=b>=0 and 59>=c>=0):
      print("Good Eveningn Mr.",e)
elif (23>=a>=20 and 59>=b>=0 and 59>=c>=0) :
      print("Good Night Mr.",e)

else :
  print("invalid")