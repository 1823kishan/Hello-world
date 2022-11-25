# n = int(input("enter your number"))
# i = 1
# while i <= 10:
#     print(n, "*", i, "=", n*i)
#     i += 1
#--------------------------------------------------------------------
# n = int(input("enter a number"))
# while n>=1:
#     print(n, end=" ")
#     n-=1
#-----------------------------------------------------------------------
# n = int(input("enter number"))
# for i in range(n, 0, -1):
#     print(i, end= " ")
#---------------------------------------------------------------------------

# n = int(input("enter number"))
# temp = n
# reversed = 0
# while temp>0:
#     riminder = temp % 10
#     temp //= 10
#
#     reversed = reversed * 10 + riminder
# print(reversed)
#
# if n==reversed:
#     print("it is palindrome")
# else:
#     print(" it is not palindrome number")
#-------------------------------------------------------------------
# n = int(input("enter number"))
#
# fact = 1
#
# while n >= 1:            for i in range(n, 1, -1):
#     fact = fact * n           fact = fact*i
#     n -= 1
# print(fact)
#---------------------------------------------
# n = int(input("enter your number"))
# for i in range(2, n):
#     if n % i == 0:
#         print(" not prime")
#         break
# else:
#     print("prime")
#------------------------------------------------------------------
# n = int(input("enter your number"))
# i =1
# while i<=n:
#     j = 1
#     while j<=i:
#         print("*", end=" ")
#         j+=1
#     print()
#     i+=1
#----------------------------------------------------
# n = int(input("enter your number"))
# i = 1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*", end=" ")
#         j+=1
#     print()
#     i+=1
#---------------------------------------------------------------
# n = int(input("enter your number"))
# i = 1
# while i<=n:
#     j=n
#     while j>=i:
#         print("*", end=" ")
#         j-=1
#     print()
#     i+=1