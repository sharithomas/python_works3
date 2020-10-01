# Write a Python program to write a list to a file

city_list=['bangalore','delhi','kochi','mumbai','hydrabad']
f1=open('city.txt','w')
for city in city_list:
    f1.write(city)
f2=open('city.txt','r')
print(f2.read())
f1.close()
f2.close()
