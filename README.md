<p><a target="_blank" href="https://app.eraser.io/workspace/GfKGAlQJF4hlHKT0Xz81" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# Title: Optimizing Bike-Sharing Operations through Data-Driven Insights
## Description:
The bike-sharing company, equipped with extensive historical ride data, aims to optimize its operations and enhance user experience. Leveraging cloud-based infrastructure, batch processing, and workflow orchestration tools, the goal is to develop a robust data engineering solution that transforms raw data into actionable insights. The solution will culminate in a dashboard providing intuitive visualizations for stakeholders to make informed decisions.

## Problem:
The bike-sharing company faces challenges in efficiently managing its fleet, stations, and user experience. These challenges include:

### Demand Forecasting:
Predicting ride demand across different time periods, stations, and user demographics to allocate resources effectively and anticipate potential service disruptions.

### User Behavior Analysis:
Understanding user preferences, ride patterns, and factors influencing ridership to tailor marketing strategies, station placement, and pricing models.

### Operational Efficiency:
Identifying inefficiencies in bike distribution, station maintenance, and service availability to optimize fleet management and reduce operational costs.

## Proposed Solution:
Develop a data engineering pipeline that encompasses the following components:

### Data Ingestion:
Extract data from the "Divvy_trips_all_2013-2021" dataset stored in Google Cloud Storage (GCS) and load it into Google BigQuery for further processing.

### Data Transformation:
Apply batch processing techniques using SQL queries within DBT to transform raw trip data into aggregated metrics such as ride counts, average trip duration, and popular routes.

### Workflow Orchestration:
Utilize Mage AI for workflow orchestration to automate the data pipeline, ensuring timely execution of data transformations and updates.

### Data Analysis:
Employ SQL queries within DBT to perform exploratory data analysis (EDA) and generate insights on ride demand, user behavior, and operational efficiency.

### Dashboard Creation:
Utilize a Business Intelligence (BI) tool such as Data Studio to design an interactive dashboard. The dashboard will include:

- A graph showing the distribution of ride types (e.g., subscriber vs. customer) to understand user demographics and preferences.
- A temporal line graph illustrating ride frequency over time, allowing stakeholders to visualize trends and seasonality in ridership.
### Technology Stack:
- Cloud: Google Cloud Platform (GCP)
- Infrastructure as Code (IaC): Terraform
- Workflow Orchestration: Mage AI
- Data Warehouse: BigQuery
- Batch Processing: DBT - SQL
- Dashboard Tool: Data Studio
## Expected Outcome:
The developed dashboard will empower stakeholders, including operations managers, marketing teams, and city planners, to make data-driven decisions to optimize bike-sharing operations, enhance user experience, and drive business growth.


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Rides Data Model-1.eraserdiagram" data-element-id="g1hSsS9Vcc_C8tmEawhkX"><img src="/.eraser/GfKGAlQJF4hlHKT0Xz81___5kM4ZM4iKkdtYlmhik2Qk756wmk1___---diagram----bc16160461f45189520128d9d8c95566-Rides-Data-Model.png" alt="" data-element-id="g1hSsS9Vcc_C8tmEawhkX" /></a>
<a href="/README-Data Warehouse Solution Architecture-2.eraserdiagram" data-element-id="K32Ncu7iXJWadXUpAxd52"><img src="/.eraser/GfKGAlQJF4hlHKT0Xz81___5kM4ZM4iKkdtYlmhik2Qk756wmk1___---diagram----6cdf8b05a564a99ed284c4e1eacc48eb-Data-Warehouse-Solution-Architecture.png" alt="" data-element-id="K32Ncu7iXJWadXUpAxd52" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/GfKGAlQJF4hlHKT0Xz81 --->