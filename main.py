# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread= n*[0]
    
    for i in range(m):
        next=0
        for x in range(1,n):
                if thread[next] > thread[x]:
                    next=x
                    
        pirmais=thread[next]
        pedejais=pirmais+data[i]
        thread[next]=pedejais
        
        output.append((next,pirmais))
        
    return output

def main():
    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    
    result = parallel_processing(n,m,data)
    for i in range(m):
        print(result[i][0],result[i][1])
    
   ## if not(10**5>= n >=1):
       ## raise ValueError("n 

    
if __name__ == "__main__":
    main()
