from flask import Flask, request, render_template
from app.graphs import bp
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64


def plot_time_periods(data):
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    data['End Time'] = pd.to_datetime(data['End Time'])

    data_for_x_axis_ticks = pd.DataFrame(data['Start Time'].to_list() + data['End Time'].to_list())
    data_for_x_axis_ticks = pd.to_datetime(data_for_x_axis_ticks[0])
    data_for_x_axis_ticks.sort_values(inplace=True)

    plt.figure(figsize=(11, 4))
    plt.barh(range(len(data)), data['End Time'] - data['Start Time'], left=data['Start Time'])
    plt.xlim(data['Start Time'][0], data['End Time'][2])
    plt.xticks(data_for_x_axis_ticks)

    plt.xlabel('Time')
    plt.ylabel('Period')
    plt.title('Time Periods')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert the plot to base64 encoded image
    encoded_image = base64.b64encode(buffer.read()).decode('utf-8')

    # Close the plot to free up memory
    plt.close()

    return encoded_image


# Create a dummy DataFrame with start time and end time columns
data = pd.DataFrame({
    'Start Time': ['2022-01-01 09:00:00', '2022-01-01 12:30:00', '2022-01-01 14:45:00'],
    'End Time': ['2022-01-01 10:30:00', '2022-01-01 15:00:00', '2022-01-01 16:30:00']
})

# Call the plot_time_periods function with the dummy data
dummy_graph_to_show = plot_time_periods(data)


@bp.route("/graphs")
def show_graphs():
    return render_template("graphs/graphs.html", dummy_graph1=dummy_graph_to_show)
