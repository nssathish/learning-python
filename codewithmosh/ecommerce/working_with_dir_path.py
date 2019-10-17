from pathlib import Path
from openpyxl import pivot

path = Path("..\\ecommerce")

print(path.exists())

path = Path("..\\emails")

path.mkdir()
path.rmdir()

path = Path("..\\")

for file in path.glob("*.py"):
    print(file)