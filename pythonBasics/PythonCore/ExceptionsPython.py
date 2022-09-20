ItemsInCart = 0

if ItemsInCart != 2:
    pass
    #raise Exception("Products cart count not matching")

assert(ItemsInCart == 0)

#try catch
#finally block executes everytime even if try fails

try:
    with open('filelog.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")