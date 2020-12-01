from .expense_regulator import expenseRegulator

if __name__ == '__main__':
    test = [1078,
            900,
            1702,
            318,
            1100,
            1541,
            20,
            10,
            10]
    e = expenseRegulator()
    n = 3
    e.resolve_accounts_recursive(n)

