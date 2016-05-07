#!/usr/bin/python
# Filename: using_list.py

shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist),'items to purchase'

print 'These items are:', # comma at end of the line
for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shoplist is now', shoplist
print 'I will sort my list now'
shoplist1 = shoplist
shoplist1.sort()
print 'Sorted shopping list is', shoplist1
print 'Original shopping list is', shoplist # changed at the same time

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist
