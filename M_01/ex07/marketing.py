import sys


def create_promotional(clients, participants, recipients):
    result = set(clients + participants) - set(recipients)
    print(list(result))

def create_loyal(clients, participants):
    result = set(participants) - set(clients)
    print(list(result))

def create_clients(clients, participants):
    result = set(clients) - set(participants)
    print(list(result))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',
                   'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
        participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                        'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
        recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
        if sys.argv[1] == 'call_center':
            create_promotional(clients, participants, recipients)
        elif sys.argv[1] == 'loyalty_program':
            create_loyal(clients, participants)
        elif sys.argv[1] == 'potential_clients':
            create_clients(clients, participants)
        else:
            print("Unknown perform list")
