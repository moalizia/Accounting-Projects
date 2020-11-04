print("Program created by Mohammed Ali Zia")
print("Last updated 09/17/2020")

program_run = 0
while program_run == 0:
    import math
    import cmath

    def sep():
        print("_____________________________________________________________")


    def TOTAL(cost):
        SUM = sum(cost)
        print("Your total bill is $" + str(SUM))


    def DISPLAY(cost, location, date):
        cost_init = 0
        for u in range(len(cost)):
            print("You spent $" + str(cost[u]) + " at " + location[u] + " on " + str(date[u]) + " of this month")
            cost_init = cost_init + cost[u]
            print(cost_init)


    T = "Target"
    J = "Jewel Osco"
    M = "Mariano's"
    S = "Shell"
    DD = "Dunkin Donuts"
    Sev = "Seven-Eleven"
    GN = "Ghareeb Nawaaz"
    Sub = "Subway"
    TB = "Taco Bell"
    MD = "McDonald's"
    FC = "Farm City Supermarket"

    ### Edit only the cost, date and location lists!!!
    ## Example:
    # For August
    # cost = [5, 6, 7]
    # date = [1, 2, 4]
    # location = [T, J, M]
    ## This means you spent $5 on the 1st of August at Target, $6 on the 2nd of August at Jewel Osco and $7 on the 4th of August at Mariano's


    # ______________________________________________________________________________________________________________________________________________________________________________________________________________________________

    ############################################
    def August_2020(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def September_2020(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)

    def October_2020(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)

    def November_2020(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def December_2020(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def January_2021(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def February_2021(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def March_2021(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def April_2021(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def May_2021(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def June_2021(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)


    def July_2021(action):
        cost = [0]
        date = ["NULL"]
        location = ["NULL"]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)

    def August_2021(action):
        cost = [32.52, 33.54, 3.48, 4.09, 25.96, 7.3, 7.02, 1.27, 18.8, 22.45, 13.46, 6.52, 20.17, 12.86, 2.25, 8.75,
                22.96,
                6.52, 1.5, 2.21, 1.11, 32.97, 2.09, 5.07]
        date = [3, 3, 5, 5, 5, 6, 10, 12, 12, 12, 12, 13, 13, 14, 17, 17, 17,
                17, 17, 19, 24, 24, 27, 31]
        location = [T, S, DD, J, T, GN, Sub, DD, T, J, M, Sub, "BP Global", TB, Sev, "Ferros", "Metro Spice Mart",
                    T, Sev, S, MD, J, MD, TB]

        if (len(cost) == len(date)) and (len(cost) == len(location)) and (len(location) == len(date)):
            print("All values are correctly placed.")
        else:
            print("Error! Some of the amounts or labels are missing or incorrectly added")

        if action == "total":
            TOTAL(cost)
        elif action == "display":
            DISPLAY(cost, location, date)
        elif action == "both":
            TOTAL(cost)
            DISPLAY(cost, location, date)

    #####0000000000000000000000000000000000000000000000#####
    # ______________________________________________________________________________________________________________________________________________________________________________________________________________________________

    print("Hint: Unique intials for months Feb, Sep, Oct, Nov, Dec")

    Months_jan = ["Jan", "January", "jan", "january", "JAN", "JANUARY"]
    Months_feb = ["Feb", "February", "feb", "february", "f", "F", "FEB", "FEBRUARY"]
    Months_mar = ["Mar", "mar", "March", "march", "MAR", "MARCH"]
    Months_apr = ["Apr", "apr", "april", "April", "APRIL", "APR"]
    Months_may = ["May", "may", "MAY"]
    Months_jun = ["Jun", "jun", "June", "june", "JUN", "JUNE"]
    Months_jul = ["Jul", "jul", "July", "july", "JULY", "JUL"]
    Months_aug = ["Aug", "aug", "August", "august", "AUG", "AUGUST"]
    Months_sep = ["Sep", "Sept", "sep", "sept", "september", "September", "S", "s", "SEPT", "SEP", "SEPTEMBER"]
    Months_oct = ["Oct", "oct", "October", "october", "oc", "Oc", "o", "O", "OCT", "OC", "OCTOBER"]
    Months_nov = ["Nov", "nov", "November", "november", "n", "N", "NOV", "NOVEMBER"]
    Months_dec = ["Dec", "dec", "December", "december", "d", "D", "DEC", "DECEMBER"]
    Years = ["2020", "20", "2021", "21"]
    Year20 = ["2020", "20"]
    Year21 = ["2021", "21"]
    ans_BT = ["bt", "BT", "Bill Total", "bill total", "total", "Total", "TOTAL", "ttl", "TTL"]
    ans_BD = ["bd", "BD", "Bill Display", "bill display", "display", "Display", "DISPLAY", "dsp", "DSP"]
    ans_both = ["both", "BOTH", "b", "B", "Both"]
    Valid_Months = []
    Valid_Months.extend(Months_jan)
    Valid_Months.extend(Months_feb)
    Valid_Months.extend(Months_mar)
    Valid_Months.extend(Months_apr)
    Valid_Months.extend(Months_may)
    Valid_Months.extend(Months_jun)
    Valid_Months.extend(Months_jul)
    Valid_Months.extend(Months_aug)
    Valid_Months.extend(Months_sep)
    Valid_Months.extend(Months_oct)
    Valid_Months.extend(Months_nov)
    Valid_Months.extend(Months_dec)

    CM_check = 0
    CY_check = 0
    CA_check = 0

    while CM_check == 0:
        choice_month = input("Month?")
        if choice_month in Valid_Months:
            CM_check = 1
        else:
            CM_check = 0
            print("That is not a valid month or data for the month doesn't exist!")

    while CY_check == 0:
        choice_year = input("Year?")
        if choice_year in Years:
            CY_check = 1
        else:
            CY_check = 0
            print("That is not a valid year!")

    while CA_check == 0:
        choice_action = input("What action do you want to perform? Bill Total(BT) or Bill Display?(BD) or both?(B)")
        if (choice_action in ans_BT) or (choice_action in ans_BD) or (choice_action in ans_both):
            CA_check = 1
        else:
            CA_check = 0
            print("That is not a valid action!")

    if choice_action in ans_BT:
        action = "total"
    elif choice_action in ans_BD:
        action = "display"
    elif choice_action in ans_both:
        action = "both"

    ############################################
    if (choice_month in Months_aug) and (choice_year in Year20):
        August_2020(action)
    elif (choice_month in Months_sep) and (choice_year in Year20):
        September_2020(action)
    elif (choice_month in Months_oct) and (choice_year in Year20):
        October_2020(action)
    elif (choice_month in Months_nov) and (choice_year in Year20):
        November_2020(action)
    elif (choice_month in Months_dec) and (choice_year in Year20):
        December_2020(action)
    elif (choice_month in Months_jan) and (choice_year in Year21):
        January_2021(action)
    elif (choice_month in Months_feb) and (choice_year in Year21):
        February_2021(action)
    elif (choice_month in Months_mar) and (choice_year in Year21):
        March_2021(action)
    elif (choice_month in Months_apr) and (choice_year in Year21):
        April_2021(action)
    elif (choice_month in Months_may) and (choice_year in Year21):
        May_2021(action)
    elif (choice_month in Months_jun) and (choice_year in Year21):
        June_2021(action)
    elif (choice_month in Months_jul) and (choice_year in Year21):
        July_2021(action)
    #####0000000000000000000000000000000000000000000000#####

    # ______________________________________________________________________________________________________________________________________________________________________________________________________________________________

    sep()
    sep()
    sep()
    Pos_vals = ["Yes", "Y", "y", "yes"]
    Neg_vals = ["No", "N", "n", "no"]
    continue_run = 0
    while continue_run == 0:
        run_input = input("Do you want to continue? (Type 'yes' or 'no')")
        if run_input in Pos_vals:
            program_run = 0
            continue_run = 1
        elif run_input in Neg_vals:
            program_run = 1
            continue_run = 1
        else:
            program_run = 0
            continue_run = 0
            print("Please type a valid response!")