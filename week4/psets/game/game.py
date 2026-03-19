import random

def check_answer(answer, guess):
    if guess < answer:
        print("Too small!")
        return False
    elif guess > answer:
        print("Too large!")
        return False
    else:
        guess == answer
        print("Just right!")
        return True
    

def main():
    #Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
    while True:
        try:
            n = int(input("Level: "))
            if n < 0: 
                continue
            else:
                break
        except ValueError:
            pass

    #Randomly generates an integer between 1 and 𝑛, inclusive, using the random module
    answer = random.randint(1, n)
    
    #Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <=0:
                continue
            if check_answer(answer, guess):
                break
        except ValueError:
            pass
    

if __name__ == "__main__":
    main()