#modules
#when we want to import entire module
import converters
converters.kg_to_lbs(70)
print(converters.kg_to_lbs(70))
#whem we want to import one fonction of a module
from converters import kg_to_lbs
kg_to_lbs(70)
print(kg_to_lbs(70))
