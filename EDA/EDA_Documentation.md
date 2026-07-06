====================================================================
Exoplanet Habitability Zone Analysis
====================================================================
Project: Exoplanet Habitability Zone Analysis - EDA
File:    EDA_Habitability_Analysis.ipynb
Dataset: Data_Gold_Layer.csv
--------------------------------------------------------------------


OVERVIEW
--------
This notebook does two main things:
  1. Adds new calculated columns to the dataset (enriched data).
  2. Defines 4 dashboard pages with charts and key numbers (KPIs).

The final enriched dataset is saved as:
  Data_Gold_Layer_Enriched.csv


====================================================================
PART 1 — SCIENTIFIC CALCULATIONS
====================================================================

STEP 1: Data Loading & Cleaning
---------------------------------
- The dataset is loaded from Data_Gold_Layer.csv (5,878 planets total).
- Missing values are filled in before any calculations:
    Temperature     → filled with the median value
    Flux            → filled with the median value
    Eccentricity    → filled with 0.0 (assumed circular orbit)
    System_Distance → filled with the median value
    Parallax        → filled with the median value


STEP 2: New Columns Added to the Dataset
-----------------------------------------
Three flag columns (True/False) and one score column are created:

  1. is_habitable (True/False)
     A planet is in the Habitable Zone if ALL of these are true:
       - Stellar Flux (Flux) is between 0.25 and 2.2 (Earth units)
       - Temperature is between 180 K and 320 K
     → Result: 302 planets are habitable.

  2. is_rocky (True/False)
     A planet is rocky if:
       - Radius < 1.6 Earth radii
     → This separates small rocky planets from large gas giants.

  3. is_habitable_rocky (True/False)
     A planet is BOTH habitable AND rocky.
     → Result: 45 planets meet this stricter condition.

  4. Escape_Velocity (numeric)
     Calculated as: sqrt(Mass / Radius)
     This measures how strong the planet's gravity is.
     It is needed for the ESI formula below.

  5. ESI — Earth Similarity Index (0 to 1 score)
     This score tells us how similar a planet is to Earth.
     A score of 1.0 = identical to Earth. A score near 0 = very different.

     ESI uses 4 planet properties compared to Earth:
       - Radius        (Earth = 1.0)     weight = 0.57
       - Density       (Earth = 5.51)    weight = 1.07
       - Escape Velocity (Earth = 1.0)   weight = 0.70
       - Temperature   (Earth = 255 K)   weight = 5.58  ← most important!

     The formula multiplies these 4 comparisons together and takes a
     weighted average. Temperature has the highest weight because it
     matters most for life.

     → Highest ESI in the dataset: 0.9935 (planet: GJ 1002 b)
     → Top 10 most Earth-like planets are listed in the notebook.


====================================================================
PART 2 — DASHBOARD PAGES (4 pages defined)
====================================================================

Each page has:
  - An objective (what question it answers)
  - KPIs (key numbers shown at the top)
  - Charts (visualizations)


--------------------------------------------------------------------
PAGE 1: Overview & Discovery Methods
--------------------------------------------------------------------
Goal: Show how and when exoplanets were discovered, and where they are.

KPIs:
  - Total Planets:       5,878
  - Unique Host Stars:   4,332
  - Max Distance:        2,674.3 parsecs (≈ 8,718 light years)
  - Binary System Share: 9.87% (planets with 2 host stars)

Charts:
  1. Stacked Area Chart  — Discoveries per year, colored by method
  2. Bar Chart           — Which discovery method found the most planets
  3. Histogram           — How far are exoplanets from Earth (in parsecs)
  4. Donut Chart         — What % of systems have 1 star vs. 2+ stars

Column names used:
  Year, Method, System_Distance, No_of_Stars, Is binary, star_name


--------------------------------------------------------------------
PAGE 2: Physical & Orbital Characteristics
--------------------------------------------------------------------
Goal: Understand planet sizes, masses, and how they orbit their stars.

KPIs:
  - Avg Radius:       94.41 Earth radii
  - Avg Mass:         241.48 Earth masses
  - Avg Density:      5.39 g/cm³
  - Avg Eccentricity: 0.120 (0 = perfect circle, 1 = very stretched)

Charts:
  1. Scatter Plot (log scale) — Kepler's 3rd Law: larger orbit = longer year
                                Habitable planets highlighted in green
  2. Scatter Plot             — Bigger radius usually means bigger mass
                                Rocky vs. gaseous planets shown in color
  3. Histogram                — Most planets have near-circular orbits
  4. Bar Chart                — Count of rocky vs. gaseous planets

