ip =input("Enter an IPv4 address: ")
parts =ip.split(".")
if len(parts) != 4:
    print("invalid IP")
else:
     valid = True
     for part in parts:
         if not part.isdigit():
             valid = False
             break
         

         num =int(part)
     
         if num <0 or num > 255:
             valid = False
             break
         if valid:
             print("Valid IPv4 address")
         else:
             print("Invalid IP address")
