import pandas as pd
import csv

df=pd.read_csv(r"C:\Users\mayank\Desktop\play_tennis.csv")
print("give the outlook:")
a=input()
print("give the humidity:")
b=input()
print("give the wind:")
c=input()
#print(df)
df4 = df['Play']
df3 = df['Wind']
df2 = df['Humidity']
df1 = df['Outlook']
count_yes=0
length = len(df4)
for i in df4:
	if i=="Yes":
		count_yes+=1
count_no=length-count_yes
prob_yes = count_yes/len(df4)
print(prob_yes)
prob_no = 1-prob_yes
print(prob_no)
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0

for i in range(0,length):
    
    if (df1[i] == a and  df4[i] == "Yes"):
        
        count_1+=1
    elif (df1[i] == a and  df4[i] == "No"):
        count_4+=1
print(count_1)	
print(count_4)
for i in range(0,length):
    
    if (df2[i] == b and  df4[i] == "Yes"):
        
        count_2+=1
    elif (df2[i] == b and  df4[i] == "No"):
        count_5+=1
print(count_2)
print(count_5)
for i in range(0,length):
    
    if (df3[i] == c and  df4[i] == "Yes"):
        
        count_3+=1
    elif (df3[i] == c and  df4[i] == "No"):
        count_6+=1
        
print(count_3)	
print(count_6)

prob_yes_input=prob_yes*(count_1/count_yes)*(count_2/count_yes)*(count_3/count_yes)

prob_no_input=prob_no*(count_4/count_no)*(count_5/count_no)*(count_6/count_no)

probability=prob_no/(prob_no+prob_yes)
if (probability < 0.49):
    print("Play=NO")
    print(probability)
else:
    print("Play=Yes")
    print(probability)
