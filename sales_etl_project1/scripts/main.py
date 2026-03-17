from extract import extract_data
from transform import transform_data
from load import load_data
from config import DB_CONFIGhg

file_path = "data/sales_data.csv"

data = extract_data(file_path= r"C:\Users\LMT02\OneDrive\Desktop\sales_etl_project1\data\sales_data.csv")

clean_data = transform_data(data)

load_data(clean_data, DB_CONFIG)

print("ETL Process Completed Successfully")