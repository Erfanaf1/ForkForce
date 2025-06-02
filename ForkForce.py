# اگر این کامنت رو میبینی یعنی ریپازیتوری رو کلون کردی روی ادیتورت.
#  n حالا این زیر 👇🏻 یک تابع بنویس که یک عدد ورودی
#  بگیره و یک عملیات ریاضی به دلخواه روش انجام بده و مقدار نهایی رو برگردونه.



# Defined by Asle Falah
def power_if_prime(n):

    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return n ** 2
    else:
        return n


# Defined by Mahdi Dolati Zadeh
def IsEven(Number):
    if Number % 2 == 0:
        return Number
    else:
        return Number + 1


# Defined by Mahdi Safarzadeh
def exp(x):
    f = 1
    if x < 0:
        x = (-1) * x
        f = -1
    xs = 1
    nm = 1
    ex = 1
    for i in range(1, x * 18):
        xs *= x
        nm *= i
        ex += (xs / nm)
    if f == -1:
        ex = 1 / ex
    return ex


# defined by Abolfazl
def powerOfTwo(n):
    return 2**n


# defined by ali,kamalpour
def logarithm(n, base=10):
    if n <= 0:
        return None
    result = 0
    current = n
    while current >= base:
        current /= base
        result += 1
    return result



# Defined by ali ebrahimi
def absolute_value(n):
    if n >= 0:
        return n
    else:

        return -n
    

#defined by Shokoohi
def power_of_three(n):
    return n**3



      
# defined by Ali Mirahmadi
def sin(x):
    n=10
    s = x
    for i in range(2, n+1):
        k = 2*i-1
        f = 1
        for j in range(1, k+1):
            f = f * j
        if i % 2 == 0:
            s = s-(x**k)/f
        else:
            s = s+(x**k)/f
        return s


# defined by seyed mehdi banaroie
def factoriel(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s


# defiend by Ilia parkan
def power(a):
    a=a**2
    return a


#defined by alireza adl gostar
def is_odd(n):
    if n%2!=0:
        return n
    else:
        return n+1


# Defiend By <Ali Negintaj>
def lengh(x):
    tedad = 0
    for i in str(x):
        tedad+=1
    return tedad    


# Defined by Amir Ansari
def custom_math_operation(number):
    if number % 2 == 0:
        return number * 2
    else:
        return number * 3

    
#defined by MohammadHossein Homayunfar
def doubleplus(n):
    n=(n*2)+2
    return n

    
# Defined by mohammad alipour
def trangle (a):
    if a%2==0:
        return a**2
    else:
        return round(a**(1/2))


#Defined By Emad Ahmadi
def fibonacci_sequence(n):
    if not isinstance(n, int):
        return "Error: Input must be an integer"
    if n <= 0:
        return "Error: Input must be a positive integer"
    
    fib_list = [0, 1] if n > 1 else [0] if n == 1 else []
    
    for i in range(2, n):
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    
    sequence_sum = sum(fib_list)
    
    return sequence_sum



#defined by moaref poor 
def idk(n):
    return n + 56



#defined by MohammadmahdiRezapour
def A_B(n):
    if n >= 0:
        return -n
    else:

        return n
    



def main():

    while True :
        try :
            
            print("\n<< Hi... Im gonna get a number from You and do some math on It...>>")
            number = int(input("Enter a number between 1 - 10 :  "))
            if  not(1 <= number <= 10) :
                print("\n!!! Invalid Number. Try Again !!!")
                continue

        except :
            print("\n!!! Enter a number !!!")
            continue
        

        Defs = [
    power_if_prime, IsEven, exp, powerOfTwo, logarithm,
    absolute_value, power_of_three, sin, factoriel, power, is_odd,
    lengh, custom_math_operation, doubleplus, trangle, fibonacci_sequence,
    idk, A_B ]
        

        final_number = 0
        for Def in Defs :
            final_number += round(Def(number) , 2)



        print(f"\nYour final number is : {final_number}\n")
        
        while True:
            try :

                Req = int(input("Do you want to try Another One? \n (1 for continue  and  2 for Exit) \n"))
                if Req == 2 :
                    return
                
                elif Req == 1 :
                    break

                else:
                    print("\n!! Enter a valid number !!\n")
                    continue

            except :
                print("\n!! Enter a number !!\n")
                continue

    


main()