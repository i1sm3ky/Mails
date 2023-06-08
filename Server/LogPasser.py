def WriteLog(LogItem):
    with open("Config/TempLog.txt", "a") as TempLog:
        TempLog.write(LogItem+'\n')
