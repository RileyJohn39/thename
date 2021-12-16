PolicySum = 0
f = open("OSICDef.dat", "r")
PolicyNum = int(f.readline())
BasicPrem = float(f.readline())
DISCOUNT = float(f.readline())
ExtraCover = float(f.readline())
GlassCover = float(f.readline())
LoanerCover = float(f.readline())
HST = float(f.readline())
ProcessingFee = float(f.readline())
f.close()
#Starting inputs
while True:
    CustFirstName = input("Enter the customers 1st name: ")
    CustSecName = input("Enter 2nd Name: ")
    CustAddress = input("Enter address: ")
    City = input("Enter the city: ")
    Province = input("Enter the Province: ")
    Postal = input("Enter postal code: ")
    CustPhone = input("Enter phone Number: ")
    while True:
        try:
            CarAmount = int(input("Enter Number of insured cars: "))
        except:
            print('Invalid input!')
        else:
            if CarAmount >= 1:
                break
            else:
                print('Invalid input!')
    OptGlassCov = input("Would you Like optional Glass coverage? Y/N: ")
    while True:
        ExtraLiability = input("Would you like extra Liability up to $1,000,000? Y/N: ")
        ExtraLiability = ExtraLiability.upper()
        if ExtraLiability == 'Y' or ExtraLiability =='N':
            break
        else:
            print("Please Enter Y or N")
    while True:
        OptLoanerCar = input("Would you like optional loaner car? Y/N: ")
        OptLoanerCar = OptLoanerCar.upper()
        if OptLoanerCar == 'Y' or OptLoanerCar == 'N':
            break
        else:
            print("Please Enter Y/N")

#Calculations here
    if CarAmount == 1:
        InsPrem = BasicPrem
    if CarAmount > 1:
        InsPrem = BasicPrem + (((BasicPrem) * (CarAmount - 1)) * DISCOUNT)
    if ExtraLiability.upper() == 'Y':
        ExtraCharge1 = (CarAmount * ExtraCover)
    if OptGlassCov.upper() == 'Y':
        ExtraCharge2 = (CarAmount * GlassCover)
    if OptLoanerCar.upper() == 'Y':
        ExtraCharge3 = (CarAmount * LoanerCover)
    print(ExtraCharge1)
    print(InsPrem)
    print(ExtraCharge3)
    print(ExtraCharge2)
    totalextracharge = ExtraCharge1 + ExtraCharge2 + ExtraCharge3
    TotalPrem = InsPrem + totalextracharge
    TAX = TotalPrem * HST
    FinalTotalCost = TotalPrem + TAX
    MonthlyPayment = (FinalTotalCost + 39.99) // 12
#printing the results
    print("CUSTOMER DETAILS")
    print("LISTING")
    print()
    print("CUSTOMER      ADDRESS      CITY       PROVINCE     POSTAL    PHONE")
    print("  NAME                                                                 ")
    print("{:<11} {:<15} {:<9} {:<10} {:<7} {:<7}".format(CustFirstName, CustAddress, City, Province, Postal, CustPhone))

    print("ONE STOP INSURANCE COMPANY")
    print()
    print("TOTAL EXTRA      INSURANCE     TOTAL PREMIUM     TAX     TOTAL")
    print("   CHARGE         PREMIUM                                     ")
    print("="*15)
    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format(totalextracharge, InsPrem, TotalPrem, TAX, FinalTotalCost))
#appended to Policies.dat
    PolicySum = PolicySum + 1
    f = open("Policies.dat", "a")
    f.write(
        f"{PolicyNum}, {CustFirstName}, {CustAddress}, {City}, {Province}, {Postal}, {CustPhone}, "
        f"{ExtraLiability}, {OptGlassCov}, {OptLoanerCar}, {InsPrem}\n")
    f.close()
    print(" Policy was saved! ")
    print("="*50)
    print("ONE STOP INSURANCE COMPANY")
    print("POLICY LISTING AS OF dd-mon-yy")
    print()
    print("POLICY CUSTOMER                    INSURANCE      EXTRA      TOTAL PREMIUM")
    print("NUMBER NAME                         PREMIUM        COSTS                  ")
    print("="*50)
    print("{:<2} {:<30} {:<12} {:<12} {}".format(PolicyNum, CustFirstName, InsPrem, FinalTotalCost, TotalPrem))
#Report 1 Above^^ Report 2 Below vv
    print("="*50)
    print("ONE STOP INSURANCE COMPANY")
    print("MONTHLY PAYMENT LISTING AS OF mm-dd-yy")
    print()
    print("POLICY CUSTOMER                    TOTAL     HST     TOTAL     MONTHLY")
    print("NUMBER  NAME                        PREMIUM            COST      PAYMENT")
    print("{:<2} {:<30} {:<7} {:<7} {:<12} {}".format(PolicyNum, CustFirstName, TotalPrem, HST, FinalTotalCost, MonthlyPayment))
    print("="*50)
    print("TOTAL POLICIES: ")
    print("{:<18}".format(PolicySum))


    while True:
        ProgramCont = input("Would you like to continue the program? Y/N: ")
        ProgramCont = ProgramCont.upper()
        if ProgramCont != "Y" and ProgramCont != "N":
            print("Please press Y or N")
            continue
        elif ProgramCont == "N":
            PolicyNum += 1
            break
        elif ProgramCont == "Y":
            PolicyNum += 1
            break
    if ProgramCont == "Y":
        continue

#writing back to to OSICDef.dat
    f = open("OSICDef.dat", "w")
    f.write(f"{PolicyNum}\n")
    f.write(f"{BasicPrem:,.2f}\n")
    f.write(f"{DISCOUNT:,.2f}\n")
    f.write(f"{ExtraCover:,.2f}\n")
    f.write(f"{GlassCover:,.2f}\n")
    f.write(f"{LoanerCover:,.2f}\n")
    f.write(f"{HST:,.2f}\n")
    f.write(f"{ProcessingFee:,.2f}\n")
    f.close()