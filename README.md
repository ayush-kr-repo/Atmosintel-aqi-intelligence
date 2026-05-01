# AtmosIntel - Hyper-Local AQI Intelligence Platform

AtmosIntel converts sparse air-quality monitoring data into ward-level pollution intelligence using spatial interpolation and geospatial analytics.

The platform estimates AQI for unsampled Delhi wards, detects pollution hotspots, generates citizen/government advisories, and exports an interactive Folium dashboard.

## Project Scale

- Processed 11,233 AQI records from 47 Delhi monitoring stations.
- Mapped pollution estimates across 251 administrative wards.
- Used Inverse Distance Weighting (IDW) interpolation with SciPy cKDTree nearest-neighbor search.
- Generated ward-level AQI estimates, hotspot rankings, citizen advisories, and mitigation recommendations.
- Automated AQI data collection through GitHub Actions using the WAQI API.

## Problem

Urban air-quality monitoring relies on a limited number of monitoring stations. Delhi has around 47 monitoring stations but more than 250 administrative wards, creating blind spots where localized pollution can go undetected.

This makes it harder for authorities to identify high-risk zones, issue hyper-local health advisories, and prioritize mitigation resources.

## Solution

AtmosIntel generates a continuous air-quality surface from sparse station readings and aggregates the estimated AQI values at ward level.

Pipeline:

1. Collect AQI readings from monitoring stations.
2. Estimate AQI at unsampled locations using IDW interpolation.
3. Use SciPy cKDTree to optimize nearest-neighbor spatial lookup.
4. Aggregate interpolated AQI values across ward polygons.
5. Rank high-risk wards.
6. Generate citizen advisories and government mitigation recommendations.
7. Export an interactive Folium dashboard.

## Technical Approach

### Inverse Distance Weighting

IDW estimates AQI at an unknown location by weighting nearby stations more heavily than distant stations.

```text
AQI(x) = sum(AQI_i / d_i^p) / sum(1 / d_i^p)
```
Where:

- `AQI_i` is the AQI value at station `i`.
- `d_i` is the distance from the unknown location to station `i`.
- `p` controls how quickly influence decreases with distance.

### KDTree Optimization

Spatial interpolation requires repeated nearest-neighbor lookups. AtmosIntel uses `scipy.spatial.cKDTree` to speed up station lookup and make interpolation practical across hundreds of ward/grid locations.

## Features

- Hyper-local AQI surface generation.
- Ward-level AQI estimation.
- Pollution hotspot ranking.
- Citizen health advisories.
- Government mitigation recommendations.
- Interactive Folium dashboard.
- Scheduled AQI data collection with GitHub Actions.

## Project Preview

Dashboard screenshots will be added after upload.

## Repository Structure

```text
atmosintel-aqi-intelligence/
├── .github/workflows/
│   └── aqi.yml
├── data/
│   ├── aqi_data.csv
│   └── delhi_wards.geojson
├── notebooks/
│   └── AtmosIntel_MVP.ipynb
├── outputs/
│   └── AtmosIntel_dashboard.html
├── src/
│   └── fetch_aqi.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Geospatial Analysis | GeoPandas, Shapely |
| Spatial Modeling | SciPy cKDTree, IDW interpolation |
| Visualization | Folium |
| Automation | GitHub Actions |
| Notebook Environment | Google Colab / Jupyter |

## Setup

Clone the repository:

```bash
git clone https://github.com/ayush-kr-repo/atmosintel-aqi-intelligence.git
cd atmosintel-aqi-intelligence
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file if you want to run AQI collection locally:

```text
WAQI_TOKEN=your_actual_token
```

The repository includes `.env.example` as a safe template. Do not commit real API tokens.

## How to Run

Run the data collector:

```bash
python src/fetch_aqi.py
```

Open the notebook:

```text
notebooks/AtmosIntel_MVP.ipynb
```

The notebook performs interpolation, ward-level AQI estimation, advisory generation, and dashboard export.

Generated dashboard:

```text
outputs/AtmosIntel_dashboard.html
```

## GitHub Actions

The workflow in `.github/workflows/aqi.yml` can collect AQI data on a schedule.

Required repository secret:

```text
WAQI_TOKEN
```

## Data Sources

- AQI readings: WAQI API / monitoring station data.
- Ward boundaries: Delhi ward GeoJSON file included in `data/delhi_wards.geojson`.

## Current Limitations

- IDW is distance-based and does not model wind, traffic, industrial activity, or weather.
- AQI quality depends on station availability and API response reliability.
- The current version estimates AQI spatially but does not forecast future pollution.
- Dashboard is exported as static HTML rather than deployed as a hosted app.

## Future Improvements

- Add pollutant-level analysis for PM2.5, PM10, NO2, SO2, and O3.
- Add wind-aware pollution movement modeling.
- Add time-series AQI forecasting.
- Deploy dashboard publicly.
- Add automated alert notifications.
- Add validation against held-out monitoring stations.

## Authors

Built by:
- Ayush Kumar
- Durlabh Biswas
- Shreyan Porel
- Vivyaan Ojha
