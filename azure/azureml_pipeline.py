# azure/azureml_pipeline.py
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment

# Connect to workspace
ws = Workspace.from_config()

# Define environment
env = Environment.from_conda_specification(name="ml-env", file_path="environment.yml")

# Define training script
src = ScriptRunConfig(source_directory=".",
                      script="train.py",
                      environment=env)

# Submit experiment
exp = Experiment(workspace=ws, name="azureml-pipeline")
run = exp.submit(src)
run.wait_for_completion(show_output=True)
