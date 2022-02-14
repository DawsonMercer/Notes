
def check_province(province_dict):
    while True:
        postal_code = input("Enter postal code: ")
        if postal_code[0].isalpha():
            postal_code = postal_code.upper()
            postal_key = postal_code[0]
            urban_or_rural = postal_code[1]
            if postal_key in province_dict:
                province = province_dict[postal_key]
                print(f"The province is: {province}")
                if urban_or_rural == "0":
                    print("Postal Code is: rural.")
                    break
                else:
                    print("Postal Code is: urban")
                    break
            else:
                print(f"{postal_code} is not a postal code. Try again!\n")
        else:
            print("Please enter correct postal code format. Ex: A1A 1A1\n")


def main():
    print("Postal Code - Question 1\n")
    province_dict = {"A": "Newfoundland",
                     "B": "Nova Scotia",
                     "C": "Prince Edward Island",
                     "E": "New Brunswick",
                     "G": "Quebec",
                     "H": "Quebec",
                     "J": "Quebec",
                     "K": "Ontario",
                     "L": "Ontario",
                     "M": "Ontario",
                     "N": "Ontario",
                     "P": "Ontario",
                     "R": "Manitoba",
                     "S": "Saskatchewan",
                     "T": "Alberta",
                     "V": "British Colombia",
                     "X": "Nunavut or Northwest Territories",
                     "Y": "Yukon"}
    choice = "y"
    while choice.lower() == "y":
        check_province(province_dict)
        choice = input("\nLook up another postal code? (y/n) ")
    print("Bye!")


if __name__ == "__main__":
    main()