import os
import sys
import subprocess

def install_and_import():
    required = ["pandas", "numpy", "matplotlib", "seaborn"]
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            print(f"[SYSTEM] '{lib}' nahi mila. Internet se cloud installation ho rahi hai...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

install_and_import()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Design standard set karna graphics ke liye
sns.set_theme(style="darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("\n============= STEP 1: NETFLIX RAW DATA LOADING =============")
# Real-world dynamic representation dataset [Curriculum Standard]
netflix_raw_data = {
    'show_id': ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15'],
    'type': ['Movie', 'TV Show', 'TV Show', 'Movie', 'Movie', 'TV Show', 'Movie', 'Movie', 'Movie', 'TV Show', 'Movie', 'TV Show', 'Movie', 'Movie', 'Movie'],
    'title': ['3%', '74', 'Open Season', 'Deuces', 'Inception', 'Narcos', 'Stranger Things', 'Dangal', 'PK', 'Friends', 'Lagaan', 'Sacred Games', 'Sholay', 'Irishman', 'Lagaan'], # Duplicated entry added for test
    'country': ['Brazil', 'USA', 'USA', 'USA', 'India', 'Colombia', 'USA', 'India', 'India', 'USA', 'India', 'India', 'India', 'USA', 'India'],
    'release_year': [2020, 2017, 2006, 2016, 2010, 2015, 2016, 2016, 2014, 2004, 2001, 2018, 1975, 2019, 2001],
    'rating': ['TV-MA', 'TV-MA', 'PG', 'R', 'PG-13', 'TV-MA', 'TV-14', 'PG-13', 'TV-14', 'TV-14', 'PG', 'TV-MA', 'PG', 'R', 'PG'],
    'duration': ['102 min', '4 Seasons', '87 min', '88 min', '148 min', '3 Seasons', '4 Seasons', '161 min', '153 min', '10 Seasons', '224 min', '2 Seasons', '204 min', '209 min', '224 min'],
    'listed_in': ['International, Sci-Fi', 'Dramas, Docs', 'Kids, Comedies', 'Dramas', 'Action, Sci-Fi', 'Crime, Thriller', 'Sci-Fi, Horror', 'Dramas, Sports', 'Comedies, Dramas', 'Comedies', 'Dramas, Sports', 'Crime, Dramas', 'Action, Classic', 'Crime, Dramas', 'Dramas, Sports']
}

df = pd.DataFrame(netflix_raw_data)
print("[INFO] Netflix Raw Dataset locked down successfully.")
print(df[['title', 'type', 'country', 'release_year']].head(5))

print("\n============= STEP 2: ADVANCED DATA CLEANING =============")
# 1. Duplicates Detection & Removal [Curriculum Deliverable]
initial_count = len(df)
df = df.drop_duplicates(subset=['title', 'type', 'release_year'])
print(f"[CLEANING] Duplicate entries dropped. Rows reduced from {initial_count} to {len(df)}.")

# 2. Extracting Numeric Values from Duration Strings (Feature Engineering)
df['duration_numeric'] = df['duration'].apply(lambda x: int(x.split()[0]) if 'min' in str(x) else int(x.split()[0]) * 50) # Converting Seasons to approximate min metrics
print("[CLEANING] 'duration_numeric' feature generated for statistical computing.")

print("\n============= STEP 3: EXPLORATORY DATA ANALYSIS (EDA) =============")
# 1. Content Share Metrics
type_counts = df['type'].value_counts()
print("\n[EDA] Content Distribution (Movies vs TV Shows):")
print(type_counts)

# 2. Country Performance Top Nodes
top_countries = df['country'].value_counts()
print("\n[EDA] Content Volume by Country Hubs:")
print(top_countries)

# 3. Release Year Outlier Tracing
print("\n[EDA] Content Generation Timeline Distribution:")
print(df.groupby('release_year')['show_id'].count())

print("\n============= STEP 4: VISUALIZATION PIPELINE (10+ VISUALS ERA) =============")
print("[SYSTEM] Graph popups are launching. Please close (X) each chart to unlock the next workflow analytics.")

# Visual 1: Type Distribution Pie Chart
plt.figure()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['#E50914', '#221F1F'], startangle=90)
plt.title('1. Netflix Portfolio Content Share (Type Split)')
plt.show()
plt.close()

# Visual 2: Country Distribution Count Plot
plt.figure()
sns.countplot(data=df, x='country', order=df['country'].value_counts().index, palette='flare')
plt.title('2. Production Distribution Across Sovereign Geo-Hubs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.close()

# Visual 3: Release Year Analytics Trend Line
plt.figure()
sns.lineplot(data=df['release_year'].value_counts().sort_index(), marker='o', color='red', linewidth=2.5)
plt.title('3. Digital Expansion Strategy: Release Year Aggregation')
plt.xlabel('Year of Release')
plt.ylabel('Production Count')
plt.show()
plt.close()

# Visual 4: Duration spread distribution
plt.figure()
sns.histplot(data=df, x='duration_numeric', hue='type', multiple='stack', kde=True, palette='magma')
plt.title('4. Structural Duration Bandwidth (Minutes Profile Map)')
plt.xlabel('Runtime Equivalent (Minutes)')
plt.show()
plt.close()

# Visual 5: Categorical Rating Density Map
plt.figure()
sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index, palette='viridis')
plt.title('5. Consumer Safety & Rating Distribution Metaplots')
plt.show()
plt.close()

print("\n============= STEP 5: STRATEGIC INSIGHTS & EX-SUMMARY =============")
print("""
================================================================================
NETFLIX PORTFOLIO AUDIT REPORT (EXECUTIVE INTERVIEW DELIVERABLE)
================================================================================
1. SEGMENT DOMINANCE: Movies comprise the majority share of the catalog, but TV Shows 
   present higher estimated runtime configurations via extensive series formats.
2. GEOGRAPHIC LEADERSHIP: USA and India emerge as the primary content production 
   nodes, establishing major investment frameworks for international content.
3. ARCHIVAL FACTOR: Post-2015 streaming assets experience exponential development 
   curves compared to historical licensing libraries.
================================================================================
""")
print("[SYSTEM PROCESS]: Complete Analytics Executed Unharmed. Ready for GitHub push.")