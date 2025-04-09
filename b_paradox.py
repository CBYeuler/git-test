import random
#Use a function to generate random dates
#x = how many people
def dates(x):
    """
    Generates a list of random birthdays for x people.
    Returns a list of strings in 'Month Day' format.
    
    """
    
    count = 0
    m_list = []
    month = [
            "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
        ]
    #used dict. to keep track of dates for the months
    month_days = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    #Generate random month and day for each person
    while count != x:
        
        pick = random.choice(month)
        num = random.randint(1, month_days[pick])
        m_list.append(pick + " " + str(num))
        count += 1
    return m_list

#wrap it in loop
#simulation parameters
def run_simulation():
    count = 0
    num_people = 23
    sim=1000
    for i in range(sim):

        birthdays = dates(num_people)
        #check for duplicates

        if len(birthdays) != len(set(birthdays)):
            count += 1
    #sim results
    print(f"Num of simulations run:{sim}|| Matches: {count}|| Percentage of Matches {(count/sim)*100:.2f}%")




if __name__ == "__main__":
    run_simulation()

