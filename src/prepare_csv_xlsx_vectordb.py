# Credit: https://github.com/Farzad-R/Advanced-QA-and-RAG-Series/commits?author=Farzad-R

from utils.prepare_vectordb_from_csv_xlsx import PrepareVectorDBFromTabularData

if __name__=="__main__":
    from pyprojroot import here
    # Specify the path to your CSV file directory below
    file_path = here("data/csv_xlsx/chan-RenalGenie_Clinical_Note_csv.csv")
    # Create an instance of the PrepareVectorDBFromTabularData class with the file directory
    data_prep_instance = PrepareVectorDBFromTabularData(file_directory=file_path)
    # Run the pipeline to prepare and inject the data into the vector database
    data_prep_instance.run_pipeline()