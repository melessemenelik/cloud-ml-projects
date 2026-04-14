# aws/sagemaker_training.py
import sagemaker
from sagemaker import get_execution_role
from sagemaker.sklearn.estimator import SKLearn

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()
role = get_execution_role()

# Define estimator
sklearn_estimator = SKLearn(
    entry_point="train.py",   # your training script
    role=role,
    instance_type="ml.m5.large",
    framework_version="1.0-1",
    sagemaker_session=sagemaker_session
)

# Launch training job
sklearn_estimator.fit({"train": "s3://your-bucket/train-data"})
