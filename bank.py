

def bankOper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updatedBal = totalBal - withdraw


    return totalBal, updatedBal


if_name_=="_main_":
    initialBal = int(sys.argv[1])
    deposit = int(sys.argv[2])
    withdraw = int(sys.argv[3])

    totalBal, updatedBal = bankOper(initial, depososit, withdraw)

    print("total balance:", totalBal)
    print("updated balance:", updatedBal)