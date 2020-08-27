def celcius2far(t):
    s = 32 + (t * 1.8)
    return s

t = float(input("Enter temperature in degree celcius:"))
if t < -273.15:
    print ("temperature too low to be true")
else:
    print("Temperature in Farhenheit is: ")
    print(celcius2far(t))
    print("\n\n")

temp=list()
temperatures=[10,-20,-289,100]
for i in temperatures:
    if i < -273.15:
        print ("temperature doesn't make sense")
        temp.append("temp doesn't make sense")
    else:
        print(celcius2far(i))
        temp.append(celcius2far(i))

file=open("far.txt",'a')
for i in range(len(temp)):
    file.write("%s\n" % temp[i])
file.close()

    
    






