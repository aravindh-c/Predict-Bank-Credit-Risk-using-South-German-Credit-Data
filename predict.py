
from src.pipeline.batch_prediction import start_batch_prediction

file_path="/config/workspace/SouthGermanCreditRisk_pred.csv"
print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction(input_file_path=file_path)
          print(output_file)
     except Exception as e:
          print(e)