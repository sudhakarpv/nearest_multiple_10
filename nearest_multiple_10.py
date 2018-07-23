# nearest_multiple_10
def main():
    pass
    n=int(input())
    fin=int((n*10))
    flag=0
    for i in range(n,fin+1):
        if(i%10==0):
            flag+=1
        if (flag==1):
            break
    print(i)
if __name__ == '__main__':
    main()
