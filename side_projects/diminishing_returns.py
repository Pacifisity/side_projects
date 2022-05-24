amount_1 = int(input("Amount 1:\n"))
amount_2 = int(input("Amount 2:\n"))

upgrade_1 = 1 / ( ( 1 + ( 1 / amount_1 ) ) ** amount_2 )
upgrade_2 = 1 * ( ( 1 + ( 1 / upgrade_1 ) ) ** 10 )

print(upgrade_1, upgrade_2)
output = 1 / ( ( 1 + ( 1 * upgrade_1 ) ) ** upgrade_2 )
print(output)