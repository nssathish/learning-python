import utils
from utils import find_max

print(utils.find_max([1,10,5,6,3,2,0]))

print(find_max([100,1234,12,1324,22]))

from ecommerce import shipping
shipping.calc_shipping()

from ecommerce.shipping import calc_shipping,calc_tax
calc_tax()
calc_shipping()
