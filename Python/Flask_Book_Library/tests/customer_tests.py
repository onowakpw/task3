import unittest
from project.customers.models import Customer

class CustomerValidTest(unittest.TestCase):
    def test_name(self):
        names = ['Oscar NŁ', 'Jane D. Tolkien', 'Oscar-Jane-2.L\'.MO Drake']
        for name in names:
            Customer(name, 'Warsaw', 60, '01234567899', 'street', '12B/D')
    
    def test_cities(self):
        cities = ['Warsaw', 'Warszawa k. Dł', 'Gdynia Północ']
        for city in cities:
            Customer('Jan Kowalski', city, 20, '01234567899', 'street', '12B/D')
    
    def test_age(self):
        ages = [5, 11, 123]
        for age in ages:
            Customer('Jan Kowalski', 'City', age, '01234567899', 'street', '12B/D')
    
    def test_pesel(self):
        pesels = ['01234567890', '11111111111', '24723774790']
        for pesel in pesels:
            Customer('Jan Kowalski', 'Miastko', 20, pesel, 'street', '12B/D')
    
    def test_streets(self):
        streets = ['Długa', 'Warszawa k. Dł ul. 121239./druga', ' Ulica szeroka '*20]
        for street in streets:
            Customer('Jan Kowalski', 'Warszawa', 25, '01234567899', street, '12')
    
    def test_appNo(self):
        appNos = ['Pierwszy', '12.f', '8/de k.5']
        for appNo in appNos:
            Customer('Jan Kowalski', 'Warszawa', 25, '01234567899','Street', appNo)

class CustomerInvalidTest(unittest.TestCase):
    def test_name(self):
        names = ['X', '!@#!$&>']
        for name in names:
            with self.assertRaises(ValueError):
                Customer(name, 'Warsaw', 60, '01234567899', 'street', '12B/D')
        
    def test_cities(self):
        cities = [' ', 'Gd@ynia Północ"*&#&@&']
        for city in cities:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', city, 20, '01234567899', 'street', '12B/D')
    
    def test_age(self):
        ages = [0, 200]  
        for age in ages:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'City', age, '01234567899', 'street', '12B/D')
    
    def test_pesel(self):
        pesels = ['01234567890232', '0', ' ', -13]  
        for pesel in pesels:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Miastko', 20, pesel, 'street', '12B/D')

    def test_streets(self):
        streets = [' ', '*&^$$!@'] 
        for street in streets:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Warszawa', 25, '01234567899', street, '12')

    def test_appNo(self):
        appNos = ['@@&^%$#', ' '] 
        for appNo in appNos:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Warszawa', 25, '01234567899', 'Street', appNo)

class CustomerExtremeTest(unittest.TestCase):
    def test_name(self):
        names = [None, 'X'*100]
        for name in names:
            with self.assertRaises(ValueError):
                Customer(name, 'Warsaw', 60, '01234567899', 'street', '12B/D')
        
    def test_cities(self):
        cities = ['', None , 'X'*200]
        for city in cities:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', city, 20, '01234567899', 'street', '12B/D')
    
    def test_age(self):
        ages = [-200, 99999999999999999, 999, 'Aeer']  
        for age in ages:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'City', age, '01234567899', 'street', '12B/D')
    
    def test_pesel(self):
        pesels = ['012345678902323'*20, '', None]  
        for pesel in pesels:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Miastko', 20, pesel, 'street', '12B/D')

    def test_streets(self):
        streets = ['', 'X' * 300, None] 
        for street in streets:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Warszawa', 25, '01234567899', street, '12')

    def test_appNo(self):
        appNos = ['', 'LongAppNumber1234567890', None] 
        for appNo in appNos:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Warszawa', 25, '01234567899', 'Street', appNo)

class CustomerInjectionTest(unittest.TestCase):
    def test_name(self):
        names = ["' OR 1=1; --", "' OR 'a'='a", "'; DROP TABLE users; --", "' OR '1'='1", "admin' --"]
        for name in names:
            with self.assertRaises(ValueError):
                Customer(name, 'Warsaw', 60, '01234567899', 'street', '12B/D')
        
    def test_cities(self):
        cities = ["<script>alert('Injected!');</script>", "'; alert('Injected!'); //", "\"<img src=x onerror=alert('Injected!')>\"", "`); alert('Injected!'); (`", "\"></script><script>alert('Injected!');</script>"]
        for city in cities:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', city, 20, '01234567899', 'street', '12B/D')
    
    def test_pesel(self):
        pesels = ["' OR 1=1; --", "' OR 'a'='a", "'; DROP TABLE users; --", "' OR '1'='1", "admin' --"]  
        for pesel in pesels:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Miastko', 20, pesel, 'street', '12B/D')

    def test_streets(self):
        streets = ["<script>alert('Injected!');</script>", "'; alert('Injected!'); //", "\"<img src=x onerror=alert('Injected!')>\"", "`); alert('Injected!'); (`", "\"></script><script>alert('Injected!');</script>"]
        for street in streets:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Warszawa', 25, '01234567899', street, '12')

    def test_appNo(self):
        appNos = ["' OR 1=1; --", "' OR 'a'='a", "'; DROP TABLE users; --", "' OR '1'='1", "admin' --"] 
        for appNo in appNos:
            with self.assertRaises(ValueError):
                Customer('Jan Kowalski', 'Warszawa', 25, '01234567899', 'Street', appNo)