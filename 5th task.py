talents = float(input("enter numbers of talents"))
pounds = float(input("enter numbers of pounds"))
lots = float(input("enter numbers od lots"))
total_lots = talents * 20 * 32 + pounds * 32 + lots
total_grams =total_lots * 13.3

kilograms = total_grams // 1000
grams = total_grams % 1000
print("weight in modern units is",)
print (kilograms, "kilograms","and",(grams),"grams")


