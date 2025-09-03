def number_of_bottles():
    for bottles in range(99, -1, -1):
        if bottles == 0:
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
        elif bottles == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
        elif bottles == 2:
            print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")
        else:
            print(f"{bottles} bottles of milk on the wall, {bottles} bottles of milk. Take one down and pass it around, {bottles - 1} bottles of milk on the wall.")

    
    
# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
number_of_bottles()
