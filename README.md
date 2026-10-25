# STAC WARS --- Team Submission

This repository contains the team's work for three STAC WARS problem
statements:

-   **PS1 --- OpenRocket Extraterrestrial Flight Design**
-   **PS2 --- Solar Radiation Analysis and Prediction**
-   **PS4 --- Product Ideathon: Mining the Asteroid Belt**

Each problem statement is stored in its own folder.

## Repository Structure

``` text
STACWARS/
├── README.md
├── PS1/
│   ├── final_epstein's_rocket.zip
│   │   ├── rocket.ork
│   │   ├── simulations.csv
│   │   └── decals/
│   │       └── epstein.png.jpeg
│   └── rocket report.pdf
├── PS2/
│   ├── SolarPrediction.csv
│   ├── data_cleaner.py
│   ├── rad_vs_envvar.py
│   ├── rad_vs_time_plot.py
│   ├── daily_avg_rad.py
│   ├── task3.py
│   └── Data visualisation report.pdf
└── PS4/
    └── ProdIdeathon by Epstein List.pptx
```

The tree above lists the main project files found in the submitted ZIP.
The PS1 OpenRocket project is currently packaged inside
`final_epstein's_rocket.zip`.

## PS1 --- OpenRocket Extraterrestrial Flight Design

**Goal:** Design and simulate a two-stage sounding rocket for the
fictional planet Mustafar using OpenRocket.

**Files included:** - `final_epstein's_rocket.zip` --- contains
`rocket.ork` and its decal asset. - `rocket report.pdf` --- the rocket
design report.

The PS1 brief specifies a final editable OpenRocket project and a
report. It also asks for exported flight simulation data in CSV format.
A separate flight-data CSV was not present in the ZIP structure I
inspected, so include it if it has been generated and is required for
your final submission.

To inspect the rocket design, extract `final_epstein's_rocket.zip` and
open `rocket.ork` in OpenRocket.

## PS2 --- Solar Radiation Analysis and Prediction

**Goal:** Explore how solar radiation varies over time and how it
relates to environmental variables in `SolarPrediction.csv`.

### Files

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `SolarPrediction.csv`               Source dataset

  `data_cleaner.py`                   Loads the CSV, standardises the
                                      date column, creates a combined
                                      `DateTime` column, groups
                                      observations by date, and creates a
                                      daytime-only subset

  `rad_vs_envvar.py`                  Plots radiation against
                                      temperature, humidity, and wind
                                      speed for both full-day and
                                      daytime-only observations, using
                                      scatter points and median lines

  `rad_vs_time_plot.py`               Plots radiation against time of day
                                      and calculates the time label with
                                      the highest grouped median
                                      radiation

  `daily_avg_rad.py`                  Calculates and plots mean daytime
                                      radiation for each date

  `task3.py`                          Calculates daily mean and maximum
                                      radiation, finds the date and
                                      weather conditions associated with
                                      the maximum individual reading, and
                                      identifies the five days with the
                                      highest daily maximum

  `Data visualisation report.pdf`     Report containing the
                                      visualisations and written analysis
  -----------------------------------------------------------------------

### Methods

-   **Pandas** is used to load, filter, group, and summarise the
    dataset.
-   **Matplotlib** is used to create scatter plots, median trend lines,
    and time-based plots.
-   The daytime subset includes observations strictly after **06:00**
    and strictly before **18:00**.
-   Scatter points show individual measurements and their spread;
    grouped median lines show the typical radiation level for each
    temperature, humidity, wind-speed, or time-of-day group.
-   Comparing full-day and daytime-only plots helps reveal how near-zero
    nighttime radiation changes the apparent relationships.

The plots show associations in the data; they do not prove that one
environmental variable causes changes in another.

### Requirements

-   Python 3
-   Pandas
-   Matplotlib
-   NumPy is listed in the PS2 assignment brief for the day-wise
    analysis, although the current scripts may not use it directly.

Install the core libraries with:

``` bash
python -m pip install pandas matplotlib numpy
```

### Run the scripts

Open a terminal in the `PS2` folder. Keep `SolarPrediction.csv` in that
same folder, because the scripts load it by filename.

``` bash
python rad_vs_envvar.py
python rad_vs_time_plot.py
python daily_avg_rad.py
python task3.py
```

`data_cleaner.py` is imported by the analysis scripts to prepare the
data. Run each script separately to view its output.

## PS4 --- Product Ideathon: Mining the Asteroid Belt

**Goal:** Present a technically plausible and economically viable
asteroid-mining concept.

**File included:** `ProdIdeathon by Epstein List.pptx`

The PS4 brief asks the pitch deck to cover all three parts:

1.  **Engineering:** how the system reaches and operates around an
    asteroid, extracts and processes resources, obtains energy,
    transports or uses the material, and handles navigation,
    communication, autonomy, and failures.
2.  **Cost:** the three biggest cost drivers and the proposed ways to
    reduce them, with assumptions stated.
3.  **Business:** the chosen resource, customers, where it will be sold
    or used, the revenue model, and key business risks.

The brief specifies six content slides for these three parts, excluding
the cover and thank-you slides.
