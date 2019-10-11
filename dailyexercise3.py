def main():
    """

    :return: to the equation
    """
    first_number = (float(input("what is your first number")))
    second_number = (float(input("what is your second number")))
    third_number = (float(input("what is your third number")))
    if first_number + second_number == third_number:
        print("it's a degenerated triangle")
    else:
        print("is not a degenerated triangle")


main()
