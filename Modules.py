import Converters
from Converters import kg_to_lbs

print(kg_to_lbs(70))

print(Converters.lbs_to_kg(154))  # Without "Converters" instance this will throw error
# since we did not do specific function import
