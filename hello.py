def square(y):
	print("{}的平方是{},三次方式是{}".format(y,y*y,y**y))

x = int(input("請輸入一個數字："))
print("您輸入的是",x)
if (x<=0):
	print("您輸入的值為負數")
elif(x==0):	
	print("您輸入的值等於0")
else:
	for i in range(1,x+1):
		square(i)