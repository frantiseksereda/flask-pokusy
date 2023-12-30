import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import http.client
import json

data = pd.DataFrame({
    'Start Time': ['2022-01-01 09:00:00', '2022-01-01 12:30:00', '2022-01-01 14:45:00'],
    'End Time': ['2022-01-01 10:30:00', '2022-01-01 15:00:00', '2022-01-01 16:30:00']
})

start_times = data['Start Time'].to_list()
end_times = data['End Time'].to_list()
combined_times_list = start_times + end_times

print(combined_times_list)


combined_data = pd.DataFrame(combined_times_list)
combined_data = pd.to_datetime(combined_data[0])
combined_data.sort_values(inplace=True)


print(combined_data)

conn = http.client.HTTPSConnection("collectionapi.metmuseum.org")
payload = ''
headers = {}
conn.request("GET", "/public/collection/v1/departments", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
json_data = json.loads(data)
departments_df = pd.DataFrame(json_data['departments'])
print(departments_df)
