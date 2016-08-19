class Customer(object):

    discount = 0

    def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
        self.name = name
        self.balance = balance
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.addr_line3 = addr_line3

    def owes(self):
       return self.balance - self.discount

    def __str__(self):
        return self.name + "\n" + self.addr_line1 + "\n" + self.addr_line2 + "\n" + self.addr_line3 + "\n" + "Balance: {:.2f}".format(self.balance) + "\n" + "Discount: {}%".format(self.discount) + "\n" + "Amount due: {:.2f}".format(self.owes())


class ValuedCustomer(Customer):
    discount = 10

def main():

    c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare');
    c2 = ValuedCustomer('Lucy', 100, '23 Main Street', 'Roosky', 'Roscommon');
    c3 = Customer('Fred', 200, '24 Main Street', 'Sneem', 'Kerry');

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()





