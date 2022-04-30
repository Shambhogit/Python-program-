def dynamic_repet_lyrics(repnam):
    for r in range(repnam):
        if r == repnam-1 :
            print("i miss you so much baby shona mona tona ")
        else:
            print("and i miss you")
        

num = int (input("How many times shall i repeat"))
dynamic_repet_lyrics(num)
