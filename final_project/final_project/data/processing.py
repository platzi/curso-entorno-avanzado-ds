import final_project.utils.paths as path
import pandas as pd
import janitor

def load_proccesed_data(file_name):
    return (
        pd.read_csv(file_name)
        .transform_column(
            "date",
            pd.to_datetime
        )
    )