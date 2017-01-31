# def main():
#     #
#     # for i in range(1,7):
#     #     for j in range(1, i ):
#     #         print(j, end = " ")
#     #     print(" ")
#     #
#     # print(" ")
#     #
#     # for a in range(1, 7):
#     #     for b in range(1, 8-a):
#     #         print(b, end= " ")
#     #     print(" ")
#     #
#     # for c in range(1, 8):
#     #     for d in range(7, c, -1):
#     #         print(end = " ")
#     #     for e in range(a, 1, -1):
#     #         print(e, end= " ")
#     #     for f in range(1, a+1):
#     #         print(f, end = " ")
#     #     print(" ")
#
#     for i in range(11, 0, -1):
#         print(i * "*")
#
#
# main()

def main():

    num = int(input("Enter: "))
    # limit = int(num ** 0.5) + 1
    # is_prime = True
    # divisor = 2
    # while (divisor < limit) and is_prime:
    #     if (num % divisor == 0):
    #         is_prime = False
    #     divisor = divisor + 1
    # if (is_prime) and (num != 1):
    #     print(num, "is prime")
    # else:
    #     print(num, "is not prime")

    sum_div = 0
    divisor = 1
    limit = num // 2
    while (divisor <= limit):
        if (num % divisor == 0):2
            sum_div = sum_div + divisor
        divisor += 1
    print(sum_div)

    if num == sum_div:
        print(num, " is a perfect number.")
    else:
        print(num, "is not perfect.")

main()

