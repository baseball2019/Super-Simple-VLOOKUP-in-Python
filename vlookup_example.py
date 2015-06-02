import python_vlookup

value_to_lookup = 'bed-and-bath/accessories'
value_list = ['bed-and-bath/accessories','bed-and-bath/storage-and-hampers/storage','new_entry_x','new_entry_y',1]

def generate_values(value_list):
    for value in value_list:
        yield value

### Basic VLOOKUP, just save your lookup tables as a csv and do it
print python_vlookup.vlookup(value_to_lookup,'example.csv',2)

### Runs Through the debug
print python_vlookup.vlookup(value_list,'example.csv',3,debug='skip')

print python_vlookup.vlookup(value_list,'example.csv',3,debug='fix')


### Faster_vlookup, can take in almost any iterable and returns an iterable
csv_rows = python_vlookup.get_csv_data('example.csv')
column_dict = python_vlookup.create_column_dict(csv_rows,1)

for matched_value in python_vlookup.faster_vlookup(generate_values(value_list),column_dict):
    print matched_value
