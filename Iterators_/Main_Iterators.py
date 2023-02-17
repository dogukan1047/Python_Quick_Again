# iterator ,iterable ve iteration
# __iter__() ve __next__()
#__iter__() bir iterator döndürür


sayilar=[2,4,5,7,8,9]

i_sayilar=iter(sayilar)

print(i_sayilar.__next__())
print(next(i_sayilar))
print(i_sayilar.__next__())
print(next(i_sayilar))

