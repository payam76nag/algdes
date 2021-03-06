def merge(left,right):
    sorted=[] #array to store the sorted list
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1

    sorted+=left[i:]
    sorted+=right[j:]
    return sorted

def merge_sort(li):
    "function to compute merge-sort"
    if len(li)==1:
        return li
    middle=len(li)//2
    left_li=merge_sort(li[:middle])
    right_li=merge_sort(li[middle:])
    return merge(left_li,right_li)

if __name__=="__main__":
    s=input()
    li=s.split(' ')
    sorted=merge_sort(li)
    print(sorted)
