from pprint import pprint

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def make_coffe(cash_1):

    a = input("What would you like? (espresso/latte/cappuccino):")
    if str(a) == "cappuccino":
        cash = process_cash()
        if float(cash) == float(MENU["cappuccino"]["cost"]):
            print("Enjoy your coffe")
            print("Your change is 0 USD")
            resources["water"] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 24
            make_coffe(0)
        elif float(cash) > float(MENU["cappuccino"]["cost"]):
            cash_1 = float(cash_1) + (float(cash) - float(MENU["cappuccino"]["cost"]))
            print("Enjoy your coffe")
            print("Your change is {} USD".format(cash_1))
            if  resources["water"] > 250 and resources["milk"] > 100 and resources["coffee"] >24:
                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24
                make_coffe(cash_1)
            else:
                print("sorry not enough resources")
                make_coffe(cash_1)
        else:
            cash_1 = float(cash_1) + float(cash)
            print("“Sorry that's not enough money. {} USD refunded".format(cash_1))
            make_coffe(cash_1)


    elif str(a) == "espresso":
        cash = process_cash()
        if float(cash) == float(MENU["espresso"]["cost"]):
            print("Enjoy your coffe")
            print("Your change is 0 USD")
            resources["water"] -= 50
            resources["coffee"] -= 18
            make_coffe(0)
        elif float(cash) > float(MENU["espresso"]["cost"]):
            cash_1 = float(cash_1) + (float(cash) - float(MENU["espresso"]["cost"]))
            print("Enjoy your coffe")
            print("Your change is {} USD".format(cash_1))
            if resources["water"] >= 50 and resources["coffee"] > 18:
                resources["water"] -= 50
                resources["coffee"] -= 18
                make_coffe(cash_1)
            else:
                print("sorry not enough resources")
                make_coffe(cash_1)
        else:
            cash_1 = float(cash_1) + float(cash)
            print("“Sorry that's not enough money. {} USD refunded".format(cash_1))
            make_coffe(cash_1)


    elif str(a) == "latte":
            cash = process_cash()
            if float(cash) == float(MENU["latte"]["cost"]):
                print("Enjoy your coffe")
                print("Your change is 0 USD")
                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24
                make_coffe(0)
            elif float(cash) > float(MENU["latte"]["cost"]):
                cash_1 = float(cash_1) + (float(cash) - float(MENU["latte"]["cost"]))
                print("Enjoy your coffe")
                print("Your change is {} USD".format(cash_1))
                if resources["water"] > 200 and resources["coffee"] > 24 and resources["milk"] > 150:
                    resources["water"] -= 200
                    resources["coffee"] -= 24
                    resources["milk"] -=150
                    make_coffe(cash_1)
                else:
                    print("sorry not enough resources")
                    make_coffe(cash_1)
            else:
                cash_1 = float(cash_1) + float(cash)
                print("“Sorry that's not enough money. {} USD refunded".format(cash_1))
                make_coffe(cash_1)






    elif str(a) == "off":
        print("Turning off")
    elif str(a) == "report":
        a=call_report()
        a.append("Cash: "+ str(cash_1) +" USD")
        for i in a:
            print(i)
        make_coffe(cash_1)
    elif str(a) == "quit":
        print("See you next time, here is you refund {} USD".format(cash_1))
        print("Next customer")
        make_coffe(0)


def process_cash():
    cash = 0
    print("Please insert coins.")
    a = input("quaters?")
    a = int(a) * 0.25
    cash += a
    b = input("dimes?")
    b = int(b) * 0.1
    cash += b
    c = input("nickles?")
    c = int(c) * 0.05
    cash += c
    d = input("pennies?")
    d = int(d) * 0.01
    cash += d
    return cash

def call_report():
    a = ["Water: "+str(resources["water"])+"ml",
          "Milk: "+str(resources["milk"])+"ml",
          "Coffe: "+str(resources["coffee"])+"g"]
    return a

make_coffe(0)