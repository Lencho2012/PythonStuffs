# 
# 
# # squares = [1, 4, 9, 16]
# # sum = 0
# # for num in squares:
# # 	sum += num
# # print sum ##30?
# 
# list = ['larry', 'urly', 'moe']
# if 'curly' in list:
# 	print 'yay'	
# else:
# 	print 'NOOO'
# 
# for i in range(5):
# 	print 'dodo'
# 	
# str = '255.255'
# #strLen = len(str)
# 	
# 
# a = ['red', 'green', 'blue']
# i = 0
# while i < len(a):
# 	print a[i]
# 	i = i + 1
# 	
# print list[:]
# 
# list = ['a', 'b', 'c', 'd']
# list[0:2] = 'z'
# print list
# 
# 
# a = [5, 1, 4, 3]
# print sorted(a)
# print a
# 
# strs = ['aa', 'BB', 'zz', 'CC']
# print sorted(strs, reverse=True)
# print sorted(strs)
# 
# (x, y, z) = (42, 13, 'hike')
# print z 
# 
# nums = [1, 2, 3, 4]
# sqrs = [n * n for n in nums]
# 
# print sqrs
# 
# str = ['hello', 'and', 'goodbye']
# shout = [s.upper() + '!!!' for s in str]
# print shout
# 
# nums = [2, 8, 1, 5]
# small = [n for n in nums if n <= 2]
# print small
# 
# for i in range(len(str)):
# 	if str[i] == '2':
# 		print 'DONE'
# ##person = raw_input("Enter you here: ")
# ##print('What', person)
# 
# 
# def sayStuff():
# 	print "STuff"
# 	print "STUFF"
# 	print "MORE STUFF"
# 	
# sayStuff()
# 
# def main():
# 	sayStuff()
# 	sumProb(100, 200)
# 	
# def sumProb(x, y):
# 	sum = x + y
# 	sentence = 'Sum of {} and {} is {}.'.format(x, y, sum)
# 	print (sentence)
	
def netmaskLength():
	netmask = raw_input("Enter Netmask: ")
	octSeperator = []
	for a in range(len(netmask)):
		if netmask[a] == '.':
			octSeperator.append(a)
	print '------Indices for Octets------'
	print octSeperator 
	firstOct = netmask[:octSeperator[0]]
	secondOct = netmask[octSeperator[0]+1:octSeperator[1]]
	thirdOct = netmask[octSeperator[1]+1:octSeperator[2]]
	fourthOct = netmask[octSeperator[2]+1:]
	print '------Individual Octets------'
	print firstOct
	print secondOct
	print thirdOct
	print fourthOct
	print '------Converting to Binary------'
	print "{0:b}".format(int(firstOct)) + ' ---> Printed as a Binary number'
	binFirst = int("{0:b}".format(int(firstOct))) #Binary number
	print "{0:b}".format(int(secondOct))
	binSecond = int("{0:b}".format(int(secondOct)))
	print "{0:b}".format(int(thirdOct))
	binThird = int("{0:b}".format(int(thirdOct)))
	print "{0:b}".format(int(fourthOct))
	binFourth = int("{0:b}".format(int(fourthOct)))
	print '------Full Binary------'
	# print binFirst
# 	print binSecond
# 	print binThird
# 	print binFourth
	
	strBinFirst = ("{0:b}".format(int(firstOct))) #Binary as a string
	for a in range(8):
		if len(strBinFirst) != 8:
			strBinFirst = "0" + strBinFirst	#turning strings into full octets
	print strBinFirst
	
	strBinSecond = ("{0:b}".format(int(secondOct))) #Binary as a string
	for a in range(8):
		if len(strBinSecond) != 8:
			strBinSecond = "0" + strBinSecond	#turning strings into full octets
	print strBinSecond
	strBinThird = ("{0:b}".format(int(thirdOct))) #Binary as a string
	for a in range(8):
		if len(strBinThird) != 8:
			strBinThird = "0" + strBinThird	#turning strings into full octets
	print strBinThird
	
netmaskLength()