#3. Write a Python script to concatenate following dictionaries to create a new one.
#dic1={1:10, 2:20}, dic2={3:30, 4:40}, dic3={5:50,6:60}, Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
result_dict={}
for d in (dic1,dic2,dic3):
    result_dict.update(d)
print("resultant dictionary",result_dict)
