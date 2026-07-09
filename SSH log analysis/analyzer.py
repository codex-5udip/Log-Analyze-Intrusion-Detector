success = 0
failed = 0
invalid_user = 0

unique_ips = set()
unique_user = set()

attacking_ip = {}
target_users = {}
with open("auth.log.txt") as file:
    for line in file:

        if "Accepted" in line:

            part = line.split()
            success += 1

            username = part[8]
            ip = part[10]

            unique_user.add(username)
            unique_ips.add(ip)

            if username in target_users:
                target_users[username] += 1
            else:
                target_users[username] = 1

            if ip in attacking_ip:
                attacking_ip[ip] += 1
            else:
                attacking_ip[ip] = 1

        if "Failed" in line:

            part = line.split()
            failed += 1

            username = part[8]
            ip = part[10]

            unique_user.add(username)
            unique_ips.add(ip)

            if ip in attacking_ip:
                attacking_ip[ip] += 1
            else:
                attacking_ip[ip] = 1

            if username in target_users:
                target_users[username] += 1
            else:
                target_users[username] = 1

print("\n========== SSH LOG REPORT ==========\n")

print("Successful Logins :", success)
print("Failed Logins     :", failed)

print("\nUnique IP Addresses :", len(unique_ips))
print("\nTop Attacking IPs")

for ip, count in attacking_ip.items():
    print(ip, ":", count)

print("\n========== Most Targeted Usernames ==========")

for username, count in target_users.items():
    print(username, ":", count)
