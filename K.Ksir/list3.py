#few important list functions.
#More dynamic operations.
#insert() adds item at specific location.
#remove() Removes the item with the specified value. 
#index() returns position of given value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
#clear()

langs = ["Python","Java","Ruby","Perl"]
langs.insert(1,"PHP")
print(langs)
langs.remove("Perl")
print(langs)
print("index of %s is %d" %("Java",langs.index("Java")))
langs.reverse()
print(langs)

langs.sort()
print(langs)
langs.clear()
print(langs)