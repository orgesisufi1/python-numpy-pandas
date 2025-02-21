import requests 
import os
import json
import csv
from dotenv import load_dotenv
dirname = os.path.dirname(__file__)
json_file = os.path.join(dirname, 'weather.json')
csv_file = os.path.join(dirname, 'weather.csv')
load_dotenv()
url = os.getenv('api_url')
key = os.getenv('api_key')

def fetchWeather(api, cityName):
    api = f"{url}{cityName}&appid={key}&units=metric"
    try:
        response = requests.get(api)
        respond = response.status_code
        if respond == 200:
            data = response.json()
            return data
        elif respond == 400:
                print(respond, 'Bad Request: Invalid Argument!')
        elif respond == 403:
            print(respond, 'Forbidden: Permission denied or Invalid API KEY')
        elif respond == 429:
            print(respond, 'Resource Exhausted: Either out of resource quota or reaching rate limiting.')
        elif respond == 500:
            print(respond, 'Internal Server Error: Internal server error (retry your request).')
        elif respond == 503:
            print(respond, 'Service Unavailable.')
        elif respond == 504:
            print(respond, 'Gateway Timeout: Retry your request.')
        else:
            print("Error, please check input")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f'Failed to connect API: {e}')


def getWeatherByCity():
    data = [ ]
    while True:
        try:
            city_input = input("Please enter the name of the city that you want to see the weather: ").strip().lower()
            api = f"{url}{city_input}&appid={key}&units=metric"
            data = fetchWeather(api, city_input)
            city_details = f"{data['name']}, {data['sys']['country']}"
            weather_details = f"Weather: {data['weather'][0]['main']}, {data['weather'][0]['description']}, {data['main']['temp']} Celcius"
            print(f"City Details:{city_details},\n{weather_details} \n")
            store_data = input("Do you want to store this data into a json/csv file? (yes/no): ").strip().lower()
            if store_data == 'yes':
                choose_file = input("Where do you want to store the data? (json/csv): ").strip().lower()
                if choose_file == 'json':
                    weather_info = {
                        'city_name': data['name'],
                        'country': data['sys']['country'],
                        'weather': data['weather'][0]['main'],
                        'description': data['weather'][0]['description'],
                        'temp': data['main']['temp']
                    }

                    try:
                        with open(json_file, 'r') as f:
                            json_data = json.load(f)
                    except FileNotFoundError as e:
                        print("File not found! ", e)

                    json_data['weather'].append(weather_info)

                    with open(json_file, 'w') as f:
                        json.dump(json_data, f, indent=4)
                
                elif choose_file == 'csv':
                    weather_info = (data['name'],data['sys']['country'], data['weather'][0]['main'],data['weather'][0]['description'], data['main']['temp'])
                    try:
                        with open(csv_file, 'a') as f:
                            csv_writer = csv.writer(f)
                            csv_writer.writerow(weather_info)
                    except FileNotFoundError as e:
                        print("File not found! ", e)
                else:
                    print("Incorrect file format input")
        except ValueError as e:
                print("Insert valid value: ", e)
        except PermissionError as e:
            print("Permission error: ", e)
        except TimeoutError as e:
            print("Timeout error", e)
        except ConnectionError as e:
            print("Connection error: ", e)
        except TypeError as e:
            print("Please input a valid city name! ", e)
        


        another_weather = input("Do you want to check the weather again? (yes/no): ").lower()
        if another_weather != 'yes':
            print("Thank you for using this weather API. See you later!")
            break

getWeatherByCity()

# The API does not support date range queries, so I’ll explain how I would approach this task if such a feature were available.

# I would create a function that prompts the user to input a start date and an end date. These inputs would be included in the API request, formatted as follows:
# f"{url}{city_input}{start_date}{end_date}&appid={key}&units=metric".

# Ideally, the API response would provide a concise summary for each day in the range, including the city name, country, temperature, and weather description.

# If the data set is large due to an extended date range, I would handle it in one of two ways:

# Display the weather details for each day within the range.
# Calculate the average temperature over the range and identify the most frequent weather condition during that period.
