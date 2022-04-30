#key value pares can be accessed using a key inside [] just like list index.

dom_abbr = {"in":"India","jp":"Japan","ru":"Russia","de":"Denmark"}

keyword = input("which one do you want?")
if keyword in dom_abbr:
    print("that stands for " + dom_abbr[keyword])
else:
    print("sorry that's not available ")