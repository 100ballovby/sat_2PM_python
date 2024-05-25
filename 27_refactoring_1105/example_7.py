# определим несколько функций
def get_account(social_security_number):
	pass


def withdraw_money(account_number):
	pass


def account_not_found():
	pass


account_number = get_account('123-456-789')
if account_number:
	withdraw_money(account_number)
else:
	account_not_found()


# Python-way
if account_number := get_account('123-456-789'):
	withdraw_money(account_number)
else:
	account_not_found()

