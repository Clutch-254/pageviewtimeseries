# Page View Time Series Visualizer

A Python script that visualizes freeCodeCamp forum page views from May 2016 to December 2019. Creates three different charts to explore trends, patterns, and seasonality in the data.

## What It Does

This visualizer creates three complementary plots to help you understand page view patterns:

1. **Line Plot** - Shows daily page views over time to spot overall trends
2. **Bar Chart** - Displays average monthly page views grouped by year
3. **Box Plots** - Reveals year-to-year trends and month-to-month seasonality patterns

## Requirements

```bash
pip install matplotlib pandas seaborn
```

## Data Format

The script expects `fcc-forum-pageviews.csv` with two columns:
- `date` - Date in a parseable format
- `value` - Number of page views on that date

## Usage

```python
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Create a line chart of daily page views
draw_line_plot()  # Saves as 'line_plot.png'

# Create a bar chart of monthly averages by year
draw_bar_plot()  # Saves as 'bar_plot.png'

# Create box plots showing trends and seasonality
draw_box_plot()  # Saves as 'box_plot.png'
```

## Data Cleaning

Before any visualization, the script automatically cleans the data by removing outliers. It filters out the top and bottom 2.5% of page views to exclude:
- Days with suspiciously low traffic (possible downtime or data errors)
- Days with abnormally high spikes (possible bot traffic or data anomalies)

This gives you a cleaner picture of normal traffic patterns.

## The Three Visualizations

### Line Plot
A straightforward time series showing the raw (cleaned) daily page view data. Great for:
- Spotting long-term growth or decline
- Identifying sudden changes or anomalies
- Getting an overall sense of traffic patterns

### Bar Chart
Shows the average page views for each month, with bars grouped by year. This helps you:
- Compare how different months performed across years
- See if certain months consistently get more traffic
- Identify yearly growth patterns

### Box Plots
Two side-by-side box plots that reveal different patterns:

**Year-wise Box Plot (Trend)**
- Shows the distribution of daily page views for each year
- Helps identify overall growth trends
- Reveals if traffic is becoming more consistent or variable

**Month-wise Box Plot (Seasonality)**
- Shows the distribution of page views for each month (across all years)
- Identifies seasonal patterns (e.g., do certain months always have higher traffic?)
- Shows which months have the most variable traffic

## What You Can Learn

- **Growth trends**: Is the forum getting more popular over time?
- **Seasonal patterns**: Do page views spike during certain months (maybe when people are learning more)?
- **Consistency**: Is traffic becoming more stable or more unpredictable?
- **Outliers**: Which specific days or months had unusual traffic?

## Output Files

All three functions save PNG images and return figure objects:
- `line_plot.png` - Daily page view trend line
- `bar_plot.png` - Monthly averages by year
- `box_plot.png` - Year-wise and month-wise distributions

## Customization Ideas(might do em later)

Feel free to adjust:
- **Outlier thresholds**: Currently removes bottom/top 2.5%, but you can change this
- **Colors**: Both box plots use color palettes (viridis and plasma) that can be changed
- **Figure sizes**: Adjust figsize parameters for different dimensions
- **Date ranges**: Filter the data to focus on specific time periods

## Tips

- The line plot shows raw trends, while the bar chart smooths them out by averaging
- Box plots are great for spotting outliers (those dots outside the whiskers)
- If you see a box plot with a very tall box, that means high variability
- Compare the two box plots to distinguish between yearly growth and monthly patterns

Perfect for understanding web traffic patterns, learning time series visualization, or just exploring how freeCodeCamp's forum grew over time!
