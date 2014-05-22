import os


#resets server before launching app
def server_reset():
    server = os.popen("ps -fA | grep python")
    for x in range(3):
        number = ""
        list = []
        read = server.readline()
        for y in range(6,11):
            list.append(read[y])
        number = number.join(list)
        os.system("kill %s"%(number))
