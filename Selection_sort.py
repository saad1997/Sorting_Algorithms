def Selection_sort(arr):
    
    x = arr
    print ("Selection Sort")
    print ("TOTAL LENGTH OF ARRAY " +str(len(x)))
    for y in range(len(x)):
        for z in range(y+1,len(x)):
            if (x[y]>x[z]):
                x1 = x[y]
                x2 = x[z]
                x[y] = x2
                x[z] = x1
            else:
                continue
        
        print(x)
def main():
    str_arr = input().split(' ') # will take in a string of numbers separated by a space
    x = [int(num) for num in str_arr]
    Selection_sort(x)
    input()


if  __name__ =='__main__':
    main()
    
        
    
    
        
