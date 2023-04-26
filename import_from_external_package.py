import of module from the extern package
'''import ecommerce.shipping
ecommerce.shipping.calc_shipping()'''

#or when Iwant to import one fonction of a extern module
'''from ecommerce.shipping import calc_shipping, [another fonction]
calc_shipping()'''

#for entire module:
from ecommerce import shipping
shipping.calc_shipping()
