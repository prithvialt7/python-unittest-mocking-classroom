import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="datagrokr",
  database="employees",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        mycursor.execute("SELECT max(salary) from salaries")
        myresult = mycursor.fetchone()
        myresult = myresult[0]
        return myresult

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        mycursor.execute("SELECT min(salary) from salaries")
        myresult = mycursor.fetchone()
        myresult = myresult[0]
        return myresult



if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)