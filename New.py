n = int(input())
books_list = []
maxi, k = 0, 0
temp_name = ''

for i in range(0, n):
    book_name, gender = map(str, input().split('/'))
    if gender == 'm':
        books_list.append(book_name)

for i in books_list:
    k = books_list.count(i)
    if k > maxi:
        maxi = k
        temp_name = i

print(temp_name)
