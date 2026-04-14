# ☁️ Cloud ML Projects

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![AWS SageMaker](https://img.shields.io/badge/AWS-SageMaker-orange)
![AWS Glue](https://img.shields.io/badge/AWS-Glue-yellow)
![AWS Redshift](https://img.shields.io/badge/AWS-Redshift-red)
![Azure ML](https://img.shields.io/badge/Azure-ML-lightblue)
![Azure Data Factory](https://img.shields.io/badge/Azure-DataFactory-darkblue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

## 🧾 Description
Showcase of **machine learning projects deployed on AWS and Azure**.  
Includes **SageMaker training jobs**, **Glue ETL workflows**, **Redshift integration**, **Azure ML pipelines**, and **Data Factory orchestration** with cloud‑native scripts.

## ⭐ Features
- AWS SageMaker training and deployment scripts
- AWS Glue ETL jobs for preprocessing
- Redshift SQL integration for analytics
- Azure ML pipelines for model training
- Azure Data Factory orchestration examples
- Sample datasets for reproducible demos

## 📂 Repository Structure
cloud-ml-projects/
│── aws/
│   ├── sagemaker_training.py
│   ├── glue_etl_job.py
│   ├── redshift_integration.sql
│── azure/
│   ├── azureml_pipeline.py
│   ├── datafactory_pipeline.json
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore

## 🚀 Quickstart
Clone the repo and install dependencies:
```bash
git clone https://github.com/melessemenelik/cloud-ml-projects.git
cd cloud-ml-projects
pip install -r requirements.txt
python aws/sagemaker_training.py
python azure/azureml_pipeline.py
## 📊 Sample Outputs

### AWS SageMaker Training
```text
2026-04-14 12:00:00 Starting training job: sklearn-training-123
2026-04-14 12:00:05 Uploading data to S3 bucket: your-bucket/train-data
2026-04-14 12:00:10 Training job launched on ml.m5.large
2026-04-14 12:05:30 Training completed successfully
2026-04-14 12:05:35 Model artifact saved to s3://your-bucket/output/model.tar.gz
2026-04-14 12:10:00 Job GlueETLJob started
2026-04-14 12:10:05 Reading data from s3://your-bucket/input-data
2026-04-14 12:10:20 Dropping column: unnecessary_column
2026-04-14 12:10:40 Writing transformed data to s3://your-bucket/output-data
2026-04-14 12:10:45 Job GlueETLJob completed successfully
2026-04-14 12:20:00 Submitting experiment: azureml-pipeline
2026-04-14 12:20:05 Environment ml-env created
2026-04-14 12:20:10 Running training script: train.py
2026-04-14 12:25:30 Training completed with accuracy: 0.92
2026-04-14 12:25:35 Experiment run finished successfully
