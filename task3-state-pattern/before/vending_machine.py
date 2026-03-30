STATE_IDLE = 'idle'
STATE_HAS_MONEY = 'has_money'
STATE_DISPENSING = 'dispensing'
STATE_OUT_OF_STOCK = 'out_of_stock'

def insert_coin(machine, amount):
    if machine['state'] == STATE_IDLE:
        machine['balance'] += amount
        machine['state'] = STATE_HAS_MONEY
        print(f'Accepted {amount}. Balance: {machine["balance"]}')
    elif machine['state'] == STATE_HAS_MONEY:
        machine['balance'] += amount
        print(f'Added {amount}. Balance: {machine["balance"]}')
    elif machine['state'] == STATE_DISPENSING:
        print('Please wait, dispensing...')
    elif machine['state'] == STATE_OUT_OF_STOCK:
        print('Out of stock. Returning coin.')

def select_product(machine, product_id):
    if machine['state'] == STATE_IDLE:
        print('Please insert money first')
    elif machine['state'] == STATE_HAS_MONEY:
        product = machine['products'].get(product_id)
        if not product:
            print('Invalid product')
            return
        if product['stock'] == 0:
            machine['state'] = STATE_OUT_OF_STOCK
            return
        if machine['balance'] < product['price']:
            print(f'Insufficient funds. Need {product["price"]}')
            return
        machine['state'] = STATE_DISPENSING
        machine['balance'] -= product['price']
        product['stock'] -= 1
        print(f'Dispensing {product["name"]}')
        if product['stock'] == 0:
            machine['state'] = STATE_OUT_OF_STOCK
        else:
            machine['state'] = STATE_IDLE
    elif machine['state'] == STATE_DISPENSING:
        print('Please wait, dispensing...')
    elif machine['state'] == STATE_OUT_OF_STOCK:
        print('Out of stock')

def cancel(machine):
    if machine['state'] == STATE_IDLE:
        print('No transaction to cancel')
    elif machine['state'] == STATE_HAS_MONEY:
        print(f'Returning {machine["balance"]}')
        machine['balance'] = 0
        machine['state'] = STATE_IDLE
    elif machine['state'] == STATE_DISPENSING:
        print('Cannot cancel, dispensing in progress')
    elif machine['state'] == STATE_OUT_OF_STOCK:
        print(f'Returning {machine["balance"]}')
        machine['balance'] = 0
        machine['state'] = STATE_IDLE

def refill(machine, product_id, quantity):
    if machine['state'] == STATE_IDLE:
        if product_id in machine['products']:
            machine['products'][product_id]['stock'] += quantity
            print(f'Refilled {product_id} with {quantity} units')
    elif machine['state'] == STATE_HAS_MONEY:
        print('Cannot refill, transaction in progress')
    elif machine['state'] == STATE_DISPENSING:
        print('Cannot refill, dispensing in progress')
    elif machine['state'] == STATE_OUT_OF_STOCK:
        if product_id in machine['products']:
            machine['products'][product_id]['stock'] += quantity
            print(f'Refilled {product_id} with {quantity} units')
            machine['state'] = STATE_IDLE
