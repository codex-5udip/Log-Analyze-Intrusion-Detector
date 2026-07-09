success = 0
failed = 0
   
with open("auth.log.txt") as file:
    for line in file:
        if "Accepted" in line:

            part = line.split()   #split every line first
            success += 1
            username = part[8]
            ip = part[10]

            print("Successful Login")
            print("Username:",username)
            print("IP Address:",ip)

        if "Failed" in line:

            part = line.split()   #split every line first
            failed += 1
            username = part[8]
            ip = part[10]

            print("Failed Login")
            print("Username:" ,username)
            print("IP Address:" ,ip)

print("Total Successful Login:",success)
print("Total Failed Login:",failed)           