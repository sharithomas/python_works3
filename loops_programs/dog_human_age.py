# Write a Python program to calculate a dog's age in dog's years. Go to the editor
#Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

human_year=int(input("input dog's age in human years"))
dog_year=0

for i in range(1,human_year+1):
    if i==1 or i==2:
        dog_year=dog_year+10.5
    else:
        dog_year=dog_year+4

print("dog's age in dog's year=", dog_year)         
