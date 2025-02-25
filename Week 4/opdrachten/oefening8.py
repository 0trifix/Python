def is_sublist(lst1, lst2):
    if len(lst1) > len(lst2):
        return False
    for i in range(len(lst2) - len(lst1) + 1):
        if lst1 == lst2[i:i + len(lst1)]:
            return True
    return False

def possible_sublists(lst1):
    sublists = [[]]
    for i in range(len(lst1)):
        for j in range(i + 1, len(lst1) + 1):
            sublists.append(lst1[i:j])
    return sublists

def main():
    my_list = [1, 2, 3, 4, 5]
    sub_list = [3, 5]
    print(is_sublist(sub_list, my_list))
    print(possible_sublists(my_list))

if __name__ == '__main__':
    main()
