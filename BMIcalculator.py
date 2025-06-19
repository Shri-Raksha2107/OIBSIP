#BMI Calaculator-This allows you to check your BMI by entering your height and weight.
def BMI_calculator():
    # Ask user to choose the measurement system
    metric_=input("Want to use metric or imperial system?(metric/imperial): ")
    meteric_lower=metric_.lower()# Convert user input to lowercase for case-insensitive comparison
    # If user selects Metric system
    if meteric_lower=="metric":
        height=float(input("Enter your height in meters(m): "))
        weight=float(input("Enter your weight in kilograms(kg): "))
        if height>0 and weight>0: # Check for valid positive height and weight
            BMI=weight/(height*height)
            print("Your BMI is: ",BMI)
            # Categorize BMI value based on standard BMI ranges
            if BMI<=18.5:
                print("You are Underweight.")
            elif BMI>18.5 and BMI<=24.9:
                print("You are Normal Weight.")
            elif BMI>=25 and BMI<=29.9:
                print("You are Overweight.")
            else:
                print("You are Obese.")
        else: # Print error message if height or weight is invalid
            print("Invalid input. Please Re-check your inputs.")
    # If user selects Imperial system
    elif meteric_lower=="imperial":
        height=float(input("Enter your height in inches(in): "))
        weight=float(input("Enter your weight in pounds(lb): "))
        if height>0 and weight>0: # Check for valid positive height and weight
            bmi=(weight/(height*height))*703
            print("Your BMI is: ",bmi)
            # Categorize BMI value based on standard BMI ranges
            if bmi<=18.5:
                print("You are Underweight.")
            elif bmi>18.5 and bmi<=24.9:
                print("You are Normal Weight.")
            elif bmi>=25 and bmi<=29.9:
                print("You are Overweight.")
            else:
                print("You are Obese.")
        else: # Print error message if height or weight is invalid
            print("Invalid input. Please Re-check your inputs.")
    # If user enters something other than 'metric' or 'imperial'
    else:
        print("Incorrect system, Please check your input.")
if __name__=="__main__":
    BMI_calculator() #This calls our main function 'BMI_calculator'.
        



