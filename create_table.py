from teste_amazon import data

with open('iphone_amazon.csv', 'w') as _file:
	_file.write('Name; Price\n')
	for ind in range(0, len(data["name"])):
		_file.write(f'{data["name"][ind]}; {data["price"][ind]}\n')
