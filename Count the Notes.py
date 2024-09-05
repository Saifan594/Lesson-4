print("\033c")

amount = int ( input ( "enter total amount: " ) )

note100 = amount // 100
note50 = (amount % 100) // 50
note10 = ((amount % 100) % 50) // 10

print ( f"notes of 100 taka {note100}" )
print ( f"notes of 50 taka {note50}" )
print ( f"notes of 10 taka {note10}" )