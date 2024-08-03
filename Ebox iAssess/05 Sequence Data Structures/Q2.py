# Airline Client Details
# Airport check-in uses service counters found at commercial airports handling commercial air travel. The check-in is normally handled by an airline itself or a handling agent working on behalf of an airline. At the time of check-in, one of the Agent's primary duties is to check for client details, tickets, passports, visas, letters of consent, etc. Client details are stored in a Dictionary.

# The passport number is the key and client details are the value. Write a  program to get the value( Client details ) by giving the key (passport number) from the dictionary.

# Input and Output Format:
# Refer to sample input and output for formatting specifications.
# print “Client not found” if search not found. else print the details as in the mentioned format below.

# Note: All text in bold corresponds to the input and the rest corresponds to output.

# Sample Input and Output 1:
# Enter the number of clients
# 2
# Enter the details of the client 1
# Shri
# shri@mail.com
# 7346218
# Enter the details of the client 2
# Veena
# veena@mail.com
# 8639124
# Enter the passport number of the client to be searched
# 7346218
# Client Details
# Shri--shri@mail.com--7346218

# Sample Input and Output 2:
# Enter the number of clients
# 2
# Enter the details of the client 1
# Shri
# shri@mail.com
# 7346218
# Enter the details of the client 2
# Veena
# veena@mail.com
# 8639124
# Enter the passport number of the client to be searched
# 2346718
# Client not found

clients = int(input("Enter the number of clients\n"))
d = {}

for client in range(clients):
    print(f"Enter the details of the client {client+1}")
    name = input()
    email = input()
    pnum = int(input())
    d[pnum] = (name, email, pnum)

searchpnum = int(input("Enter the passport number of the client to be searched\n"))

if searchpnum in d:
    details = d[searchpnum]
    print(f"Client Details\n{details[0]}--{details[1]}--{details[2]}")
else:
    print("Client not found")