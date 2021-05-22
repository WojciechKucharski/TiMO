from datetime import datetime, date


def printError(e):  # saving error message to file
    try:
        dateC = "Data\\CrashLog\\" + date.today().strftime("%d_%m_%Y") + ".txt"  # current date
        now = datetime.now().strftime("%H_%M_%S") + str(e) + "\n"  # current time + error message
        with open(dateC, "a") as myfile:
            myfile.write(now)
        myfile.close()  # close file
    except Exception as e:
        print(e)
