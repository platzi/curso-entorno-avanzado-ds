import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def covid_time_series(df: pd.DataFrame):
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series")

def top_countries(df: pd.DataFrame, n: int, highlight: list):

    def highlight_color(value, highlight_values):

        if value in highlight_values:
            return "red"
        return "lightblue"

    top_countries_df = (
        df
        .select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(n)
        .transform_column(
            column_name="country_region",
            function=lambda x: highlight_color(x, highlight),
            dest_column_name="color"
        )
    )

    sns.barplot(
        data=top_countries_df,
        x="value",
        y="country_region",
        palette=top_countries_df.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");


