import pandas as pd

data = pd.read_csv("./location_finder.csv")

# id = id of the car
# origin = (latitute,longitude)
# pit_stops = [(latitute,longitude), (latitute,longitude), ..]
# destination = (latitute,longitude)
output_data = pd.DataFrame(columns=['id','origin','pit_stops','destination'])

for id in list(set(data['id'].values)):
    temp_data = data[data["id"] == id]
    origin = None
    destination = None
    pit_stops = list()
    if temp_data.iloc[0]['speed'] == 0:
        origin = (temp_data.iloc[0]['latitude'],temp_data.iloc[0]['longitude'])
    if temp_data.iloc[0]['speed'] == 0:
        destination = (temp_data.iloc[-1]['latitude'],temp_data.iloc[-1]['longitude'])
    for index, value in enumerate(temp_data['speed'].values[1:-2]):
        if value == 0:
            pit_stops.append((temp_data.iloc[index]['latitude'],temp_data.iloc[index]['longitude']))
    output_data = output_data.append(
                                pd.Series(
                                    [
                                        id,
                                        origin,
                                        list(set(pit_stops)),
                                        destination,
                                    ],
                                    index=output_data.columns,
                                ),
                                ignore_index=True,
                            )
output_data.to_csv(f"./{data['Date'].values[0]}.csv")
pass

