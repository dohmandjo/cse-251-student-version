"""
Course: CSE 251 
Lesson: L02 Prove
File:   prove.py
Author: Joel Doh

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py" and leave it running.
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the description of the assignment.
  Note that the names are sorted.
- You are required to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a separate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here
class thread_class(threading.Thread):
    
    def __init__(self, url):
        threading.Thread().__init__()
        self.url = url
        self.response={}
        self.status_code={}

    def run(self):
        global call_count
        response = requests.get(self.url)
        if response.status_code==200:
          self.response=response.json()
          call_count += 1
        else:
            print(response.status_code)

# TODO Add any functions you need here
def response_storage(api_dict, key):
    for x in api_dict:
        return thread_class(key)

def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    # TODO Retrieve Top API urls
    api_response = requests.get(TOP_API_URL)
    top_api_data = api_response.json()

    api_top = thread_class(TOP_API_URL) 
    api_top.start()
    api_top.join()

    # print_dict(top.response)
    film6 = thread_class(api_top.response["films"] + "6") 
    film6.start()
    film6.join()
    # TODO Retrieve Details on film 6

    response_film6=film6.response
    threads=[]
    for x in response_storage(response_film6,'characters'):
      threads.append(x)
    char_len = len(threads)  
    for x in response_storage(response_film6,'planets'):
      threads.append(x)
    plan_len = len(threads)
    for x in response_storage(response_film6,'starships'):
      threads.append(x)
    star_len = len(threads)  
    for x in response_storage(response_film6,'vehicles'):
      threads.append(x)
    veh_len = len(threads)
    for x in response_storage(response_film6,'species'):
      threads.append(x)
    spec_len = len(threads)
    # Create and start the film thread

    for t in threads:
       t.start()
    for t in threads:
       t.join()

    characters=[x.response['name'] for x in threads[:char_len ]]
    planets=[x.response['name'] for x in threads[char_len :plan_len]]
    starships=[x.response['name'] for x in threads[plan_len:star_len]]
    vehicles=[x.response['name'] for x in threads[star_len:veh_len]]
    species=[x.response['name'] for x in threads[veh_len:spec_len]]

    #Sorting the lists
    characters.sort()
    planets.sort()
    starships.sort()
    vehicles.sort()
    species.sort()

    # TODO Display results
    log.write("----------------------------------------")
    log.write(f'Title   : {(response_film6['title'])}')
    log.write('Director: {}'.format(response_film6['director']))
    log.write('Producer: {}'.format(film6['producer']))
    log.write('Released: {}'.format(film6['release_date']))

    log.write('')

    log.write("Characters: {}".format(len(characters)))
    log.write(", ".join(characters))
    
    log.write('')

    log.write("Planets: {}".format(len(planets)))
    log.write(", ".join(planets))

    log.write('')

    log.write("Starships: {}".format(len(starships)))
    log.write(", ".join(starships))

    log.write('')

    log.write("Vehicles: {}".format(len(vehicles)))
    log.write(", ".join(vehicles))

    log.write('')

    log.write("Species: {}".format(len(species)))
    log.write(", ".join(species))

    log.write('')

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')
    

if __name__ == "__main__":
    main()