from utils import *
from models import *

all_objects = list(filter(lambda obj: not obj.startswith('__'), dir()))
print(all_objects)