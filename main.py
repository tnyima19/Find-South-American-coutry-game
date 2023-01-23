import turtle
import pandas as pd


def get_moouse_click_coor(x,y):
    print(x,y)

def printMissingCountries(missing_countries, data):
    for country in missing_countries:
        t= turtle.Turtle()
        t.penup()
        missing_country_location = data[data.countries == country]
        t.goto(int(missing_country_location.x), int(missing_country_location.y))
        t.write(country)
        

def check_if_country_exists(name_of_country, list_of_countries, named_countries, data):
    #print(data)
    print(name_of_country)
    if name_of_country in list_of_countries:
        named_countries.append(name_of_country)
        print("I am here")
        t = turtle.Turtle()
        #t.hideturtle()
        t.penup()
        country_location = data[data.countries == name_of_country ]
        t.goto(int(country_location.x), int(country_location.y))
        t.write(name_of_country)
        

def missedStates(list_of_countries, named_country, missing_countries):
    
    missing_countries = [country for country in list_of_countries if country not in named_country]  
    missing_countries_data = pd.DataFrame(missing_countries)
    missing_countries_data.to_csv("CountriesToLearn.csv")
    return missing_countries
    
            
    
def main():       
    screen = turtle.Screen()
    screen.title("U.S States Game")
    image = "samerica.gif"
    screen.addshape(image)
    named_countries = []
    turtle.shape(image)
    missing_countries = []

    data = pd.read_csv("countries.csv")
    list_of_countries = data["countries"].tolist()
    type(list_of_countries)
    #print(list_of_states)


    while(len(named_countries) < 14):
        country_answer = screen.textinput(title=f"{len(named_countries)}/ 14 countries", prompt="What's another country's name?" ).title()
        if country_answer == "Exit":
            break
        check_if_country_exists(country_answer, list_of_countries, named_countries, data)



    #States to learn 
    missing_countries = missedStates(list_of_countries, named_countries, missing_countries)
    printMissingCountries(missing_countries, data)
    print(missing_countries)
    
    screen.exitonclick()
    return 0

main()

