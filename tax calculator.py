# Name: Olatunde Samson
# Matric No: BU24SEN1008
# Department: SOFTWARE ENGINEERING
# Personal Income Tax Calculator for 2009 U.S. Federal Tax Rates

print("TAX COLLECTOR:")
print("Filing Status:")
print("0 - Single filer")
print("1 - Married filing jointly or qualified widow(er)")
print("2 - Married filing separately")
print("3 - Head of household")

# user inputs
status = int(input("Enter your filing status (0-3): "))
income = float(input("Enter your taxable income: "))

# Tax brackets for 2009: list of (upper_limit, rate) for each filing status
brackets = [
    # 0: Single
    [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],
    
    # 1: Married Filing Jointly
    [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)],
    
    # 2: Married Filing Separately
    [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)],
    
    # 3: Head of Household
    [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]
]

# confirm status
if status < 0 or status > 3:
    print("Invalid filing status entered.")
else:
    tax = 0.0
    prev_limit = 0.0
    selected_brackets = brackets[status]
    
    for upper, rate in selected_brackets:
        if income <= prev_limit:
            break
        if income < upper:
            tax += (income - prev_limit) * rate
            break
        else:
            tax += (upper - prev_limit) * rate
            prev_limit = upper
    else:
        # For the highest bracket (inf)
        tax += (income - prev_limit) * rate
    
    print(f"Your income tax is: ${tax:.2f}")