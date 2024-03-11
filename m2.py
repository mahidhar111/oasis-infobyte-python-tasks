def calculate_bmi(weight, height):
  """
  Calculates the Body Mass Index (BMI) for a given weight and height.

  Args:
      weight: Weight in kilograms (kg).
      height: Height in meters (m).

  Returns:
      The calculated BMI as a float.
  """
  return weight / (height * height)

def interpret_bmi(bmi):
  """
  Interprets the calculated BMI based on standard BMI categories.

  Args:
      bmi: The calculated BMI value.

  Returns:
      A string describing the BMI category.
  """
  if bmi <= 18.5:
    return "Underweight"
  elif bmi <= 24.9:
    return "Normal weight"
  elif bmi <= 29.9:
    return "Overweight"
  else:
    return "Obese"

def main():
  """
  Prompts the user for weight and height, calculates BMI, and displays the result.
  """
  while True:
    try:
      weight = float(input("Enter your weight in kilograms (kg): "))
      height = float(input("Enter your height in meters (m): "))
      break
    except ValueError:
      print("Invalid input. Please enter numerical values for weight and height.")

  bmi = calculate_bmi(weight, height)
  bmi_category = interpret_bmi(bmi)

  print(f"Your BMI is: {bmi:.2f}")
  print(f"BMI category: {bmi_category}")

if __name__ == "__main__":
  main()
