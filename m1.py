import random
import string

def generate_password(length):
  """
  Generates a random password of the specified length.

  Args:
      length: The desired length of the password.

  Returns:
      A randomly generated password as a string.
  """

  # Define character sets for different categories
  lowercase_letters = string.ascii_lowercase
  uppercase_letters = string.ascii_uppercase
  digits = string.digits
  symbols = string.punctuation

  # Combine character sets for password generation
  all_characters = lowercase_letters + uppercase_letters + digits + symbols

  # Generate password using random choices
  password = ''.join(random.choices(all_characters, k=length))

  return password

def main():
  """
  Prompts the user for desired password length and displays the generated password.
  """
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        print("Password length should be at least 8 characters.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a numerical value.")

  password = generate_password(length)
  print("Your generated password is:", password)

if __name__ == "__main__":
  main()
