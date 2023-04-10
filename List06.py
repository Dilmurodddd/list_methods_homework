def main(fruits):
    """
    Given a list called Fruits, it contains at least one apple. Find how many apples are on the list and return.
    Args:
        fruits(list): parameter
    Returns:
        int: return answer
    """
    a=0
    b=0
    while a<len(fruits):
        if fruits[a]=='apple':
            b+=1
        a+=1
    return b
print(main(["apple", "banana", "apple", "pear"]))