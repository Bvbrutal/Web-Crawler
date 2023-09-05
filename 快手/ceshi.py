lst = [0, 1, 2, 3, 4,5,5,5,5,5, 6, 7, 8, 9,'4545']
print("原列表为：", lst)
exclude=[5]
for key in lst:
        print(key)
        if key in exclude:
                lst.remove(key)
print(lst)
print("删除后的列表为：",len(lst))

