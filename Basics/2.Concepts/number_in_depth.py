import math

# random
import random  

l1 = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(l1))  # randomly prints one item

random.shuffle(l1)
print(l1)

# Decimal condext manager

# >>> 0.1+0.1+0.4
# 0.6000000000000001
# >>> 0.1+0.1+0.1
# 0.30000000000000004
# >>> 0.1+0.1+0.1-0.3
# 5.551115123125783e-17
# >>> (0.1+0.1+0.1)-0.3
# 5.551115123125783e-17

# >>> from decimal import Decimal
# >>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
# Decimal('0.3')
# >>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
# Decimal('0.0')