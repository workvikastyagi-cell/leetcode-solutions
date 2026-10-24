import pandas as pd

def department_highest_salary(
    employee: pd.DataFrame,
    department: pd.DataFrame
) -> pd.DataFrame:
    merged = employee.merge(
        department,
        left_on="departmentId",
        right_on="id",
        suffixes=("_employee", "_department")
    )

    highest = merged.groupby("departmentId")["salary"].transform("max")
    result = merged[merged["salary"] == highest]

    return result[["name_department", "name_employee", "salary"]].rename(
        columns={
            "name_department": "Department",
            "name_employee": "Employee",
            "salary": "Salary"
        }
    )
