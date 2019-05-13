def find_new_salary(current_salary,job_level):
    # write your logic here
    if(job_level==3):
        current_salary=current_salary*(15/100)+current_salary
        new_salary=current_salary
        print(new_salary)
    elif(job_level==4):
        current_salary=current_salary*(7/100)+current_salary
        new_salary=current_salary
        print(new_salary)
    elif(job_level==5):
        current_salary=current_salary*(5/100)+current_salary
        new_salary=current_salary
        print(new_salary)
    else:
        new_salary=current_salary
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(10000,3)
print(new_salary)
