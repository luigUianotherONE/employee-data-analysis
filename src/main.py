import pandas as pd

from data_cleaning import clean_data
from validation import validate_data
from analysis import salary_by_gender, salary_by_department, experience_correlation, top_earners, invalid_phones_summary


def main():
    # 1. carregar dados
    df = pd.read_csv("data/raw/employees.csv")

    # 2. limpeza
    df = clean_data(df)

    # 3. validação
    df = validate_data(df)

    # 4. salvar resultado
    df.to_csv("data/processed/employees_cleaned.csv", index=False)

    # 5. análises simples
    print("\nSalary by gender:")
    print(salary_by_gender(df))

    print("\nSalary by department:")
    print(salary_by_department(df))

    print("\nExperience correlation:")
    print(experience_correlation(df))

    print("\nTop earners:")
    print(top_earners(df))

    print("\nPhone errors:")
    print(invalid_phones_summary(df))


if __name__ == "__main__":
    main()