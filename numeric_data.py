num = 3.1
print(type(num))

print(3 / 2)
#Python 3 will return the correct anwser, to drop the decimel we need to use floor division

print(3//2)

num = 1 
num += 1
print(num)

#Rounding
print(round(3.657493,2))

#defined a funtion to find the average of a list
def average(testTimes):
	return(sum(testTimes)/len(testTimes))

testTimes = [3.55, 8.32, 15.12, 22.123, 14.64, 19.2, 49.3]
if average(testTimes) < 30:
	for user in testTimes:
		user += 1
		print(round(user, 2))
else:
	print("That's all")	