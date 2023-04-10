def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    a=0
    b=0
    while a<len(list01):
        if list01[a]==0:
            b+=1
        a+=1
    return b
print(main([1,0,1,0,1,0,1]))