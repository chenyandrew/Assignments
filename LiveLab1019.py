# def displaySortedNumbers():
#
#     num1, num2, num3 = input("Enter three numbers: ").split(",")
#
#     list = [eval(num1), eval(num2), eval(num3)]
#
#     print("The sorted numbers are", sorted(list))
#
#
#
# displaySortedNumbers()
#
# #
#
# def futureInvestmentValue():
#
#     investment = eval(input("The amount invested: "))
#     annual_rate = eval(input("Annual interest rate: "))
#     month_rate = (annual_rate / 100) / 12
#
#     print("Years", "Future Value")
#     for i in range(1,31):
#         months = i * 12
#         print(i, (investment * ((1 + month_rate) ** months)))
#
# futureInvestmentValue()
#
# #
#
# def main():
#
#     print("i", "m(i)")
#     count = 0
#     total = 0
#     for a in range(1, 21):
#         sum = a / (a + 1)
#         total += sum
#         print(a, total)
#         count += 1
#
# main()


def sqrt(n):
    sgn = 0
    if n < 0:
        sgn = -1
        n = -n
    val = n
    while True:
        last = val
        val = (val + n / val) * 0.5
        if abs(val - last) < 0.0000001:
            break
    if sgn < 0:
        return complex(0, val)
    return val

print(sqrt())

# def is_prime (num):
#     divisor = 2
#     limit = int (num ** 0.5) + 1
#     isPrime = True
#     while (divisor < limit) and isPrime:
#         if (num % divisor == 0):
#             isPrime = False
#         divisor = divisor + 1
#     return isPrime
#
# def print_twins():

#     for num in range (2, 1000):
#         twin = num + 2
#         if (is_prime(num)) and (is_prime(twin)):
#             print ("(" + str(num) + ", " + str(twin) + ")")
#
# print_twins()