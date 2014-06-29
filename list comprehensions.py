__author__ = 'kdoddipalle'
first_list = [1, 'two', 3, 'four', 5]
second_list = [item for item in first_list if type(item) == int]
print second_list