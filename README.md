# KKPlot
Python library to simplify and enhance the visualization of data trends.


# Available Plots
## Trend with IQR Function Documentation

The `trend_with_IQR` function is designed to visualize data trends, focusing on the Interquartile Range (IQR) across different values of a specified feature. It leverages Plotly for plotting and offers customizable parameters for detailed visualization.

### Parameters

- **data**: DataFrame containing your data.
- **x_feature**: Feature on the x-axis.
- **x_feature_type**: Type of `x_feature` ('str' for strings or 'numeric' for numerical values).
- **unique_x_labels**: Unique labels/values for `x_feature`. If set to 'auto', unique values are automatically determined.
- **y_feature**: Feature on the y-axis to analyze.
- **thresholds**: List of dictionaries defining threshold lines on the plot with keys 'y' (threshold value), 'name' (label), 'line_color', 'line_dash', and 'line_width'.
- **x_axis_title**: Title for the x-axis.
- **y_axis_title**: Title for the y-axis.
- **y_axis_range**: Range for the y-axis as [min, max].
- **title**: Title of the plot.
- **show_image**: Boolean indicating whether to display the plot.
- **save_image**: Boolean indicating whether to save the plot as an image file.
- **scale**: Scale factor for the image (if `save_image` is True).
- **folder_path**: Folder path to save the image (if `save_image` is True).
- **plot_name**: Name of the file for the saved plot (if `save_image` is True).

### Functionality

1. **Data Preparation**: Filters and aggregates the data to calculate lower quartile, median, and upper quartile values for each unique label/value of `x_feature`.

2. **Plot IQR**: Plots the upper and lower quartiles as lines, with the area between these lines filled, representing the IQR. Medians are plotted with markers, lines, and texts, showing the central tendency for each group.

3. **Threshold Lines**: Allows plotting of horizontal threshold lines across the chart, defined by `thresholds`, to indicate specific values of interest. Labels for these lines are placed accordingly.

4. **Customization**: Supports customization of the plot's appearance with parameters for axis titles, axis ranges, the overall title, and legend positioning. Also, supports scaling and saving the plot as an image.

5. **Display or Save**: Based on `show_image` and `save_image` flags, either displays the plot in an output cell or saves it to a specified path.

### Example Use Case

This function is particularly useful for visualizing the distribution and central tendency of a variable (`y_feature`) across different groups or over time (`x_feature`). It's beneficial for identifying trends, outliers, and variations within the data, making it a valuable tool in exploratory data analysis, reporting, or presenting data insights.
