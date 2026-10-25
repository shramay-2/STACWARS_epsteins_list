# Solar Radiation Data Analysis (PS:2)

A Python-based exploratory data analysis project using
`SolarPrediction.csv`. The project investigates how measured solar
radiation varies with temperature, humidity, wind speed, and time of
day. It uses Pandas for data preparation and summarisation, and
Matplotlib for visualisation.

## Objectives

-   Explore the relationship between solar radiation and weather
    variables.
-   Compare full-day observations with daytime-only observations.
-   Visualise the daily pattern of solar radiation.
-   Use grouped median values to make the central trends easier to
    interpret.
-   Identify notable patterns, variation, and potential outliers.

## Dataset

The project uses `SolarPrediction.csv`.

Important columns used include:

-   `Radiation` --- measured solar radiation.
-   `Temperature` --- temperature in Fahrenheit.
-   `Humidity` --- humidity percentage.
-   `Speed` --- wind speed in miles per hour.
-   `Data` / `Date` and `Time` --- date and time information used to
    construct timestamps.

The dataset file should be kept in the project directory alongside the
Python scripts.

## Requirements

-   Python 3
-   Pandas
-   Matplotlib

Install the libraries with:

``` bash
pip install pandas matplotlib
```

## Project files

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `SolarPrediction.csv`               Source dataset

  `data_cleaner.py`                   Loads the CSV, renames and formats
                                      the date column, creates a combined
                                      `DateTime` column, groups rows by
                                      date, and creates the daytime-only
                                      subset

  `rad_vs_envvar.py`                  Creates scatter plots with median
                                      trend lines for radiation against
                                      temperature, humidity, and wind
                                      speed; compares full-day and
                                      daytime-only data

  `rad_vs_time_plot.py`               Plots radiation observations by
                                      time of day and calculates the time
                                      label with the highest grouped
                                      median radiation

  `daily_avg_rad.py`                  Calculates and plots mean daytime
                                      radiation for each date

  `task3.py`                          Calculates daily mean and maximum
                                      radiation, identifies the date and
                                      weather conditions of the maximum
                                      reading, and lists the five dates
                                      with the highest daily maximum

  `Data visualisation report.pdf`     Report containing the project's
                                      visualisations and written analysis
  -----------------------------------------------------------------------

## Methodology

### 1. Data preparation

`data_cleaner.py` loads the CSV using Pandas. The source date column is
renamed from `Data` to `Date`, the date is formatted consistently, and
the date and time strings are combined into a `DateTime` column.

The script also creates:

-   `grouped`: rows grouped by date.
-   `day_only`: observations strictly after 06:00 and strictly before
    18:00.

The daytime subset is used to compare relationships without the large
number of near-zero radiation readings that occur overnight.

### 2. Weather-variable comparisons

`rad_vs_envvar.py` produces plots for:

-   Temperature vs radiation.
-   Humidity vs radiation.
-   Wind speed vs radiation.

For each variable, the script displays individual observations as a
scatter plot and overlays a median line. The scatter points show the
spread of measurements, while the grouped median provides a clearer view
of the typical radiation value at each recorded variable value.

Each relationship is shown for both the complete dataset and the
daytime-only subset. Comparing the two helps show how nighttime
observations affect the apparent patterns.

### 3. Radiation over time

`rad_vs_time_plot.py` plots individual radiation measurements against
time of day. It rounds timestamps to five-minute intervals, groups the
observations by the resulting time-of-day value, and calculates median
radiation for each group. This is intended to show both variation across
observations and the typical daily radiation pattern.

### 4. Daily summaries

`daily_avg_rad.py` calculates the mean radiation for each date using
daytime observations.

`task3.py` calculates daily mean and maximum radiation, retrieves the
date and weather-variable values associated with the highest individual
radiation reading, and identifies the five dates with the highest daily
maximum radiation.

## Running the scripts

Run commands from the project directory so the scripts can find
`SolarPrediction.csv`.

``` bash
python rad_vs_envvar.py
python rad_vs_time_plot.py
python daily_avg_rad.py
python task3.py
```

`data_cleaner.py` is imported by the other scripts and can also be run
directly to inspect the prepared data.

## Key interpretation points

-   Temperature generally shows a positive association with solar
    radiation, especially when looking at daytime observations.
-   The spread of scatter points indicates that temperature alone does
    not explain radiation levels.
-   Full-day plots include nighttime observations with near-zero
    radiation, which can alter the apparent relationship between
    variables.
-   Radiation typically rises after sunrise, reaches higher values
    around the middle of the day, and declines towards sunset.
-   Humidity and wind-speed relationships should be interpreted
    cautiously because the points are widely spread and some ranges may
    contain fewer observations.
-   Correlation does not establish causation. The plots show
    associations, not proof that one variable directly causes another.

## Notes

-   The daytime filter uses strict comparisons: observations exactly at
    06:00 or 18:00 are excluded.
-   The scripts use the column name `Speed` for wind speed.
-   Visual patterns and potential outliers should be verified against
    the original rows before treating any measurement as an error.
