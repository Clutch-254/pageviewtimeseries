import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Register matplotlib converters for date plotting
register_matplotlib_converters()

# Import data (df)
# Use a relative path assuming the file is in the same directory or accessible
# Replace the placeholder path if needed
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean the data
# Calculate the 2.5th and 97.5th percentiles
bottom_limit = df["value"].quantile(0.025)
top_limit = df["value"].quantile(0.975)

# Filter the data
df = df[
    (df["value"] >= bottom_limit)
    & (df["value"] <= top_limit)
]

def draw_line_plot():
    """
    Draws a line chart of daily page views.
    """
    # Use a copy of the original dataframe
    df_line = df.copy()

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot the data
    ax.plot(df_line.index, df_line["value"], color="red", linewidth=1)

    # Set labels and title
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't modify this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    """
    Draws a bar chart of average daily page views per month grouped by year.
    """
    # Copy and prepare data for the bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Calculate average daily page views for each month grouped by year
    df_grouped = (
        df_bar.groupby(["year", "month"])["value"].mean().unstack()
    )

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 7))

    # Plot the data
    df_grouped.plot(kind="bar", ax=ax)

    # Set labels and title
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Set legend details
    month_names = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    ax.legend(title="Months", labels=month_names)

    # Save image and return fig (don't modify this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    """
    Draws two adjacent box plots for year-wise and month-wise data distribution.
    """
    # Copy and prepare data for the box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["Year"] = df_box["date"].dt.year
    df_box["Month"] = df_box["date"].dt.strftime("%b") # Abbreviated month name

    # Order of months for correct plotting
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    # Create the figure and axes for the two plots side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(20, 7))

    # --- First Box Plot: Year-wise (Trend) ---
    sns.boxplot(
        x="Year", y="value", data=df_box, ax=axes[0],
        palette="viridis" # Optional: add a nice color palette
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # --- Second Box Plot: Month-wise (Seasonality) ---
    sns.boxplot(
        x="Month", y="value", data=df_box, ax=axes[1],
        order=month_order,
        palette="plasma" # Optional: add a nice color palette
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't modify this part)
    fig.savefig('box_plot.png')
    return fig

