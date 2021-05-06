def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    else:
        tuple_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    else:
        tuple_b = (tuple_b[0], tuple_b[1])
    element_1 = tuple_a[0] + tuple_b[0]
    element_2 = tuple_a[1] + tuple_b[1]
    new_tuple = (element_1, element_2)

    return new_tuple
