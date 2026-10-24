import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates().sort_values(ascending= False)
    result = salary.iloc[1] if len(salary) >= 2 else None
    return pd.DataFrame({'SecondHighestSalary': [result]})