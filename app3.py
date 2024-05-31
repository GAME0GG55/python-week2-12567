num_string= '12.25'
num_integer = 23

print('Data typecasting:',type(num_string))
#explicit type conversing
num_string =float(num_string)
print(f'Data Type Casting:{num_string}',type(num_string))

num_sum = num_integer + num_string
print(f'Sum:
{num_sum}',type(num_sum))