weather = input("What's the weather like today? (sunny, rainy, cloudy): ").lower()

if weather == "sunny":
  print("Great! Go for a picnic in the park.")
elif weather == "rainy":
  print("Stay indoors and read a book.")
elif weather == "cloudy":
  print("Maybe take a walk with an umbrella.")
else:
  print("I'm not sure about that weather. Observe later and try again!")
