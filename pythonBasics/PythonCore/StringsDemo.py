str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str2 = "RahulShetty"

print(str[1])  #a

print(str[0:5])  #substring

print(str+str1)  #oncatination

print(str2 in str)  #substring check

var = str.split(".")
print(var)
print(var[0])

str3 = " great "
print(str3.strip()) #trims white spaces
print(str3.lstrip())
print(str3.rstrip())