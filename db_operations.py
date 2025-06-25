from db_connection import create_connection, execute_query


def create_account(account_number, balance, pin, account_type, interest_rate=0, overdraft_limit=0):
    connection = create_connection("localhost", "root", "Root@123", "banking_accounts")
    insert_account_query = """
    INSERT INTO accounts (account_number, balance, pin, account_type, interest_rate, overdraft_limit)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    data = (account_number, balance, pin, account_type, interest_rate, overdraft_limit)
    execute_query(connection, insert_account_query, data)


def get_account(account_number):
    connection = create_connection("localhost", "root", "Root@123", "banking_accounts")
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
    account = cursor.fetchone()
    cursor.close()
    connection.close()
    return account


def update_account_balance(account_number, new_balance):
    connection = create_connection("localhost", "root", "Root@123", "banking_accounts")
    update_balance_query = "UPDATE accounts SET balance = %s WHERE account_number = %s"
    execute_query(connection, update_balance_query, (new_balance, account_number))


def change_pin(account_number, new_pin):
    connection = create_connection("localhost", "root", "Root@123", "banking_accounts")
    change_pin_query = "UPDATE accounts SET pin = %s WHERE account_number = %s"
    execute_query(connection, change_pin_query, (new_pin, account_number))


def transfer_funds(from_account_number, to_account_number, amount):
    from_account = get_account(from_account_number)
    to_account = get_account(to_account_number)

    if from_account and to_account and from_account['balance'] >= amount:
        update_account_balance(from_account_number, from_account['balance'] - amount)
        update_account_balance(to_account_number, to_account['balance'] + amount)
        return True
    return False
