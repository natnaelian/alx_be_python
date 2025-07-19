#recieving input from user.
x = input("What's the weather like today? (sunny/rainy/cold): ")

#conditions
if x == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif x == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif x == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")    
