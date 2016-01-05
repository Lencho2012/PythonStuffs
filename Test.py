

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
	sum += num
print sum ##30?

list = ['larry', 'curly', 'moe']
if 'curly' in list:
	print 'yay'

for i in range(5):
	print 'dodo'

a = ['red', 'green', 'blue']
i = 0
while i < len(a):
	print a[i]
	i = i + 1
	
print list[:]

list = ['a', 'b', 'c', 'd']
list[0:2] = 'z'
print list


a = [5, 1, 4, 3]
print sorted(a)
print a

strs = ['aa', 'BB', 'zz', 'CC']
print sorted(strs, reverse=True)
print sorted(strs)

(x, y, z) = (42, 13, 'hike')
print z 

nums = [1, 2, 3, 4]
sqrs = [n * n for n in nums]

print sqrs

str = ['hello', 'and', 'goodbye']
shout = [s.upper() + '!!!' for s in str]
print shout

nums = [2, 8, 1, 5]
small = [n for n in nums if n <= 2]
print small


person = raw_input("Enter you here: ")
print('What', person)


def sayStuff():
	print "STuff"
	print "STUFF"
	print "MORE STUFF"
	
sayStuff()

