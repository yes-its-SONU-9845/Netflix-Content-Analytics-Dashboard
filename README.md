# Netflix-Content-Analytics-Dashboard
# Project 2: Netflix Content Analytics

## 📌 Project Description
This project delivers a comprehensive Exploratory Data Analysis (EDA) on Netflix's global content catalog, strictly aligned with the DMV Core Tech 2026 industry curriculum guidelines. The primary focus is to ingest unstructured streaming data, perform custom feature engineering, map out content distribution channels (Movies vs. TV Shows), trace historical release patterns, and extract data-driven entertainment insights for executive reporting.

## 🛠️ Tools, Technologies & Libraries Used
- **Programming Language:** Python 3.12+
- **Data Preprocessing & Wrangling:** Pandas, NumPy
- **Data Visualization Metrics:** Matplotlib, Seaborn
- **Environment Integration:** VS Code (Visual Studio Code) / Terminal Scripting Mode

## 📋 Project Workflow & Core Deliverables

### 1. Data Loading & Catalog Auditing
- Ingested a multi-variable Netflix catalog array containing parameters: `show_id`, `type`, `title`, `country`, `release_year`, `rating`, `duration`, and `listed_in`.
- Audited data structural types, isolated row dimensions, and checked initial shape boundaries.

### 2. Advanced Data Preprocessing & Feature Engineering
- Programmatically scanned and dropped duplicate content entries across multi-column subsets (`title`, `type`, `release_year`) to enforce strict data hygiene.
- **Feature Engineering:** Developed a dynamic data transformation pipeline using lambda logic to parse duration strings (`min` or `Seasons`) into a normalized numerical field called `duration_numeric` for clean mathematical charting.

### 3. Exploratory Data Analysis (EDA) & Aggregations
- Calculated exact volume market shares between Movies and TV Shows inside the active digital catalog.
- Segmented production volumes across geographical sovereign hubs to identify primary source markets.
- Aggregated temporal production patterns over release years to evaluate archive expansion metrics.

### 4. Professional Visualization Pipeline
Generated custom-themed data graphics to visualize streaming trends:
1. **Catalog Composition:** High-contrast Pie Chart defining the core type split.
2. **Geographic Distribution:** Frequency-ordered Count Plots identifying key content nations.
3. **Temporal Progression:** Linear Trend Plots highlighting catalog expansion over time.
4. **Duration Spread Matrix:** Multi-variable Stacked Histograms mapped with smooth KDE density curves.
5. **Consumer Safety Layout:** Horizontal Rating Density Bar Plots analyzing target demographics.

---

## 📈 Strategic Content Insights & Executive Summary
Based on the data output, the following analytical observations have been documented for streaming business strategy:
1. **Catalog Composition:** While Movies currently dominate the overall volume, TV Shows provide much heavier cumulative runtime engagement per asset due to extensive seasonal formats.
2. **Sovereignty Production Hubs:** The USA and India stand out as primary content creation pillars, making them the most critical target regions for future localization investments.
3. **Archival Modernization:** Content published after 2015 shows an aggressive exponential hockey-stick growth curve, shifting licensing strategies toward modern digital-first originals over historical assets.

1. Clone this repository to your local system:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
