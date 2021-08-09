from src.bank_account import *

bank_account = BankAccount("John", 500, "business")

#print(bank_account.holder_name)
#print(bank_account.balance)
#print(bank_account.type)

personal_account = BankAccount("Jo", 350, "personal")

bank_account.pay_monthly_fee()
print(bank_account.balance)

personal_account.pay_monthly_fee()
print(personal_account.balance)








#bank_account.pay_in(50)

#print(bank_account.balance)

#bank_account.pay_monthly_fee(50)

#print(bank_account.balance)


#bank_account.holder_name = "Ada"
#print(bank_account.holder_name)




#account = {
#    "holder_name": "John",
#    "balance": 500,
#    "type": "business"
#}

#print(get_account_name(account))
