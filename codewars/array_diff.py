def array_diff(a, b):
    #task https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
    
    #Your goal in this kata is to implement a difference function,
    #which subtracts one list from another and returns the result.
    
    #It should remove all values from list a,
    #which are present in list b keeping their order.
    
    #If a value is present in b, 
    #all of its occurrences must be removed from the other
    
    def del_same_el_from_list(arr):
        new_list = []

        for i in arr:
            if i in new_list:
                continue
            else:
                new_list.append(i)

        return new_list

    a, b = map(del_same_el_from_list, [a, b])
    
    

    return [a, b]

def main():

    print(array_diff([1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5], [4, 4, 4, 4, 4, 5, 6, 7]))

    return 0


if __name__ == '__main__':
    main()
