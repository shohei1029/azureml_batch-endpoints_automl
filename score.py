import joblib
import os

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')

    model = joblib.load(model_path)

def run(mini_batch): # Pandas df if input is FIleDataset
    print(f"run method start: {__file__}, run({mini_batch})")
    result = model.predict(mini_batch)
    return result.tolist()