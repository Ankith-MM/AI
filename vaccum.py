combinations = [
    ("dirty", "dirty"),
    ("dirty", "clean"),
    ("clean", "dirty"),
    ("clean", "clean")
]

start_loc = input("Enter initial location (A/B): ").strip().upper()

for state_A, state_B in combinations:
    print(f" Testing Combination: Room A = '{state_A}', Room B = '{state_B}'")
    room_A = state_A
    room_B = state_B
    loc = start_loc

   
    if room_A == "clean" and room_B == "clean":
        print(f"Room {loc} is already clean.")
    
  
    while room_A == "dirty" or room_B == "dirty":
        if loc == "A":
            if room_A == "dirty":
                print("Room A is dirty -> Cleaning...")
                room_A = "clean"
            else:
                print("Room A is clean -> Moving to Room B")
                loc = "B"
        else:
            if room_B == "dirty":
                print("Room B is dirty -> Cleaning...")
                room_B = "clean"
            else:
                print("Room B is clean -> Moving to Room A")
                loc = "A"

    print("\n--- Final Status ---")
    print("The status of room A is:", room_A)
    print("The status of room B is:", room_B)
