newphase="rainstorm"
   #012345678
   #1,2,3,4,5,6,7,8,9 -- college board version 
#Create a new variable callled shortphrase
#and assign it a value by slicing 
# #the newphase varablie by removing 
# the first 3 characters
# and the last 3 characters
# the first three chracters are "rai"
# the last three characters are "orm"
# substring(string,start,end)
shortphrase=newphase[3:len(newphase)-3]
#college board version [4:len(newpharse)-6]
print(shortphrase)
#explain len(newphase)-3=9-3=6
#why does it end with 6?
#because the last index is not included  