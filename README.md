# Tracking-GPS-Location-using-Python

Description:

To identify car GPS data from a GPS operator for cars moving in the area of a large city, for a five consecutive weekdays to identify car trips(Start place - Stop Place), Positioning of car location on roads.

The dataset is consists of Car_id, Latitude, Longitude, Heading, Speed, Date, and Time.

The first task is to identify the car trips means the staring location of a car and ending location of the car. Using the latitude and longitude points consider as a Pit_Stops to find the origin and destination of a car and it creates a new CSV file for Start place and Stop place of a car.

In the second part to position the car locations on roads. Created an algorithm for to find lost probable road segments of a car and its location. So, basically first create a get_route function code for to find a way of a car using latitude and longitude points and connect this code file with the location_finder1.py file. Then Run the get_route code file and location_finder1.py file to creates a map of a city where car moving from one location to another location.

Libraries used: Pandas, Matplotlib, mplleaflet, get route, Overpass API, Json.
