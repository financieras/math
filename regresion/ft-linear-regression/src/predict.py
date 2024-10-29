import json

# load json file with theta values
try:
    with open('src/theta.json') as file:
        data = json.load(file)

    theta0 = float(data["theta0"])
    theta1 = float(data["theta1"])
except:
    print("\033[2;30mNotice: Could not read json file. Reverting to default values.\033[0m")
    theta0 = 0
    theta1 = 0


def estimatePrice(mileage:int):
    estimatedPrice = theta0 + (theta1 * mileage)
    return estimatedPrice


if __name__ == '__main__':
    milage = None

    # input user for milage value
    while milage == None:
        try:
            milage = int(input("\033[0;34mPlease enter the milage of the car: \033[0m"))
            if milage < 0:
                milage = None
                raise Exception("")
        except:
            print("\033[0;31mInvalid input. Please try again\033[0m")

    price = round(estimatePrice(milage), 2)
    print("_"*20)
    print(f"\033[0;34mFor the milage you entered:\n\033[0;33m{milage} KM\n\033[0;34mThe estimated price is:\n\033[0;33m{price} €\033[0m")
