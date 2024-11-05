# # 1 Foydalanuvchidan raqam so'rang va u 0 dan katta bo'lsa, uni yig'indiga qo'shib boring. 0 kiritilganda, yig'indini chiqarin.
# yigindi = 0
# while True:
#     son = int(input("Raqam kiriting: "))
#     if son > 0:
#         yigindi += son
#     elif son == 0:
#         print("Yig'indi:", yigindi)
#         break

# # 2 A dan B gacha bo’lgan sonlarni yig’indisni ekranga chiqaring.
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))

# yigindi = 0
# son = A
# while son <= B:
#     yigindi += son
#     son += 1

# print("Yig'indi:", yigindi)


# # 3 Foydalanuvchi ekrandan bir nechta raqamlarni ketma – ket kiritadi va kiritlgan raqamlarni list ga qo’shing va hosil bo’lgan listni ekranga chiqaring.
# raqamlar = []
# while True:
#     raqam = input("Raqam kiriting (yoki 'exit' tugatish uchun): ")
#     if raqam.lower() == 'exit':
#         break
#     raqamlar.append(int(raqam))

# print("Raqamlar listi:", raqamlar)

# # 4 x = [1, 2, 3, 14, 5, 6, 6, 7] berilgan list ning katta elemantini toping
# x = [1, 2, 3, 14, 5, 6, 6, 7]
# katta = x[0]
# i = 1

# while i < len(x):
#     if x[i] > katta:
#         katta = x[i]
#     i += 1

# print("Katta element:", katta)


# # 5 x = [1, 2, 3, 14, 5, 6, 6, 7] berilgan list ning katta elemanti nechanchi index da ekanligni chiqaring
# x = [1, 2, 3, 14, 5, 6, 6, 7]
# katta = x[0]
# index = 0
# i = 1

# while i < len(x):
#     if x[i] > katta:
#         katta = x[i]
#         index = i
#     i += 1

# print("Katta element indexi:", index)

# # 6 Ekrandan kirtilgan biror sonning necha xonali ekanligni aniqlang 
# son = int(input("Sonni kiriting: "))
# xonalar_soni = 0

# while son != 0:
#     son //= 10
#     xonalar_soni += 1

# print("Xonalar soni:", xonalar_soni)


# # 7 x = [1, 2, 0, 14, 5, -6] berilgan list ning katta elemanti va kichik elementini toping 
# x = [1, 2, 0, 14, 5, -6]
# katta = x[0]
# kichik = x[0]
# i = 1

# while i < len(x):
#     if x[i] > katta:
#         katta = x[i]
#     elif x[i] < kichik:
#         kichik = x[i]
#     i += 1

# print("Katta element:", katta)
# print("Kichik element:", kichik)


# # 8 . x = [-2, 31, 104, 51, 19, 7] berilgan list ning katta elemantini va kichik elementlarni o’rnini almashting va hosil borga listni ekranga chiqaring
# x = [-2, 31, 104, 51, 19, 7]
# katta_index = 0
# kichik_index = 0
# i = 1

# while i < len(x):
#     if x[i] > x[katta_index]:
#         katta_index = i
#     if x[i] < x[kichik_index]:
#         kichik_index = i
#     i += 1

# x[katta_index], x[kichik_index] = x[kichik_index], x[katta_index]

# print("Natijaviy list:", x)

# 9 . List yaratiladi va ekrandan son kiritiladi kiritilgan son listning ichida bor bo’lsa “Element bor” aks holda “Element yo’q” kabi so’zlarni chiqaring
# x = [3, 5, 7, 10, 15]  # Misol uchun biror list yaratdik
# son = int(input("Sonni kiriting: "))

# i = 0
# topildi = False

# while i < len(x):
#     if x[i] == son:
#         topildi = True
#         break
#     i += 1

# if topildi:
#     print("Element bor")
# else:
#     print("Element yo'q")

# # 10 While operatoridan foydalanib berilgan A va B sonlaring EKUB ni chiqaring
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))

# while B != 0:
#     A, B = B, A % B

# print("EKUB:", A)


# 11 While operatoridan foydalanib berilgan A va B sonlaring EKUK ni chiqaring
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))

# a, b = A, B
# while b != 0:
#     a, b = b, a % b

# ekub = A * B // a
# print("EKUK:", ekub)


