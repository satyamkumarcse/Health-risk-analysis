
n = int(input("input the number of people you want to prepare health report on: "))
high_risk_people = 0
medium_risk_people = 0
low_risk_people = 0
i = 0
while i<n:
   

    i +=1
    w = int(input(f"user {i} enter your weight in (kgs): "))
    h = float(input(f"user {i} enter your height in metres: "))

    bmi = (w)/(h**2)
    if 0<bmi<18.5:
        print(f"bmi of user {i} is {bmi} : (underweight): ")
    elif 18.5 <=bmi<=24.9:
        print(f"bmi of user {i} is {bmi} : (normal weight)")
    else:
        print(f"user {i} has bmi {bmi} : overweight ")


    systolic  = float(input(f"user {i} enter your measured blood pressure systolic value: "))
    diastolic  = float(input(f"user {i} enter your measured blood pressure diastolic value: "))


    if 0<systolic<90 and 0<diastolic<60:
        print(f"user {i} has low bp")
    elif 90<systolic<120 and 60<diastolic<80:
        print(f"user {i} has normal bp")
    else:
        print("systolic/diastolic of user is high")



    hr = int(input(f" user {i} enter your resting heart rate in bpm: "))
    
    if 0<hr<60:
        print(f"user {i} has low resting heart rate : {hr}")
    elif 60<hr<100:
        print(f"user {i} has a normal resting heart rate : {hr}")
    else:
        print(f"user {i} has a very high resting heart rate")



    

    if hr<60 or hr>100:
     print(f"user {i} heart rate is not in healthy range")
    else:
        print('heart rate in healthy range')


    if systolic<90 or diastolic<60 or systolic>120 or diastolic>80:
        print(f"user {i} blood pressure is not in healthy range")
    else:
        print("bp is in healthy range")

    health_risk= 0
    if (bmi<18.5 or bmi>24.9) and (hr<60 or hr>100) and (systolic<90 or diastolic<60 or systolic>120 or diastolic>80):
        health_risk += 3
        print(f"user {i} has very high health risk") 
    elif (bmi<18.5 or bmi>24.9) and (hr<60 or hr>100):
        print(f"user {i} has very high health risk") 
        health_risk += 2

    elif (hr<60 or hr>100) and (systolic<90 or diastolic<60 or systolic>120 or diastolic>80) :
        print(f"user {i} has very high health risk") 
        health_risk += 2
    elif (systolic<90 or diastolic<60 or systolic>120 or diastolic>80) and  (bmi<18.5 or bmi>24.9):
        print(f"user {i} has very high health risk")
        health_risk += 2 
    elif (bmi<18.5 or bmi>24.9):
        print(f"user {i} has medium level health risk")
        health_risk += 1
    elif (hr<60 or hr>100):
        print(f"user {i} has medium level health risk")
        health_risk += 1
    elif (systolic<90 or diastolic<60 or systolic>120 or diastolic>80):
        print(f"user {i} has medium level health risk")
        health_risk += 1
    else:
        print(f"user {i} has low health risk")
        health_risk += 0

    if health_risk==3 or health_risk==2:
        high_risk_people=high_risk_people+1
    elif health_risk==1:
        medium_risk_people=medium_risk_people+1
    elif health_risk==0:
        low_risk_people=low_risk_people+1
    print()

print("-----summary-----")
print(f"number of people with high health risk is: {high_risk_people}")
print(f"number of people with medium health risk is: {medium_risk_people}")
print(f"number of people with low health risk is: {low_risk_people}")


# for i in range(1,10):
#     print(i,end="")

# for j in range(1,10):
#     print("hi")

# print(i)
        





        



