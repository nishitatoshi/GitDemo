values = [1, 2, "rahul", 4, 5]

# list is a datatype that allows multiple values and can be of different datatypes
print(values[0])  #1
print(values[3])  #4
print(values[-1])  #prints last value
print(values[1:3]) #prints from index 1 to 3-1

values.insert(3,"shetty") #insert
print(values)
values.append("End") #append-adds at the end
print(values)
values[2]="RAHUL" #updating
print(values)
del values[0]
print(values)


#Tuple-same as List but immutable
val = (1, 2, "rahul", 4.5)
print(val)

#Dictionay- key:value pair

dic = {"a":2, 4:"bcd", "c":"hello world"}
print(dic)
print(dic["c"])

dict = {}
dict["firstname"] = "Nishita"
dict["lastname"] = "Toshi"
dict["gender"] = "female"
print(dict)
print(dict["firstname"])

