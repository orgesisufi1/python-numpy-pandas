import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("token_key") 
api_url = os.getenv('base_url')


def fetch_api(token, from_currency, to_currency, append_values):
    try:
        response = requests.get(f'{api_url}{token}/latest/{from_currency}')
        respond = response.status_code
        if respond == 200:
            data = response.json()
            return append_values.append(data['conversion_rates'][from_currency]), append_values.append(data['conversion_rates'][to_currency])
        elif respond == 400:
            print(respond, 'Bad Request: Invalid Argument!')
        elif respond == 403:
            print(respond, '403 Forbidden: Permission denied or Invalid API KEY')
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



def convertCurrencties():
    print("Hello. Welcome to my Currency Convertor")
    while True: 
        currency_values = [ ]
        try:
            from_curr = input("Which currency do you want to convert from: ").strip().upper()
            to_curr = input("To which currency do you want to convert to: ").strip().upper()
            ammount = float(input("Can you please tell me the ammount that you want to convert: "))
            exchange = fetch_api(key, from_curr, to_curr, currency_values)
            if exchange:
                print(f"The rate between {from_curr} to {to_curr} is: {currency_values[0], currency_values[1]}")
                final_value = currency_values[1] * ammount
                print(f"{ammount} {from_curr} in {to_curr} today is: {format(final_value, '.2f')} {to_curr}")
            else:
                print("Please write the input properly with existing currencies!")
        except ValueError as e:
            print("Insert valid value: ", e)
        except PermissionError as e:
            print("Permission error: ", e)
        except TimeoutError as e:
            print("Timeout error", e)
        except ConnectionError as e:
            print("Connection error: ", e)

        another_convertion = input("Do you want to make another conversion? (yes/no): ").lower()
        if another_convertion != 'yes':
            print("Thank you for using my currency converter. Have a good day!")
            break

convertCurrencties()