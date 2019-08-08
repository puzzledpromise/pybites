class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager

    def __enter__(self):
        self.__account = Account()
        self.__account._transactions = self._transactions[:]
        return self.__account

    def __exit__(self, *args):
        if self.__account.balance >= 0:
            self._transactions = self.__account._transactions[:]
        self.__account = None


