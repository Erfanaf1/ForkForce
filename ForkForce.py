# اگر این کامنت رو میبینی یعنی ریپازیتوری رو کلون کردی روی ادیتورت. 
#  n حالا این زیر 👇🏻 یک تابع بنویس که یک عدد ورودی 
#  بگیره و یک عملیات ریاضی به دلخواه روش انجام بده و مقدار نهایی رو برگردونه.

    
# defined by Abolfazl 
def powerOfTwo(n):
    return 2**n


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