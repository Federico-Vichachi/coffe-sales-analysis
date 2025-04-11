import zipfile

with zipfile.ZipFile('data/coffee-sales.zip', 'r') as zip_ref:
    zip_ref.extractall("coffe-sales")