# important points this queries are specific to sqlite like auto_increment is already there for id column
# once can map Foreign key with another table suing REFRENCES syntax
sql_for_departments_table = """
                                CREATE TABLE Departments (
                                    Id INT NOT NULL ,
                                    Name VARCHAR(25) NOT NULL,
                                    PRIMARY KEY(Id)
                                );
                                """
    
sql_for_employees_table = """
                            CREATE TABLE Employees (
                                Id INT NOT NULL ,
                                Fname VARCHAR(25) NOT NULL,
                                Lname VARCHAR(25) NOT NULL,
                                Phone VARCHAR(11),
                                ManagerId INT,
                                DepartmentId INT NOT NULL,
                                Salary INT NOT NULL,
                                HireDate DATETIME NOT NULL,
                                PRIMARY KEY(Id),
                                FOREIGN KEY(ManagerId) REFERENCES Employees(Id),
                                FOREIGN KEY(DepartmentId) REFERENCES Departments(Id)
                            );
                            """

sql_for_customers_table = """
                            CREATE TABLE CUSTOMERS (
                                Id INT NOT NULL,
                                Fname VARCHAR(25) NOT NULL,
                                Lname VARCHAR(25) NOT NULL,
                                Email VARCHAR(100) NOT NULL,
                                PhoneNumber VARCHAR(11),
                                PRIMARY KEY(Id)
                            );
                          """

sql_for_cars_table = """
                        CREATE TABLE CARS (
                            Id INT NOT NULL,
                            CustomerId INT NOT NULL,
                            EmployeeId INT NOT NULL,
                            Model VARCHAR(35) NOT NULL,
                            Status VARCHAR(35) NOT NULL,
                            TotalCost INT NOT NULL,
                            PRIMARY KEY(Id),
                            FOREIGN KEY(CustomerId) REFERENCES Customers(Id),
                            FOREIGN KEY(EmployeeId) REFERENCES Employees(id)
                        );
                     """