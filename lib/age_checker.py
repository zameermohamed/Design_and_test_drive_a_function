import datetime
# import dateutil
import math 

def age_checker(dob:str):
    check_list = dob.split("-")
    if len(check_list[0]) == 4:
        if int(check_list[1]) < 13:
            if int(check_list[2]) < 32:

                formatted_dob = datetime.datetime.strptime(dob,"%Y-%m-%d")
                current_date = datetime.datetime.now()
                age = current_date - formatted_dob
                age_in_days = age.days
                age_in_years = math.floor(age_in_days/365)
                if age_in_years >= 16:
                    return "Access granted!"
                elif age_in_years < 0:
                    raise Exception("Date of birth is in the future!")
                else: 
                    return f"Access denied. Your current age is {age_in_years} and required age is 16."

    raise Exception("Incorrect date of birth format")