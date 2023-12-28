import requests
import time
import datetime

url = "https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/NadAr"
api_key = "RGAPI-eb7d8522-5ed5-4aa5-9346-fe61a9d8bbe6"

def get_user():

    get_summoner_url = url + "?api_key=" + api_key

    response = requests.get(get_summoner_url)

    return response.json()

def get_time_slice():
    
    timestamp = []
    dates = (["01/12/2021","14/12/2021"],["14/12/2021","28/12/2021"],
             ["28/12/2021","14/01/2022"],["14/01/2022","28/01/2022"],
             ["28/01/2022","14/02/2022"],["14/02/2022","28/02/2022"],
             ["28/02/2022","14/03/2022"],["14/03/2022","28/03/2022"],
             ["28/03/2022","14/04/2022"],["14/04/2022","28/04/2022"],
             ["28/04/2022","14/05/2022"],["14/05/2022","28/05/2022"],
             ["28/05/2022","14/06/2022"],["14/06/2022","28/06/2022"],
             ["28/06/2022","14/07/2022"],["14/07/2022","28/07/2022"],
             ["28/07/2022","14/08/2022"],["14/08/2022","28/08/2022"],
             ["28/08/2022","14/09/2022"],["14/09/2022","28/09/2022"],
             ["28/09/2022","14/10/2022"],["14/10/2022","28/10/2022"],
             ["28/10/2022","14/11/2022"],["14/11/2022","28/11/2022"],
             ["28/11/2022","14/12/2022"],["14/12/2022","31/12/2022"],             
             ["14/01/2023","28/01/2023"],
             ["28/01/2023","14/02/2023"],["14/02/2023","28/02/2023"],
             ["28/02/2023","14/03/2023"],["14/03/2023","28/03/2023"],
             ["28/03/2023","14/04/2023"],["14/04/2023","28/04/2023"],
             ["28/04/2023","14/05/2023"],["14/05/2023","28/05/2023"],
             ["28/05/2023","14/06/2023"],["14/06/2023","28/06/2023"],
             ["28/06/2023","14/07/2023"],["14/07/2023","28/07/2023"],
             ["28/07/2023","14/08/2023"],["14/08/2023","28/08/2023"],
             ["28/08/2023","14/09/2023"],["14/09/2023","28/09/2023"],
             ["28/09/2023","14/10/2023"],["14/10/2023","28/10/2023"],
             ["28/10/2023","14/11/2023"],["14/11/2023","28/11/2023"],
             ["28/11/2023","14/12/2023"],["14/12/2023","31/12/2023"])
    
    for date in dates:
        start_date = round(time.mktime(datetime.datetime.strptime(date[0], "%d/%m/%Y").timetuple()))
        end_date = round(time.mktime(datetime.datetime.strptime(date[1], "%d/%m/%Y").timetuple()))
        timestamp.append([start_date,end_date])
    
    return timestamp
def get_matches():
    
    timestamp = get_time_slice()
    summoner = get_user()
    puuid = summoner['puuid']
    

    for slice in timestamp:
        get_100_matches_url = f"https://ru.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={slice[0]}&endTime={slice[1]}&type=ranked&start=0&count=100"
        print(get_100_matches_url)
        response = requests.get(get_100_matches_url)
        print(response.json())

get_matches()
