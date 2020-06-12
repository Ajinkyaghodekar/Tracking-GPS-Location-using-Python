import pandas as pd
import matplotlib.pyplot as plt
import mplleaflet

import get_route

data = pd.read_csv("./location_finder.csv")
output_data = pd.DataFrame(columns=['id','latitude','longitude','way'])
data =  data[:500]
for id in list(set(data['id'].values)):
    temp_data = data[data["id"] == id]
    for latitude, longitude in zip(temp_data['latitude'].values,temp_data['longitude'].values):
        lats, longs = get_route.get_coords(latitude,longitude)
        way = [(lat,lon) for lat,lon in zip(lats,longs)]
        output_data = output_data.append(
                                    pd.Series(
                                        [
                                            id,
                                            latitude,
                                            longitude,
                                            way,
                                        ],
                                        index=output_data.columns,
                                    ),
                                    ignore_index=True,
                                )
output_data.to_csv(f"./{data['Date'].values[0]}_way.csv")

plt.plot(output_data["longitude"], output_data["latitude"], 'b')
plt.plot(output_data["longitude"], output_data["latitude"], 'rs')

mplleaflet.show()

