import barcode

code = '01230050280'

upc = barcode.get('upc', code)
k = upc.get_fullcode()
b = upc.to_ascii()
print(b)
filename = upc.save('upc13')



