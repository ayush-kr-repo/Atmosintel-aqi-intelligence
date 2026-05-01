# AtmosIntel – Hyper‑Local AQI Intelligence Platform

## Overview
**AtmosIntel** is a hyper‑local air quality intelligence system designed to convert sparse monitoring station data into **ward‑level pollution insights**. The platform uses spatial interpolation and environmental analytics to generate **real‑time pollution heatmaps**, identify high‑risk zones, and produce automated advisories for citizens and government authorities.

The goal is to enable **data‑driven urban pollution management** by transforming raw air quality data into actionable intelligence.

---

# 🚨 Problem Statement

Urban air quality monitoring relies on a **limited number of monitoring stations**, which often represent large geographic regions. This creates blind spots where localized pollution sources remain undetected.

For example:

- Delhi has **~47 monitoring stations**
- But contains **250+ administrative wards**

Because of this limitation, authorities struggle to:

- Detect **localized pollution hotspots**
- Identify **pollution sources early**
- Issue **hyper-local health advisories**
- Deploy **mitigation resources efficiently**

This results in **reactive pollution management instead of proactive environmental control**. 

---

# 💡 Proposed Solution

AtmosIntel addresses this problem by generating a **continuous air‑quality surface across the city** using spatial interpolation techniques.

The system pipeline works as follows: 

1. Collect **real-time AQI measurements** from monitoring stations  
2. Use **Inverse Distance Weighting (IDW) interpolation** to estimate pollution levels at unsampled locations  
3. Optimize spatial queries using **KDTree nearest-neighbor search**  
4. Generate a **city-wide pollution surface**
5. Aggregate pollution values at the **administrative ward level**
6. Detect **high-risk pollution zones**
7. Generate **automated citizen advisories and mitigation recommendations**
8. Display results on an **interactive geospatial dashboard**

---

# 🧠 Core Technical Idea

### Inverse Distance Weighting (IDW)

IDW is a spatial interpolation technique that estimates pollution levels at unknown locations by **weighting nearby monitoring stations inversely to their distance**.

Points closer to a monitoring station influence the prediction more than distant stations.

Mathematically:
AQI(x) = Σ (AQI_i / d_i^p) / Σ (1 / d_i^p)

Where:

- `AQI_i` = AQI value of station i  
- `d_i` = distance to station i  
- `p` = power parameter controlling influence decay  

---

### KDTree Optimization

Spatial interpolation requires frequent **nearest-neighbor searches**.

Using **KDTree spatial indexing** from SciPy significantly improves performance by reducing search complexity from:
O(n²) → approximately O(n log n)

This enables **fast interpolation across hundreds of ward locations**.

# ✨ Key Features

## 1️⃣ Hyper-Local AQI Mapping
Transforms sparse station data into a **continuous pollution heatmap across the entire city**.

---

## 2️⃣ Ward-Level Air Quality Intelligence
Estimates AQI values for **each administrative ward**, enabling localized environmental insights.

---

## 3️⃣ Pollution Hotspot Detection
Automatically identifies the **most polluted wards requiring immediate attention**.

---

## 4️⃣ Automated Citizen Advisories

The system generates **health recommendations** such as:

- Wear protective masks
- Avoid outdoor physical activity
- Limit exposure for vulnerable populations

---

## 5️⃣ Government Mitigation Recommendations

AtmosIntel suggests possible mitigation actions such as:

- Deploy **dust suppression vehicles**
- Inspect **construction zones**
- Investigate **local pollution sources**
- Increase **environmental monitoring**

---

## 6️⃣ Priority Action List

The system produces a ranked list of **top polluted wards** to help authorities **prioritize interventions efficiently**.

---

**--> System Architecture**

```
AQI Monitoring Stations
        ↓
Real‑Time Data Collection (GitHub Dataset)
        ↓
Spatial Interpolation Model (IDW + KDTree)
        ↓
City‑Wide Pollution Surface
        ↓
Ward‑Level AQI Aggregation
        ↓
Advisory & Decision Engine
        ↓
Interactive Monitoring Dashboard
```

---

# 🛠 Technology Stack

| Component | Technology |
|--------|--------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Geospatial Analysis | GeoPandas, Shapely |
| Spatial Modeling | SciPy KDTree, IDW Interpolation |
| Visualization | Folium |
| Data Pipeline | GitHub Actions |
| Development Environment | Google Colab |

---

# 📊 Dashboard Preview
*(Screenshots will be inserted here)*

### AQI Heatmap


### Ward-Level Pollution Visualization


### Monitoring Station Map

---
** --> Repository Structure**

```
delhi-aqi-dataset
│
├── data/aqi_data.csv
├── data/delhi_wards.geojson
├── notebooks/AtmosIntel_MVP.ipynb
├── outputs/AtmosIntel_dashboard.html
├── src/fetch_aqi.py
├── priority_wards.csv(created in the colab notebook)
├── aqi_collector.py
└── .github/workflows/
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/durlabhjilegend-lgtm/AtmosIntel.git
cd AtmosIntel
```

Install dependencies:
```bash
pip install pandas numpy geopandas shapely scipy folium
```

Or install using requirements file:
```
pip install -r requirements.txt
```

# ▶️ How to Run the Project

### 1️⃣ Open the Notebook

Open **AtmosIntel_MVP.ipynb** in **Google Colab**.

### 2️⃣ Run All Cells

The notebook will:

- Load AQI data from GitHub  
- Display monitoring stations  
- Perform spatial interpolation  
- Estimate ward‑level AQI  
- Generate advisories  

### 3️⃣ Generate Dashboard

The notebook exports an interactive dashboard:

```
AtmosIntel_dashboard.html
```

---

**Dashboard Capabilities**

The generated dashboard allows users to:

- View **real‑time AQI distribution**
- Identify **high‑risk wards**
- Inspect monitoring stations
- Monitor pollution hotspots
- Access automated advisories

---

# 📊 Data Source

AQI data is collected from urban air quality monitoring stations.

The dataset includes:

- Monitoring station name
- Latitude
- Longitude
- AQI value

Administrative boundaries are provided via:
```
delhi_wards.geojson
```

# 🚀 Future Improvements

Planned improvements include:

- Real‑time pollutant monitoring (PM2.5, PM10, NO₂, SO₂)
- Machine learning based **pollution source detection**
- Wind‑driven pollution trajectory analysis
- Automated alert notification systems
- Integration with smart city command centers
- Time-series pollution forecasting

---

# 🌱 Impact

AtmosIntel demonstrates how environmental data can be transformed into **actionable intelligence for urban governance**.

Potential benefits include:

- Early detection of pollution hotspots  
- Targeted mitigation strategies  
- Improved public health awareness  
- Data‑driven environmental policy  

---

# 👨‍💻 Authors

Developed by:

- **Durlabh Biswas**
- **Ayush Kumar**
- **Shreyan Porel**
- **Vivyaan Ojha**
---

Explore the notebook and dashboard to see how AtmosIntel converts raw AQI data into hyper‑local pollution intelligence.
