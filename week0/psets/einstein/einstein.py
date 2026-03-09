def main():
    mass = int(input("Enter the mass of the object in kilograms: "))
    print(energy(mass))


def energy(mass):
    speed = 300000000  # Speed of light in meters per second
    return mass * speed**2


if __name__ == "__main__":
    main()


