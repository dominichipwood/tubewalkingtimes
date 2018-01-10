import re

wt=open("walking_times.txt")  #wt=walking times
lines=wt.readlines()

station1=input("Walking time from ")
station2=input("to ")


def read(st):   #read number next to station. 
    for line in lines:
        if re.match(st,line):
            twodigits=re.search("[0-9][0-9]",line) #if 2 digit number or 1 digit?
            onedigit=re.search("[0-9]",line)
            if twodigits:   
                    return int(twodigits.group())
            elif onedigit:
                return int(onedigit.group())
            else:
                raise NameError

def fromBr(st): #time fomr brixton
    i=len(lines)-1
    time=read(st) #will miss this in while loop
    while not re.match(st,lines[i]):    #go though lines until get to station
        time=time+read(lines[i])
        i=i-1
    return time
                
        
print("The walking time betwee {} and {} is {} minutes".format(station1,station2,abs(fromBr(station1)-fromBr(station2)) ) )

wt.close()
