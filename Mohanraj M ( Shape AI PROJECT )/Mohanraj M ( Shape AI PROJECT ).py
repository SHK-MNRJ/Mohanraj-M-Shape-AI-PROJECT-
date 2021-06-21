import requests

api_key='fc3b6f9bb77e520e6125e2341e6e12c4'
place=input("Enter your City name:")

full_api_link="https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid="+api_key
api_link=requests.get(full_api_link)
api_data=api_link.json()

kelvin=273.15
temperature_of_city=((api_data['main']['temp'])-kelvin)
weather_description=api_data['weather'][0]['description']
humidity=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']

print("*****************************************************")
print("Weather report for the location of {}".format(place.upper()))
print("*****************************************************")

print("This Below printing statements are for testing process")
print("\n")
print(temperature_of_city)
print(weather_description)
print(humidity)
print(wind_speed)
print("\n")

r=open('report.txt','a')

temp=str(temperature_of_city)
wd=str(weather_description)
hum=str(humidity)
ws=str(wind_speed)
print("The fetched data's are uploaed to the file named report.txt")
print("\n")
r.write("Current temprature is: ")
r.write(temp+"deg in C \n")
r.write("Current weather_description is: ")
r.write(wd+"\n")
r.write("Current humidity is: ")
r.write(hum+"% \n")
r.write("Current wind_speed is: ")
r.write(ws+"kmph \n")
print("Printing completed , Check out the file report.txt in this same location")
r.close()
