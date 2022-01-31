


class house_rental_property:

    def __init__(self):
        self.income = None
        self.expense = None
        self.cashflow = None
        self.roi = None
        self.cost = None
        self.incomedict = {}
        self.expensedict = {}


    def integer_check(self,text):
        while True:
            answer = input(text)
            if answer.isdigit():
                return int(answer)
            else:
                print("Please input a number.")

    def yes_no(self,maybe):
        while True:
            yessir = input(maybe)
            if yessir == 'yes':
                return 'yes'
            elif yessir == 'no':
                return 'no'
            else:
                print("Please enter 'yes' or 'no'.")

    def meth_income(self):

        rent = self.integer_check("How many rooms does the property have? ")
        self.incomedict['Rooms'] = rent
        charge = self.integer_check("How much do you charge for each room in the house? ")
        self.incomedict['Charge'] = charge
        option = self.yes_no("Does the property have a pool or any outside water feautures ('yes'/'no')? ")
        if option == 'yes':
            option1 = self.yes_no("Do you pay for the maintenance on these feautures ('yes'/'no')? ")
            if option1 == 'yes':
                pool = self.integer_check("How much do you pay for maintenance monthly? ")
                self.incomedict['Maintenance'] = pool
            elif option1 == 'no':
                pool = 0
                self.incomedict['Maintenance'] = pool
        elif option == 'no':
            pool = 0
            self.incomedict['Maintenance'] = pool
        misc = self.integer_check("If there are any other renting fees please provide the amount here: ")
        self.incomedict['Misc'] = misc

        cost_per_room = rent * charge
        self.income = cost_per_room + misc + pool

        print(f"The total amount of your rental income is: ${self.income} ")

    def meth_expenses(self):
        tax = self.integer_check("How much do you pay in taxes monthly on the home? ")
        self.expensedict['Tax'] = tax
        mortgage = self.integer_check("How much do you pay for a mortgage? ")
        self.expensedict['Mortgage'] = mortgage
        insurance = self.integer_check("How much is the insurance monthly on the home? ")
        self.expensedict['Insurance'] = insurance
        vacancy = self.integer_check("How much do you put away a month incase of vacancy? ")
        self.expensedict['Vacancy'] = vacancy
        capex = self.integer_check("How much do you put aside for capital expenditures? ")
        self.expensedict['Capex'] = capex
        repairs = self.integer_check("What is the average price of repairs per month? ")
        self.expensedict['Repairs'] = repairs
        util = self.yes_no("Do you pay for the utilities ('yes'/'no')? ")
        if util.lower() == 'yes':
            util = self.integer_check("How much do you pay monthly for utilities? ")
            self.expensedict['Utilities'] = util
        elif util.lower() == 'no':
            util = 0
            self.expensedict['Utilities'] = util
        hoa = self.integer_check("How much do you pay in HOA (Enter '0' if you don't live in an HOA)? ")
        self.expensedict['HOA'] = hoa
        work = self.yes_no("Do you pay for lawn maintenance ('yes'/ 'no')? ")
        if work == 'yes':
            lawn = self.integer_check("How much do you pay for lawn maintenance? ")
            self.expensedict['Lawn'] = lawn
        elif work == 'no':
            lawn = 0
            self.expensedict['Lawn'] = lawn
        manag = self.integer_check("How much do you pay for property management? ") 
        self.expensedict['Management'] = manag


        self.expense = tax + mortgage + insurance + vacancy + capex + repairs + util + hoa + lawn + manag

        print(f"Your total monthly expense is : ${self.expense}")


    def flow(self):
        if self.expense == None:
            bighouse.return_on_investment
            return
        elif self.income == None:
            bighouse.return_on_investment
            return

        # Expenses
        tax = self.expensedict.get('Tax')
        mortgage = self.expensedict.get('Mortgage')
        insurance = self.expensedict.get('Insurance')
        vacancy = self.expensedict.get('Vacancy')
        capex = self.expensedict.get('Capex')
        repairs = self.expensedict.get('Repairs')
        utilities = self.expensedict.get('Utilities')
        hoa = self.expensedict.get('HOA')
        lawn = self.expensedict.get('Lawn')
        manag = self.expensedict.get('Management')
        self.expense = tax + mortgage + insurance + vacancy + capex + repairs + utilities + hoa + lawn + manag

        # Income
        rooms = self.incomedict.get('Rooms')
        charge = self.incomedict.get('Charge')
        misc = self.incomedict.get('Misc')
        main = self.incomedict.get('Maintenance')

        cost_per_room = rooms * charge
        self.income = cost_per_room + misc + main
        self.cashflow = self.income - self.expense

        print(f"Your totol cash flow is: ${self.cashflow}")

    def return_on_investment(self):
        if self.expense == None:
            print("Please finish the forms.")
            return
        elif self.income == None:
            print("Please finish the forms.")
            return
        self.cost = self.integer_check("How much was the total cost of the home? ")
        down = self.integer_check("How much was the down payment on the property? ")
        closing = self.cost * .05
        rehab = self.integer_check("How much did you pay for repairs on the home when first purchased? ")
        misc = self.integer_check("What is the amount of any other expenses when first purchasing the home? ")

        total_invest = down + closing + rehab + misc
        annual_cash = self.cashflow * 12 

        total = annual_cash/total_invest
        self.roi = total * 100
        print(f"Your total return is %{self.roi} ")

    def edit_bay(self):
        edit = input("What form did you want to edit? | 1)Expenses ('exp') | 2) Income ('income') | ")
        if edit == 'income':
            print("If you're done editing plese input: 'exit'")
            while True:
                for inc, come in self.incomedict.items():
                    print(inc,come)
                opt = input("What would you like to change? ")
                if opt.title() in self.incomedict:
                    del self.incomedict[opt.title()]
                    opt2 = self.integer_check("What would you like to change it to? ")
                    self.incomedict[opt.title()] = opt2
                elif opt == 'exit':
                    return
                else:
                    print("Option is not on form.")

        if edit == 'expenses':
            print("If you're done editing plese input: 'exit'")
            while True:
                for exp, ense in self.expensedict.items():
                    print(exp,ense)
                opt = input("What would you like to change? ")
                if opt.title() in self.expensedict:
                    del self.expensedict[opt.title()]
                    opt2 = self.integer_check("What would you like to change it to? ")
                    self.expensedict[opt.title()] = opt2
                elif opt == 'exit':
                    return
                else:
                    print("Option is not on form.")

    def run(self):
        
        while True:
        
            print("You must complete both forms before your return is to be processed. (Type 'done' when all forms are filled out) ")
            print("If you want to edit any past information enter 'edit'.")
            response = input("Which part of the form did you want to fill out? | 1)Expenses ('exp') | 2) Income ('income') |  ")
            if response == 'exp':
                bighouse.meth_expenses()
            elif response == 'income':
                bighouse.meth_income()
            elif response == 'done':
                bighouse.flow()
                bighouse.return_on_investment()
            elif response == 'edit':
                bighouse.edit_bay()    
            else:
                print("That is not an option.")

        

bighouse = house_rental_property()
print(bighouse.run())
