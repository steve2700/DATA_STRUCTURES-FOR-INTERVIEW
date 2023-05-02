class usernameGenerator:
    def __init__(self,first_name, last_name,campus,cohort_year):
        self.first_name = first_name
        self.last_name = last_name
        self.campus = campus
        self.cohort_year = cohort_year
    
    def isvalid_campus(self):
        """checking whether the campus you select is true and valid"""
        valid_campuses = ['JHB', 'CPT', 'DBN', 'PHO']
        return self.campus.upper() in valid_campuses
    
    def generateUsername(self):
        if not self.isvalid_campus():
            return None
        first_name = self.first_name.lower()
        last_name = self.last_name.lower()

        """checking whether there is a digit in the firstname or last_name"""
        if any(char.isdigit() for char in first_name) or any(char.isdigit() for char in last_name):
            return None
    
        if len(first_name) < 3:
            first_name += 'o' * (3-len(first_name))
        if len(last_name) < 3:
            last_name += 'o' * (3-len(last_name))
        return first_name[-3:] + last_name[-3:] + str(self.cohort_year)
    

if __name__ == '__main__':
    first_name = input("Please input your FirstName:")
    last_name = input("Please input your lastName: ")
    campus = input("Please Enter the campus you will be attending(JHB,DBN,CPT,PTO): ")
    cohort_year = 2023
    user = usernameGenerator(first_name,last_name,campus,cohort_year)
    username = user.generateUsername()
    if username is None:
        print("Invalid input, please check your input and try again")

    else:
        print("Your username is:" + username)
