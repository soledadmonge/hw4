import sys
import os
import pytest
from datetime import datetime 
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hw5_lib', 'hw5_lib')))
sys.path.append(os.path.abspath("../")) 

from hw4 import get_day_month_year  

def test_get_day_month_year():
    dates = [
        datetime(2024, 1, 15),
        datetime(2023, 12, 31),
        datetime(2022, 6, 10)
    ]
    
    expected_data = [
        {'day': 15, 'month': 1, 'year': 2024},
        {'day': 31, 'month': 12, 'year': 2023},
        {'day': 10, 'month': 6, 'year': 2022}
    ]
    expected_df = pd.DataFrame(expected_data)

    result_df = get_day_month_year(dates)
    
    pd.testing.assert_frame_equal(result_df, expected_df, check_like=True) , "The Values on the DF does not correspond with the input."

if __name__ == "__main__":
    pytest.main()