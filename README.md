# Data Analysis on Spotify Streaming History

A series of Jupyter notebooks aimed at applying data science concepts to my own streaming history using pandas.

# Core Capabilities Demonstrated
Data Infrastructure: Python, Pandas, Requests, Jupyter

Concepts: Extract-Transform-Load (ETL) pipelines, Time-Series Filtering, Defensive API Consumption, Data Vectorization

## data-cleaning.ipynb

Noise Reduction: Isolated core music streaming logs by identifying and removing non-music anomalies (audiobooks and podcasts), ensuring no data pollution in downstream models.

Schema Optimisations: Streamlined the dataframe by stripping non-essential metadata columns, reducing memory overhead and improving array-processing efficiency

Temporal Data Parsing: Converted string-based ISO 8601 timestamps into native Pandas datetime objects, allowing for more efficient processing and easier handling

Parametric Data Segmentation: Engineered a reusable filtering pipeline to dynamically filter logs by year, establishing a framework for multi-year analysis

## wrapped.ipynb



Vectorized Mapping: Developed a high-speed lookup pipeline using Pandas .map() to cross-reference local historical data with external music metadata.

Robust API Integration: Consumed the Last.fm REST API to fetch crowdsourced genre data, implementing defensive exception handling to manage missing fields and empty payloads cleanly.

Data Optimization: Implemented strict volume thresholds (top 150 artists) to maximize script execution speeds and prevent API rate-limiting blocks.
