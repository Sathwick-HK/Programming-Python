a = input()
b = input()
c = input()
l = input()
m = input()
n = input()
x = input()
y = input()
z = input()
d1 = (a*b)/100
t1 = a-d1+c
d2 = (l*m)/100
t2 = l-d2+n
d3 = (x*y)/100
t3 = x-d3+z
print("Flipkart Rs."+t1)
print("Snapdeal Rs."+t2)
print("Amazon Rs."+t3)
if(t1<=t2 && t1<=t3):
    print("He will prefer Flipkart")
elif(t2<=t3 && t2<=t1):
    print("He will prefer Snapdeal")
else:
    print("He will prefer Amazon")