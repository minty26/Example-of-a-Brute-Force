import itertools

# THE FOLLOWING SHOULD NOT BE USED FOR HACKING AS IT IS ILLEGAL AND IMMORAL

# THE USERNAME FUNCTION DOES NOT WORK AS IT ISN'T ACTUALLY LOOKING FOR SOMETHING. INSTEAD, IT IS JUST AN EXAMPLE OF WHAT A HACKER WOULD DO, AND THIS ALSO EXPLAINS THE NEED OF 2 FACTOR AUTHENTIFACATION


def brute_force_attack(username):
    password_length = 6
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;':,.<>/?`~"

    for length in range(1, password_length + 1):
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            print(f"Trying password: {password}")

            if password == "correct_password":
                print("Final Password found!")
                return

    print("Password not found.")

# Enter the username for the account you want to see
username = input("Enter the username: ")

# Start the brute force attack
brute_force_attack(username)
