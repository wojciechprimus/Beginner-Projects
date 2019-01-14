i=100

while i > 2:
    print(i,"bottles of beer on the wall", i, "bottles of beer.")
    print("Take one down and pass it around", i-1 ,"bottles of beer on the wall")
    i=i-1
else:
    print(i,"bottles of beer on the wall", i, "bottles of beer.")
    print("Take one down and pass it around", i-1,"bottle of beer on the wall")
    print(i-1 , "bottle of beer on the wall", i-1 , "bottle of beer.")
    print("""Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.""")
