# Useful Plotly Methods for Data Visualization

## Chart Creation
- **`plotly.express.line(data_frame, x, y)`**: Creates a line chart.
  - `data_frame`: Data source.
  - `x`: Data for the x-axis.
  - `y`: Data for the y-axis.
- **`plotly.express.bar(data_frame, x, y)`**: Creates a bar chart.
- **`plotly.express.scatter(data_frame, x, y)`**: Creates a scatter plot.
- **`plotly.express.pie(data_frame, names, values)`**: Creates a pie chart.
- **`plotly.express.histogram(data_frame, x)`**: Creates a histogram.

## Layout and Styling
- **`fig.update_layout(title, xaxis_title, yaxis_title)`**: Updates the layout and styling of the figure.
  - `title`: Title of the figure.
  - `xaxis_title`: Title of the x-axis.
  - `yaxis_title`: Title of the y-axis.
- **`fig.update_traces(marker, line, name)`**: Updates trace attributes like marker properties and line styles.
- **`fig.update_xaxes(tickangle, title_standoff)`**: Customizes x-axis properties.
  - `tickangle`: Angle of x-axis ticks.
  - `title_standoff`: Distance of axis title from the axis.

## Interactivity
- **`fig.show()`**: Displays the figure.
- **`plotly.io.write_html(fig, file)`**: Saves the figure as an HTML file.
- **`fig.add_trace(trace)`**: Adds a new trace to the figure.
- **`fig.add_vrect(x0, x1, fillcolor, opacity)`**: Adds a vertical shaded region to the figure.
  - `x0`, `x1`: Defines the x-axis range of the rectangle.
  - `fillcolor`: Color of the fill.
  - `opacity`: Opacity of the fill.

## Data Manipulation
- **`fig.data`**: Accesses the data traces of the figure.
- **`fig.layout`**: Accesses the layout settings of the figure.
- **`fig.update_frames(data)`**: Updates the frames for animations.

These methods are central to constructing, manipulating, and displaying different types of visualizations in Plotly, making it a versatile tool for data analysis and presentation.
