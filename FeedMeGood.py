

import mysql.connector
from tabulate import tabulate

class colors:
    DAY = GREEN = '\033[92m'
    MEAL_HEADER = BOLD = '\033[1m'
    MEAL = '\033[3m'
    RESET = '\033[0m'

def query_database(sql_query, return_response):
    try:
        sql_cursor = msql_connector.cursor()
        sql_cursor.execute(sql_query)
    except (MySQL.Error, MySQLdb.Warning) as error:
        print("Database error:" + error)
        return None
    
    if return_response == 1:
        result = sql_cursor.fetchall()
        return result

def choose_random_recipe(meal_type, no_meat):
    if no_meat==1:
        name = query_database("SELECT nazwa_przepisu FROM Przepis WHERE rodzaj='" + 
                               meal_type + 
                               "' AND bez_miesa=TRUE ORDER BY RAND () LIMIT 1", 1)
    else:
        name = query_database("SELECT nazwa_przepisu FROM Przepis WHERE rodzaj='" + 
                               meal_type + 
                               "' ORDER BY RAND () LIMIT 1", 1) 
    return str(name).strip("',[]()")


def print_recipe_details(recipe_name):
    print(colors.BOLD + "Szczegoly przepisu: " + colors.RESET + colors.GREEN + recipe_name + colors.RESET + "\n")
   
    table_to_print = []
    recipe_cost = 0
    recipe_calories = 0
    recipe_carbs = 0
    recipe_protein = 0
    recipe_fat = 0
    recipe_weight = 0

    recipe_ingredients = query_database("SELECT Produkt_Przepis.nazwa_produktu_fk, " +              #ingredient[0]
                                                "Produkt_Przepis.liczba_gramow_produktu, " +        #ingredient[1]
                                                "Produkt.cena_produktu_za_100g, " +                 #ingredient[2]
                                                "Produkt.kcal, " +                                  #ingredient[3]
                                                "Produkt.weglowodany, " +                           #ingredient[4]
                                                "Produkt.bialko, " +                                #ingredient[5]
                                                "Produkt.tluszcz " +                                #ingredient[6]
                                        "FROM Produkt_Przepis " +
                                        "JOIN Produkt " +
                                          "ON " + 
                                             "Produkt_Przepis.nazwa_produktu_fk=Produkt.nazwa_produktu " +
                                         "AND Produkt_Przepis.nazwa_przepisu_fk='" + recipe_name + "';", 1)
    
    for ingredient in recipe_ingredients:
        table_to_print.append([ingredient[0], ingredient[1], ingredient[2], ingredient[1]*ingredient[2]/100, ingredient[3], ingredient[1]*ingredient[3]/100, ingredient[4], ingredient[5], ingredient[6]])
        recipe_weight += ingredient[1]
        recipe_cost += ingredient[1]*ingredient[2]/100
        recipe_calories += ingredient[1]*ingredient[3]/100
        recipe_carbs += ingredient[4]
        recipe_protein += ingredient[5]
        recipe_fat +=  ingredient[6]
    
    result = [[str(recipe_calories), str(recipe_weight),str(recipe_carbs), str(recipe_protein), str(recipe_fat), str(recipe_cost)]] 
    print(tabulate(result, headers=['Kcal', 'Masa[g]', 'Węglowodany', 'Białko', 'Tłuszcz', 'Koszt[zł]']))
    
    return recipe_weight, recipe_cost, recipe_calories, recipe_carbs, recipe_protein, recipe_fat 


def print_ingredient_details(ingredient_name):  
    print(colors.BOLD + "Szczegóły produktu: " + colors.RESET + colors.GREEN + ingredient_name + colors.RESET)
    result = query_database("SELECT * FROM Produkt WHERE nazwa_produktu='" + ingredient_name + "';", 1)
    print(tabulate(result, headers=['Produkt', 'Kcal/100g', 'Węglowodany', 'Białko', 'Tłuszcz', 'zl/100g']))

def get_recipes_by_main_ingredient(main_ingredient):    
    result = query_database("SELECT nazwa_przepisu_fk FROM Produkt_Przepis WHERE nazwa_produktu_fk='" + 
                            main_ingredient + 
                            "' AND glowny_skladnik=TRUE", 1) 
    return result

def print_recipes_by_main_ingredient(main_ingredient):
    print(colors.BOLD + "\nWszystkie przepisy, których główny składnik to: " + colors.RESET + colors.GREEN + main_ingredient + colors.RESET)
    result = get_recipes_by_main_ingredient(main_ingredient)
    for recipe in result:
        print("\t" + str(recipe).strip("',[]()"))
    
def print_week_meal_plan():
    days=["PONIEDZIAŁEK", "WTOREK", "ŚRODA", "CZWARTEK", "PIĄTEK", "SOBOTA", "NIEDZIELA"]
    meals=["ŚNIADANIE", "II ŚNIADANIE", "OBIAD", "DESER", "KOLACJA"]

    days_details = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    day_details_table = []

    for day, day_details in zip(days, days_details):
        print(colors.DAY + colors.BOLD + "\t\t\t" +day + colors.RESET)
        for meal in meals:
            random_meal = choose_random_recipe(meal, 0)
            
            print(colors.MEAL_HEADER + meal + ": " + colors.RESET + 
                  colors.MEAL + random_meal + colors.RESET)
            
            day_details_table = print_recipe_details(random_meal)
            for index in range(len(day_details)):
                day_details[index] += day_details_table[index]
       
        print("")
        print(tabulate([day_details], headers = ['Waga[g]', 'Koszt[zł]', 'Kcal', 'Węglowodany', 'Białko', 'Tłuszcz']))   
        day_details = []
        print("\n")

def update_recipes_from_file(meal_type, no_meat):
    file_with_recipes = open("db_recipes_update", "r") 
    for recipe in file_with_recipes:
        if no_meat==0:
            print(recipe.strip())
            query_database("INSERT INTO Przepis (nazwa_przepisu, rodzaj) " +
                            "VALUES ('" + recipe.strip() + "', '" + meal_type + "');", 0)
        
        else:
            query_database("INSERT INTO Przepis (nazwa_przepisu, rodzaj, bez_miesa) " +
                           "VALUES ('" + recipe.strip() + "', '" + meal_type + "', TRUE);", 0)

#def update_products_from_file():

### CONNECT TO DB ###
msql_connector = mysql.connector.connect(user='feedmeuser', password='pass', host='localhost', database='Jedzenie')

print_week_meal_plan()
#print_recipes_by_main_ingredient("Schab")
#print_recipe_details("Schab w sosie koperkowym")
#print_ingredient_details("Schab")
#update_recipes_from_file("obiad", 0)
### DISCONNECT FROM DB ###
msql_connector.close()
