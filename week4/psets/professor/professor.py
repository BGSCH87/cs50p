import random


def main():
    
    #random generate 10 math problems: X + Y
    level = get_level()
    score = 0
    
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        tries = 0 

        while True:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    score += 1
                    break # Correct! Move to the next of the 10 problems
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
            
            # If we've failed 3 times, show answer and move to next problem
            if tries == 3:
                print(f"{x} + {y} = {answer}")
                break

    print(f"Score: {score}")

            

        

def get_level():
    #ask the user for the level they want to play in, in little professor
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                continue
            else:
                break
        except ValueError:
            pass
    return level



def generate_integer(level):
    #ONLY job is to give back ONE number
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else: 
        raise ValueError




if __name__ == "__main__":
    main()