# # while1 A va B butun musbat sonlari berilgan (A > B). A uzunlikdagi kesmada maksimal darajada B kesma joylashtirilgan. A kesmaning bo'sh qismini aniqlovchi dastur.
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))

# while A >= B:
#     A -= B

# print("Bo'sh qism:", A)


# # while2 A va B butun musbat sonlari berilgan (A > B). A uzunlikdagi kesmada B kesmadan nechta joylashtirish mumkinligini aniqlovchi dastur.
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))

# count = 0
# while A >= B:
#     A -= B
#     count += 1

# print("Joylashtirishlar soni:", count)


# # while3 N va K butun musbat sonlari berilgan. Faqat ayirish va qo'shish amallaridan foydalanib N sonini K songa bo'lgandagi qoldiqni topuvchi dastur.
# N = int(input("N ni kiriting: "))
# K = int(input("K ni kiriting: "))

# while N >= K:
#     N -= K

# print("Qoldiq:", N)

# # while4 n butun soni berilgan (n > 0). Agar n soni 3 ning darajasi bo'lsa, "3 ning darajasi" deb chiqaring, aks holda "3 ning darajasi emas" deb chiqaring.
# n = int(input("n ni kiriting: "))

# while n % 3 == 0:
#     n //= 3

# if n == 1:
#     print("3 ning darajasi")
# else:
#     print("3 ning darajasi emas")



# # while5 2 sonining qandaydir darajasi bilan mos keladigan n butun soni (n > 0) berilgan.
# n = int(input("n ni kiriting: "))

# daraja = 0
# m = 1
# while m < n:
#     m *= 2
#     daraja += 1

# if m == n:
#     print("Daraja:", daraja)
# else:
#     print("Mos kelmaydi")


# while6 n natural soni berilgan. Quyidagi ifodani hisoblovchi dastur: n! = n * (n-2) * (n-4) …
# n = int(input("n ni kiriting: "))

# factorial = 1
# while n > 0:
#     factorial *= n
#     n -= 2

# print("Natija:", factorial)


# while7 n natural soni berilgan. Kvadrati n dan katta bo'lgan eng kichik butun k sonini toping.
# n = int(input("n ni kiriting: "))

# k = 1
# while k * k <= n:
#     k += 1

# print("Natija:", k)

# while8 n natural soni berilgan. Kvadrati n dan katta bo'lmagan eng katta butun k sonini toping.
# n = int(input("n ni kiriting: "))

# k = 0
# while (k + 1) * (k + 1) <= n:
#     k += 1

# print("Natija:", k)


# # while9 n natural soni berilgan (n > 1). 3^k >= n shartini qanoatlantiruvchi eng kichik butun k sonini toping.
# n = int(input("n ni kiriting: "))

# k = 0
# power = 1
# while power < n:
#     power *= 3
#     k += 1

# print("Natija:", k)


# while10 n natural soni berilgan (n > 1). 3^k < n shartini qanoatlantiruvchi eng katta butun k sonini toping.
# n = int(input("n ni kiriting: "))

# k = 0
# power = 1
# while power * 3 < n:
#     power *= 3
#     k += 1

# print("Natija:", k)


# while11 n natural soni berilgan. (1 + 2 + 3 + ... + k) >= n shartini qanoatlantiruvchi eng kichik k sonini toping.
# n = int(input("n ni kiriting: "))

# k = 1
# summa = 0
# while summa < n:
#     summa += k
#     k += 1

# print("Natija:", k - 1)

# while12 n natural soni berilgan. (1 + 2 + 3 + ... + k) < n shartini qanoatlantiruvchi eng katta k sonini toping.
# n = int(input("n ni kiriting: "))

# k = 1
# summa = 0
# while summa + k < n:
#     summa += k
#     k += 1

# print("Natija:", k - 1)


# while13 a soni berilgan. (1 + 1/2 + 1/3 + … + 1/k) >= a shartini qanoatlantiruvchi eng kichik k sonini toping.
# a = float(input("a ni kiriting: "))

# k = 1
# summa = 0.0
# while summa < a:
#     summa += 1 / k
#     k += 1

# print("Natija:", k - 1)


# while14 a soni berilgan. (1 + 1/2 + 1/3 + … + 1/k) <= a shartini qanoatlantiruvchi eng katta k sonini toping.
# a = float(input("a ni kiriting: "))

# k = 1
# summa = 0.0
# while summa + (1 / (k + 1)) <= a:
#     k += 1
#     summa += 1 / k

# print("Natija:", k)