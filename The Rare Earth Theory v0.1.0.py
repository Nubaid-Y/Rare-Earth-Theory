universal_number = 0

def MainGame():
    print("Welcome to The Rare Earth Theory.\n"
    "In this simulation, you will design a star system and planet to determine whether intelligent life can emerge.\n You can assume the planet is already in the goldilocks zone.\n")

    star = input("Star type (O B A F G K M): ").upper()
    valid = ("O","B","A","F","G","K","M")
    while star not in valid:
        print ("Please answer from the letters OBAFGKM.")
        star = input("Star type (O B A F G K M): ").upper()
        
    while True:
        planet = float(input("Planet mass (Earth = 1): "))
        if planet > 10:
            print("That planet is too big to be terrestrial. Try a smaller size.")
        elif planet < 0.3:
            print("That planet is too small to retain an atmosphere or a magnetic field. Try a larger size.")
        else:
            break

    while True:
        timeframe = float(input("Age (1-10 billion years): "))
        if timeframe < 1:
            print("That is way too short for any life to emerge.")
        elif timeframe > 10 and star != "M":
            print("The star will become too hot for the planet to remain habitable. Only M-type stars stay stable for hundreds of billions of years. Try again.")
        else:
            break

    return(star, planet,timeframe)


def SingleCell(x, y, z):
    single_cell = (x not in ("O", "B") and 0.3 <= y <= 5 and z >= 1)
    if not single_cell:
        return 0, None
    chances = {
        "A":"B",
        "F": "C",
        "G": "D",
        "K": "D",
        "M": "C",
    }
    return 1, chances.get(x)

def Photosynthesis(x, y, z):
    photo = (x not in ("O", "B") and 0.5 <= y <= 3 and z >= 2)
    if not photo:
        return 0, None
    chances = {
        "A":"A",
        "F": "B",
        "G": "C",
        "K": "D",
        "M": "B",
    }
    return 1, chances.get(x)

def Reproduction(x, y, z):
    if x in ("O", "B", "A") or not (0.5 <= y <= 3 and z >= 3):
        return 0, None

    chances = {
        "A": "A",
        "F": "B",
        "G": "C",
        "K": "D",
        "M": "B",
    }
    return 1, chances.get(x)


def Multicellular(x, y, z):
    if x in ("O", "B", "A", "F") or not (0.7 <= y <= 3 and z >= 4):
        return 0, None

    chances = {
        "G": "C",
        "K": "D",
        "M": "B",
    }
    return 1, chances.get(x)


def ComplexLife(x, y, z):
    if x in ("O", "B", "A", "F") or not (0.8 <= y <= 2 and z >= 4):
        return 0, None

    chances = {
        "G": "B",
        "K": "C",
        "M": "A",
    }
    return 1, chances.get(x)


def Intelligence(x, y, z):
    if x in ("O", "B", "A", "F") or not (0.8 <= y <= 2 and z >= 5):
        return 0, None

    chances = {
        "G": "B",
        "K": "C",
        "M": "A",
    }
    return 1, chances.get(x)


x,y,z = MainGame()

SingleCell(x, y, z)
Photosynthesis(x, y, z)
Reproduction(x, y, z)
Multicellular(x, y, z)
ComplexLife(x, y, z)
Intelligence(x, y, z)

universal_number += (
    + SingleCell(x, y, z)[0]
    + Photosynthesis(x, y, z)[0]
    + Reproduction (x, y, z)[0]
    + Multicellular(x, y, z)[0]
    + ComplexLife(x, y, z)[0]
    + Intelligence(x, y, z)[0]
)

LIKELIHOODS = {
    "A": "Unlikely (10–30%)",
    "B": "Possible (30–50%)",
    "C": "Likely (50–75%)",
    "D": "Very likely (75–100%)",
}

if universal_number == 0:
    print("Life did not emerge on your planet. Sorry.")
elif universal_number == 1:
    print("Single-cell organisms emerged on your planet!")
    print("Likelihood: " + LIKELIHOODS[SingleCell(x, y, z)[1]])
elif universal_number == 2:
    print("Photosynthesis occured on your planet!")
    print("Likelihood: " + LIKELIHOODS[Photosynthesis(x, y, z)[1]])
elif universal_number == 3:
    print("Life on your planet evolved to reproduce! Now it can multiply.")
    print("Likelihood: " + LIKELIHOODS[Reproduction(x, y, z)[1]])
elif universal_number == 4:
    print("Multicellular life emerged on your planet!")
    print("Likelihood: " + LIKELIHOODS[Multicellular(x, y, z)[1]])

elif universal_number == 5:        
    print("Complex life emerged on your planet!")
    print("Likelihood: " + LIKELIHOODS[ComplexLife(x, y, z)[1]])
else:
    print("Congratulations! Intelligent life emerged on your planet!")
    print("Likelihood: " + LIKELIHOODS[Intelligence(x, y, z)[1]])