# This program calculates the gross pay for
# each of Megan's baristas.

# NUM_EMPLOYEES is used as a constant for the
# size of the list.
NUM_EMPLOYEES = int(input("Enter Amount of Employees : "))

def main():
    # Create a list to hold employee hours.
    hours = [0] * NUM_EMPLOYEES

    # Get each employee's hours worked.
    for index in range(NUM_EMPLOYEES):
        print("Enter the hours worked by employee ", index + 1, ": ", sep="", end="")
        hours[index] = float(input())

    # Get the hourly pay rate.
    pay_rate = float(input("Enter the hourly pay rate: "))

    # Display each employee's gross pay.
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(
              "Gross pay for employee ",
                index + 1,
                ": $", 
                format(gross_pay, ",.2f"),
                sep="",
            )
    maxh = max(hours)
    minh = min(hours)
    index = 1
    maxpay = []
    minpay = []
    print("employee ", end="")
    for i in range(NUM_EMPLOYEES):
        if hours[i] == maxh:
            maxpay.append(i + 1)
    grossmax = format(maxh * pay_rate, ",.2f")
    print(*maxpay, sep=",", end=" ")
    print(f"get(s) maxmimum gross pay ${grossmax}")

    print("employee ", end="")
    for i in range(NUM_EMPLOYEES):
        if hours[i] == minh:
            minpay.append(i + 1)
    grossmin = format(minh * pay_rate, ",.2f")
    print(*minpay, sep=",",  end=" ")
    print(f"get(s) minimum gross pay ${grossmin}")
# Call the main function.
main()