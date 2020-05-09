a = int(input())
b = int(input())
c = int(input())
l = int(input())
m = int(input())
n = int(input())
x = int(input())
y = int(input())
z = int(input())
d1 = int((a*b)/100)
t1 = a-d1+c
d2 = int((l*m)/100)
t2 = l-d2+n
d3 = int((x*y)/100)
t3 = x-d3+z
print("Flipkart Rs."+str(t1))
print("Snapdeal Rs."+str(t2))
print("Amazon Rs."+str(t3))
if(t1<=t2 & t1<=t3):
    print("He will prefer Flipkart")
elif(t2<=t3 & t2<=t1):
    print("He will prefer Snapdeal")
else:
    print("He will prefer Amazon")
