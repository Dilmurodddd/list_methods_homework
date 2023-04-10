def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    a=0
    b=0
    k=[]
    l=[0,1,2,3,4,5,6,7,8,9]
    while a<len(fruits):
        if fruits[a]=="apple":
            b+=1

        a+=1
    b=str(b)
    b.split()
    if len(b)>0:
        m=int(b)
    
    b.split()
    g=l[:m]
    g.insert(0,int(b))
    return g
print(main(["apple","apple", "banana", "apple", "pear", "apple"]))