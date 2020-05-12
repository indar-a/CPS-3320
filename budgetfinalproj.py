#This budget program allows you to enter your income and expenses (however many you choose)
#to indicate whether you will have sufficent or insufficient funds after your total expenses 
#are deducted from your total income. It is a handy way to keep track of and stay accountable
#of your expenses and spending. It uses simple functions to allow the user to add sources of
#income & their amounts, expenses & their amounts, as many times as they'd like, and have their
#expense status be displayed. All of this is performed within the user's Command Prompt or Terminal 
#shell. 

import sys

#Define class and assign variables to hold key budget functions

class Application:
    def __init__(track):
        track.income = 0
        track.expenses = 0
        track.expenseAmount = []
        track.expenseType = []
        track.incomeType = []
        track.incomeAmount = []
        track.incomeTrack()

#Define a function to allow user to add multiple incomes (if necessary).

    def addIncome(track):
        addIncome = input('Would you like to add a source of income? [Select "y" if yes. Press any other key if no.]:')
        return addIncome

#Define a function to track total incomes (if more than one). 

    def incomeTotal(track):
        track.income = sum(track.incomeAmount)

#Define a function to allow user to add multiple incomes (if necessary).

    def newExpense(track):
        newExpense = input('Would you like to add an expense? [Select "y" if yes. Press any other key if no.]:')
        return newExpense

#Define a function to track total expenses (if more than one). 

    def expenseTotal(track):
        track.expenses = sum(track.expenseAmount)

#Define an error handling function in case user opts not to add 
#a source of income or expenses at all. The program will not execute 
#if it does not have any incomes of expenses to keep track of.

    def incomeError(track):
        if not track.incomeAmount:
            print('You must enter at least one source of income.')
            track.incomeTrack()
        
    def expenseError(track):
        if not track.expenseAmount:
            print('You must enter at least one expense.')
            track.expenseTrack()

#Define a function to allow the user to enter the dollar value
#amount and name of their income. This is accomplished using a 
#nested if else loop within a while loop, followed by initializing 
#a for loop to hold income data. 

    def incomeTrack(track):
        x = False
        while not x:
            result = track.addIncome()
            if result == 'y':
                incomeValue = int(input('Please enter the dollar value of your income [Round to Nearest Tenth]: '))
                track.incomeAmount.append(incomeValue)
                incomeType = input('Please enter the source of this income [Name of Company/Workplace]:')
                track.incomeType.append(incomeType)
            else:
                track.incomeError()
                x = True
        track.incomeTotal()
        name = [name for name in track.incomeType]
        income = [income for income in track.incomeAmount]
        incomeData = dict(zip(name, income))
        for i in incomeData:
            print(i + ': ', '$' + str(incomeData[i]))
        print('Total user income: ', '$' + str(track.income))
        track.expenseTrack()

#Define a function to allow the user to enter the dollar value
#amount and name of their expense. This is accomplished using a 
#nested if else loop within a while loop, followed by initializing 
#a for loop to hold expense data.

    def expenseTrack(track):
        x = False
        while not x:
            result = track.newExpense()
            if result == 'y':
                expenseValue = int(input('Enter expense amount. [Numbers Only]: '))
                track.expenseAmount.append(expenseValue)
                expenseType = input('Enter expense name. [Name Only]: ')
                track.expenseType.append(expenseType)
            else:
                track.expenseError()
                x = True
        track.expenseTotal()
        name = [name for name in track.expenseType]
        expense = [income for income in track.expenseAmount]
        expenseData = dict(zip(name, expense))
        for k in expenseData:
            print(k + ': ', '$' + str(expenseData[k]))
        print('Your expense total is: ', '$' + str(track.expenses))
        track.totalOutput()

#Define a function to compute whether the the user has a sufficient or
#insufficient amount of funds by subtracting their total expenses from
#their total income. Finally, it allows the user to repeat the process
#if desired and either resets the program to allow the user to do so without
#having to manually run it again, or close the program if the user does not
#desire to repeat. This is all accomplished using if/else statements.

    def totalOutput(track):
        totalOutput = track.income - track.expenses
        if totalOutput < 0:
            print('You have insufficient funds in the amount of ' + '$' + str(totalOutput) + ' start saving!')
        if totalOutput == 0:
            print('Your income and expenses are equal. Save more than you spend!')
        if totalOutput > 0:
            print('You have sufficient funds in the amount of ' + '$' + str(totalOutput) + ' keep up the good work and continue saving!')
        repeat = input('Would you like to compute your budget again? [y/n]: ')
        if repeat == 'y':
            track.resetRepeat()
        else:
            track.exitProcess()

#Define a function to reset the program and set all values to 0 again
#in case the user decides to repeat the process. This is accomplished
#by initilizing all variables to 0 and deleting any previously stored
#information for incomes and expenses.

    def resetRepeat(track):
        track.income = 0
        track.expenses = 0
        del track.expenseAmount[0:]
        del track.expenseType[0:]
        del track.incomeType[0:]
        del track.incomeAmount[0:]
        track.incomeTrack()

#Define a function to exit the program once the user has decided not to 
#repeat the process and is ready to exit the program). This is done using
#the sys.exit() function allowing the user to exit the program once
#indicating they desire to do so.

    def exitProcess(track):
        print('Process Completed.')
        sys.exit(0)

#This calls on the Application() class allowing the program to run.

if __name__ == '__main__':
    Application()