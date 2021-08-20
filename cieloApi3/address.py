class Address(object):

    def __init__(self, street=None, number=None, complement=None, zip_code=None, city=None, state=None, country=None):

        self.street = street
        self.number = number
        self.complement = complement
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.country = country