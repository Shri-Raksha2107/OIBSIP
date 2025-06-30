#BMI Calaculator-This allows you to check your BMI by entering your height and weight.
def BMI_calculator():
    metric_=input("Want to use metric or imperial system?(metric/imperial): ")
    metric_lower=metric_.lower()
    if metric_lower=="metric":
        height=float(input("Enter your height in meters(m): "))
        weight=float(input("Enter your weight in kilograms(kg): "))
        if height>0 and weight>0: 
            BMI=weight/(height*height)
            print("Your BMI is: ",BMI)
            if BMI<=18.5:
                print("You are Underweight.")
            elif 18.5 < BMI <= 24.9:
                print("You are Normal Weight.")
            elif 25<=BMI<=29.9:
                print("You are Overweight.")
            else:
                print("You are Obese.")
        else: 
            print("Invalid input. Please Re-check your inputs.")
    elif metric_lower=="imperial":
        height=float(input("Enter your height in inches(in): "))
        weight=float(input("Enter your weight in pounds(lb): "))
        if height>0 and weight>0: 
            bmi=(weight/(height*height))*703
            print("Your BMI is: ",bmi)
            if bmi<=18.5:
                print("You are Underweight.")
            elif 18.5 < BMI <= 24.9:
                print("You are Normal Weight.")
            elif 25<=BMI<=29.9:
                print("You are Overweight.")
            else:
                print("You are Obese.")
        else: 
            print("Invalid input. Please Re-check your inputs.")
    else:
        print("Incorrect system, Please check your input.")
if __name__=="__main__":
    BMI_calculator() 
        



