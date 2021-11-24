import random
import string

DEBUG = True
host = ''
database = ''
user=''
passwd=''
port = '5432'
SECRET_KEY = '123123'

gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))


