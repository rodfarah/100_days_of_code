import pandas as pd

# data = pd.read_csv("day_25/weather_data.csv")

# print(data)


# temp_list = data["temp"].to_list()

# print(data[data.temp == data.temp.max()])

# °F = (°C × 9/5) + 32


# test_dict = {"name": ["Rodrigo", "Pedro", "Paula", "Victorio"],
#              "idade": [47, 32, 38, 86],
#              "sexo": ["Masculino", "Masculino", "Feminino", "Masculino"]
#              }


# data = pd.DataFrame(test_dict)

# data.to_csv("day_25/new_file.csv")


data_frame = pd.read_csv("day_25/Central_Park_Squirrel_Census.csv")

colour_serie = data_frame["Primary Fur Color"]

gray_squirrels_count = len(
    data_frame[data_frame["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(
    data_frame[data_frame["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(
    data_frame[data_frame["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

result_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"], 
    "Count" : [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

final_data_frame = pd.DataFrame(result_dict)

print(final_data_frame)

final_data_frame.to_csv("/home/rofarah/Documents/TI/Code/100_days_of_code/day_25/squirrel_color_count.csv")
