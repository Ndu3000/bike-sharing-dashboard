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
Utilize a Business Intelligence (BI) tool such as Looker Studio to design an interactive dashboard. The dashboard will include:

- A graph showing the distribution of ride types (e.g., subscriber vs. customer) to understand user demographics and preferences.
- A temporal line graph illustrating ride frequency over time, allowing stakeholders to visualize trends and seasonality in ridership.
    - Access the dashboard example [﻿here](https://lookerstudio.google.com/reporting/708e47ae-5213-45dd-913a-c3e2b343ec58) ﻿if the Looker Studio link is still active otherwise view it [here](https://github.com/Ndu3000/bike-sharing-dashboard/blob/main/visuals/images/dashboard.JPG). Note that a subset of the data has been queried for cost reasons so this is not indicative of real-world results but is only to demonstrate the technology capability to solve a business requirement.
### Technology Stack:
- Cloud: Google Cloud Platform (GCP)
- Infrastructure as Code (IaC): Terraform
- Workflow Orchestration: Mage AI
- Data Warehouse: BigQuery
- Batch Processing: DBT - SQL
- Dashboard Tool: Data Studio
## Expected Outcome:
The developed dashboard will empower stakeholders, including operations managers, marketing teams, and city planners, to make data-driven decisions to optimize bike-sharing operations, enhance user experience, and drive business growth.

## Instructions:
### Setting up Mage AI on Google Cloud Platform (GCP) using Terraform:
1. **Install Terraform:**
    - Download and install Terraform from Terraform's official website.
2. **Clone the Repository:**
3. **Navigate to Terraform Directory:**
4. **Set up Terraform Configuration:**
    - Update the `terraform.tfvars`  file with your desired configuration parameters.
5. **Initialize Terraform:**
    - Run `terraform init`  to initialize the Terraform configuration.
6. **Review Terraform Plan:**
    - Run `terraform plan`  to review the execution plan and ensure it matches your expectations. This is made easy by writing the `.out` cloud environment file e.g `terraform plan --out="tf_plan.out"`and running `terraform apply`  based on this cloud environment file.
7. **Apply Terraform Changes:**
    - Run `terraform apply`  to apply the Terraform configuration changes and provision the resources on GCP. So based on the above you will run it like this - `terraform apply tf_plan.out`.
8. **Terraform: Resources**
- [﻿Installing Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)  
- [﻿Installing gcloud CLI](https://cloud.google.com/sdk/docs/install)  
- [﻿Mage Terraform Templates](https://github.com/mage-ai/mage-ai-terraform-templates) 
Additional Mage Guides
- [﻿Terraform](https://docs.mage.ai/production/deploying-to-cloud/using-terraform)  
- [﻿Deploying to GCP with Terraform](https://docs.mage.ai/production/deploying-to-cloud/gcp/setup) 
### **Set up Google Big Query:**
1. Set up Google BigQuery and partition the raw schema table by month which means that in DBT you will have to consider the partitioning in the dbt model for the staging table.
2. A query for the partitioned table looks something this:
`SELECT * FROM  mage-project-74715.raw_divvy.bike_rides-2024-04-20T07_48_42_restore WHERE TIMESTAMP_TRUNC(_PARTITIONTIME, MONTH) = TIMESTAMP("2024-04-01") LIMIT 1000;`
![image](https://github.com/Ndu3000/bike-sharing-dashboard/assets/9050323/f6ad6af4-04aa-4e0a-858a-208a838d28fd)
3. The final data warehouse should look like the data model diagram at the bottom of this README file after setting up a single normal form normalised star schema for our data warehouse as this data is not too complex. The normalisation and partitioning is still required for the efficient querying of this large data set of daily bike rides since the year 2013 (over 2 million records).
### Configuring Mage AI Environment:
1. **Access Mage AI Console:**
    - Once the Terraform setup is complete, access the Mage AI console using the provided URL.
2. **Authenticate and Set Up Project:**
    - Follow the on-screen instructions to authenticate and set up your project in the Mage AI console.
3. **Versioning**:
    - Set up GitHub versioning on the top right settings button to sync the GCP Mage instance with local development.
### Setting up Raw Pipeline in Mage AI:
1. **Access Data Pipeline Section:**
    - Navigate to the Data Pipeline section in the Mage AI console.
2. **Create a New Pipeline:**
    - Create a new pipeline and name it appropriately (e.g., "Chicago Data Raw Pipeline"). Here is the API endpoint:
[﻿data.cityofchicago.org/resource/fg6s-gzvg.json](https://data.cityofchicago.org/resource/fg6s-gzvg.json) 
3. **Set up Data Source:**
    - Configure a data loader first in the pipeline to fetch data from the City of Chicago API mentioned above.
4. **Define Transformation Rules:**
    - Then define any necessary transformation rules or filters to process the raw data from the API.
5. **Schedule Pipeline Execution:**
    - Then set up a schedule for the pipeline to execute periodically to fetch updated data from the API.
6. **Run Pipeline and set up trigger schedule:**
    - Execute the pipeline to fetch data from the City of Chicago API and store it Google Big Query.
### Setting up DBT Staging Pipeline in Mage AI:
1. **Access DBT Environment:**
    - Navigate to the DBT section in the Mage AI console.
2. **Create DBT Project:**
    - Create a new DBT project within Mage AI. The initial set up of the DBT project structure in Mage should look like this.
![image](https://github.com/Ndu3000/bike-sharing-dashboard/assets/9050323/f525e25d-c017-4acd-9291-01e92777f508)

3. **Define DBT Configuration:**
    - Define your DBT project configuration, including connections to your data sources and targets.
4. **Create DBT Models:**
    - Define your DBT models within the Mage AI environment, either by writing SQL or using DBT's modeling capabilities.
5. **Run DBT Jobs:**
    - Run DBT jobs to execute your defined models and populate your target data warehouse.
6. **Verify Results:**
    - Verify the results of your DBT jobs to ensure that your models are functioning as expected and that data is correctly transformed and loaded into your target data warehouse.
By following these steps, you should be able to set up a raw pipeline in Mage AI to fetch data from the City of Chicago API and then set up a DBT staging pipeline to transform and load the data into your target data warehouse. Ensure to replace placeholders with actual values and customize the setup according to your specific requirements and environment.


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Data Warehouse Solution Architecture-1.eraserdiagram" data-element-id="K32Ncu7iXJWadXUpAxd52"><img src="/.eraser/GfKGAlQJF4hlHKT0Xz81___5kM4ZM4iKkdtYlmhik2Qk756wmk1___---diagram----3c1b68cf72162f77c40110b6d7d0b1e7-Data-Warehouse-Solution-Architecture.png" alt="" data-element-id="K32Ncu7iXJWadXUpAxd52" /></a>
<a href="/README-Rides Data Model-2.eraserdiagram" data-element-id="g1hSsS9Vcc_C8tmEawhkX"><img src="/.eraser/GfKGAlQJF4hlHKT0Xz81___5kM4ZM4iKkdtYlmhik2Qk756wmk1___---diagram----31d4d9029b6cc0b04345873e36c6dcd5-Rides-Data-Model.png" alt="" data-element-id="g1hSsS9Vcc_C8tmEawhkX" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/GfKGAlQJF4hlHKT0Xz81 --->
