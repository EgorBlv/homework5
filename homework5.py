immutable_var = (1, 2, True, 'hold')
print(immutable_var)
#immutable_var [0] = 100 # кортеж не изменит свое значение. Если использовать список внутри кортежа тогда возможно изменить части кортежа. Воспринимает как строку?
mutable_list = [1, 2, True, 'dark']
print(mutable_list)
mutable_list [0] = 606
mutable_list [2] = False
print(mutable_list)