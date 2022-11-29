num=int(input('input n: '))
if num>0:
    def ugly_number(num):
        "find ugly number"
        new_list=[]
        num_1=1
        while len(new_list)<num:
            if num_1==1 :
                new_list.append(num_1)
                num_1+=1
            else:
                index=0
                divide=[2,3,5]
                new1=int(num_1)
                while index<len(divide):
                    if new1%divide[index]==0:
                        new1=new1/divide[index]
                    else:
                        index+=1
                if new1==1:
                    new_list.append(num_1)
                num_1+=1
    
        return(new_list)
    def n_th_ugly_number():
        "select n_th ugle number"
        new_num=ugly_number(num)
        return new_num[-1]
    func_call=n_th_ugly_number()
    print("The",num,"th ugly number is",func_call)
else:
    print("Invalid Input")
        
                        
                    
                
