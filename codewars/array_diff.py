def array_diff(a, b):
    #task https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
    
    def del_same_el_from_list(arr):
        new_list = []

        for i in arr:
            if i in new_list:
                continue
            else:
                new_list.append(i)

        return new_list

    a, b = map(del_same_el_from_list, [a, b])
    
    c = [i for i in a if not(i in b)]

    return c