Key insight: A planet with Radius > 1.6 Earth radii is classified as
             gaseous (like Neptune/Jupiter). Below that = rocky (like Earth).

Column names used:
  Semi_major axis, orbital period, Radius, Mass, Density, Eccentricity,
  is_habitable, is_rocky


--------------------------------------------------------------------
PAGE 3: Stellar Properties & Host Systems
--------------------------------------------------------------------
Goal: Learn about the stars that host these exoplanets.

KPIs:
  - Avg Star Temperature:   5,431.1 K  (our Sun = 5,778 K)
  - Avg Stellar Mass:       0.97 solar masses  (very similar to our Sun)
  - Avg Stellar Luminosity: 1.45 solar luminosities
  - Largest System:         8 planets around one star

Charts:
  1. H-R Diagram      — Plot of star temperature vs. brightness (luminosity)
                        Classic astronomy chart; hotter = brighter
  2. Scatter Plot     — Stars that are more massive tend to be hotter
  3. Bar Chart        — Most host stars have only 1 planet discovered
  4. Correlation Heatmap — How strongly star properties relate to each other

Column names used:
  Star Temperature, Star Radius, Stellar Mass, Stellar Luminosity,
  Planet numbers, star_name, PlanetName


--------------------------------------------------------------------
PAGE 4: Habitability & Goldilocks Zone
--------------------------------------------------------------------
Goal: Find the most Earth-like planets that could support life.

KPIs:
  - Habitable Zone Planets:   302
  - Habitable Rocky Planets:   45
  - Highest ESI Score:        0.9935  → GJ 1002 b
  - Closest Habitable Planet: Proxima Cen b at 1.30 pc (≈ 4.2 light years)

Charts:
  1. Goldilocks Zone Scatter  — Flux vs. Temperature with the safe zone shaded
                                in light green (where habitable planets live)
  2. Radius vs. Flux Scatter  — Shows which planets are both small AND in HZ
                                Red dashed line at Radius = 1.6 marks rocky boundary
  3. ESI Histogram            — Most planets score very low (not Earth-like at all)
  4. Top 10 Bar Chart         — The 10 planets with the highest ESI scores

Column names used:
  Flux, Temperature, Radius, ESI, System_Distance,
  is_habitable, is_rocky, is_habitable_rocky, pl_name


====================================================================
LIBRARIES USED
====================================================================
  pandas      — loading and working with the data table
  numpy       — math calculations (sqrt, abs, etc.)
  matplotlib  — drawing charts
  seaborn     — making charts look nicer (built on matplotlib)


====================================================================
KEY COLUMN NAMES (Gold Layer Naming Convention)
====================================================================
  pl_name           — planet name
  PlanetName        — alternate planet name column
  star_name         — host star name
  Radius            — planet radius (Earth units)
  Mass              — planet mass (Earth units)
  Density           — planet density (g/cm³)
  Temperature       — planet equilibrium temperature (Kelvin)
  Flux              — stellar flux (Earth insolation units)
  Eccentricity      — orbit shape (0 = circle)
  Semi_major axis   — average distance from star (AU)
  orbital period    — time for one orbit (days)
  System_Distance   — distance from Earth (parsecs)
  Parallax          — stellar parallax measurement
  Year              — year the planet was discovered
  Method            — how it was discovered
  No_of_Stars       — how many stars in the system
  Is binary         — True/False: does it have 2 stars
  Planet numbers    — how many planets in the system
  Star Temperature  — host star temperature (Kelvin)
  Star Radius       — host star radius (solar units)
  Stellar Mass      — host star mass (solar units)
  Stellar Luminosity — host star brightness (solar units)

  [New columns added by this notebook]
  Escape_Velocity   — sqrt(Mass / Radius)
  ESI               — Earth Similarity Index (0 to 1)
  is_habitable      — True if planet is in the Habitable Zone
  is_rocky          — True if Radius < 1.6 Earth radii
  is_habitable_rocky — True if both habitable AND rocky


====================================================================
SUMMARY
====================================================================
This notebook taught us how to:
  1. Clean missing data before doing calculations.
  2. Use scientific formulas to score how "Earth-like" each planet is.
  3. Define what "habitable" means using temperature and flux thresholds.
  4. Organize a 4-page dashboard with specific charts for each topic:
       Page 1 → Discovery history
       Page 2 → Planet physical properties
       Page 3 → Star properties
       Page 4 → Habitability and ESI ranking
  5. The most Earth-like planet found is GJ 1002 b with ESI = 0.9935.
  6. The closest potentially habitable planet is Proxima Cen b at 4.2 light years.