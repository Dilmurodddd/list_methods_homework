def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    a=0
    b=0
    c=0
    while a<len(list1):
        if list1[a]==1:
            b+=1
        if list1[a]==0:
            c+=1
        a+=1
    return b,c

print(main([1, 0, 0, 0, 1, 0, 1, 0]))