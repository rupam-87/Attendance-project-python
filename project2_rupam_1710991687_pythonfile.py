
import pandas as pd
 # reading the dataset
df=pd.read_csv('AttendancePercentageWiseReport.csv')
print(df.head())

 #remove the spaces from columns
s=lambda x: x.strip()

df = df.rename(columns=s)

for i in df.columns[4:]:
 # remove the spaces from the values of a columnn
        df[i] = df[i].str.strip()
        df[i] = df[i].replace('---','0')
for i in df.columns[4:]:
# converting the string to integer
    df[i] = pd.to_numeric(df[i])

#Selecting student that have attendance less than 75 in atleast in one subject for theory and practical seperatly

theory_detail = df[(df['AML3201'] < 75) | (df['CSL2301'] < 75) | (df['CSL3307'] < 75) | (df['CSL4207'] < 75) |
            (df['CSL4208'] < 75) | (df['CSL4305'] < 75) | (df['CSL4318'] < 75) | (df['CSL4336'] < 75) | (df['CSL5210'] < 75) | (df['CSP2301'] < 75) |
            (df['ECL3311'] < 75) | (df['GEW1601'] < 75) | (df['GEW1603'] < 75) | (df['GEW1604'] < 75) | (df['GEW1605'] < 75) | (df['GEW1607'] < 75) | (df['GEW1608']
               < 75) | (df['GEW1609'] < 75) | (df['GEW1610'] < 75) | (df['GEW1611'] < 75) | (df['GEW1613'] < 75)]
practical_detail = df[(df['AMP1201'] < 75) | (df['CSP1307'] < 75) | (df['CSP2210'] < 75) | (df['ECP1311'] < 75)]

#make csv file for theory and practicle seperatly

theory_detail.to_csv('Make_Up_List1.csv')
print(theory_detail)
practical_detail.to_csv('Make_Up_List2.csv')
print(practical_detail)

#student having attendance greater than 75

for i in df.columns[4:]:
   left_student=df[df[i]>=75.00]
#make csv file attendance ok for student having attendance greater than 75
left_student.to_csv('Attendance_OK.csv')
print(left_student.head())
