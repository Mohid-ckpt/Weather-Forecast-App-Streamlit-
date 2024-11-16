import requests

API_KEY = '6d7e19fa4c71fcb05fa50aab48c57e8c'

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    filtered_data = filtered_data[:8*forecast_days]
    return filtered_data

if __name__=="__main__":
    print(get_data(place='Tokyo', forecast_days=3))