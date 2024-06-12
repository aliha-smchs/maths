import streamlit as st
import pandas as pd


# Set page Title

def alldata():
    # Load the data
    file_2023 = 'data/Math2023.csv'
    file_2024 = 'data/Math2024OLD.csv'

    # Read the CSV files
    data_2023 = pd.read_csv(file_2023)
    data_2024 = pd.read_csv(file_2024)
    grade_boundaries_2023 = {
        'Year 2': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 3': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 4': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 5': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 6': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 7': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 8': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 9': {'Mathematic': {'9': 80, '8': 75, '7': 65, '6': 50, '5': 40, '4': 36, '3': 30, '2': 0}},
        'Year 10': {'Mathematic': {'9': 80, '8': 75, '7': 65, '6': 50, '5': 40, '4': 36, '3': 30, '2': 0}},
        'Year 11': {'Mathematic': {'9': 80, '8': 75, '7': 65, '6': 50, '5': 40, '4': 36, '3': 30, '2': 0}},
        'Year 12': {'Mathematic': {'A*': 85, 'A': 75, 'B': 65, 'C': 55, 'D': 50, 'E': 40, 'U': 0}},

    }

    grade_boundaries_2024 = {
        'Year 2': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 3': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 4': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 5': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 6': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 7': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 8': {'Mathematic': {'A*': 80, 'A': 75, 'B': 65, 'C': 50, 'D': 40, 'E': 36, 'F': 30, 'U': 0}},
        'Year 9': {'Mathematic': {'9': 80, '8': 75, '7': 65, '6': 50, '5': 40, '4': 36, '3': 30, '2': 0}},
        'Year 10': {'Mathematic': {'9': 80, '8': 75, '7': 65, '6': 50, '5': 40, '4': 36, '3': 30, '2': 0}},
        'Year 11': {'Mathematic': {'9': 80, '8': 75, '7': 65, '6': 50, '5': 40, '4': 36, '3': 30, '2': 0}},
        'Year 12': {'Mathematic': {'A*': 85, 'A': 75, 'B': 65, 'C': 55, 'D': 50, 'E': 40, 'U': 0}},
        'Year 13': {'Mathematic': {'A*': 85, 'A': 75, 'B': 60, 'C': 55, 'D': 50, 'E': 40, 'U': 0}},

    }

    # Function to apply the grade boundaries to the data
    def apply_grade_boundaries(year, subject, marks, grade_boundaries):
        boundaries = grade_boundaries.get(year, {}).get(subject, {})
        for grade, threshold in boundaries.items():
            if marks >= threshold:
                return grade
        return 'U' if pd.notna(marks) else 'N/A'

    # Apply the custom grade boundaries to both datasets
    data_2023['Grade'] = data_2023.apply(
        lambda row: apply_grade_boundaries(row['Year'], 'Mathematic', row['Mathematic'], grade_boundaries_2023), axis=1)
    data_2024['Grade'] = data_2024.apply(
        lambda row: apply_grade_boundaries(row['Year'], 'Mathematic', row['Mathematic'], grade_boundaries_2024), axis=1)

    # Define a function to compare grades and add the appropriate label
    def compare_grades(grade_2023, grade_2024):
        grade_order = ['U', '2', '3', '4', '5', '6', '7', '8', '9', 'F', 'E', 'D', 'C', 'B', 'A', 'A*']

        if grade_2023 == 'N/A' or grade_2024 == 'N/A':
            return 'N/A'

        index_2023 = grade_order.index(grade_2023)
        index_2024 = grade_order.index(grade_2024)

        if index_2024 > index_2023:
            return 'Above'
        elif index_2024 == 15 and index_2023 == 15:
            return 'Above'
        elif index_2024 == index_2023:
            return 'Expected'
        else:
            return 'Below'

    # Add a comparison column to the dataframes
    comparison_results = []

    for i, row in data_2023.iterrows():
        student_2023 = row['Student']
        grade_2023 = row['Grade']
        student_row_2024 = data_2024[data_2024['Student'] == student_2023]
        if not student_row_2024.empty:
            grade_2024 = student_row_2024.iloc[0]['Grade']
            comparison = compare_grades(grade_2023, grade_2024)
        else:
            comparison = 'N/A'
        comparison_results.append({
            'Student': student_2023,
            'Grade 2023': grade_2023,
            'Grade 2024': grade_2024 if not student_row_2024.empty else 'N/A',
            'Comparison': comparison
        })

    comparison_df = pd.DataFrame(comparison_results)
    # Calculate the percentage of Above, Expected, and Below comparisons

    # Add a year group to the comparison DataFrame for better analysis
    comparison_df['Year Group'] = data_2023['Year']

    # Calculate the percentage of Above, Expected, and Below comparisons for each year group
    comparison_counts_excluding_na = comparison_df[comparison_df['Comparison'] != 'N/A'].groupby(
        ['Year Group', 'Comparison']).size().unstack(fill_value=0)
    comparison_counts_excluding_na = (comparison_counts_excluding_na.div
                                      (comparison_counts_excluding_na.sum(axis=1), axis=0) * 100).__round__(0)

    def determine_result(row):
        above = row['Above']
        expected = row['Expected']

        if above >= 74.5 and (above + expected) >= 75:
            return 'OUTSTANDING'
        elif above < 75 and above > 60 and (above + expected) >= 74.5:
            return 'VeryGOOD'
        elif above < 61 and above > 50 and (above + expected) >= 74.5:
            return 'GOOD'
        elif above < 51 and above > 16 and (above + expected) >= 74.5:
            return 'Acceptable'
        elif above < 65 and above > 16 and (above + expected) < 74.5:
            return 'Weak'
        elif above < 16 and above > 0 and (above + expected) < 74.5:
            return 'VeryWeak'
        else:
            return 'N/A'

    # Apply the function to the dataframe
    comparison_counts_excluding_na['Result'] = comparison_counts_excluding_na.apply(determine_result, axis=1)

    def categorize_year_group(year_group):
        primary_years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', 'Year 6']
        secondary_years = ['Year 7', 'Year 8', 'Year 9', 'Year 10', 'Year 11']
        post16_years = ['Year 12', 'Year 13']

        if year_group in primary_years:
            return 'Primary'
        elif year_group in secondary_years:
            return 'Secondary'
        elif year_group in post16_years:
            return 'POST16'
        else:
            return 'Unknown'

    comparison_counts_excluding_na['Category'] = comparison_counts_excluding_na.index.map(categorize_year_group)

    # Aggregate the results by category
    category_summary = comparison_counts_excluding_na.groupby('Category').agg({
        'Above': 'mean',
        'Below': 'mean',
        'Expected': 'mean',
        'Result': 'first'  # This will not work correctly, we need a custom function for correct aggregation of results
    })

    # Define a custom function to determine the aggregated result for each category
    def aggregate_results(df):
        above = df['Above'].mean()
        expected = df['Expected'].mean()

        if above >= 74.5 and (above + expected) >= 74.5:
            return 'OUTSTANDING'
        elif above < 75 and above > 60 and (above + expected) >= 74.5:
            return 'VeryGOOD'
        elif above < 60 and above > 50 and (above + expected) >= 74.5:
            return 'GOOD'
        elif above < 50 and above > 16 and (above + expected) >= 74.5:
            return 'Acceptable'
        elif above < 60 and above > 16 and (above + expected) < 74.5:
            return 'Weak'
        elif above < 16 and above > 0 and (above + expected) < 74.5:
            return 'VeryWeak'
        else:
            return 'N/A'

    # Apply the custom aggregation function
    category_summary['Result'] = comparison_counts_excluding_na.groupby('Category').apply(aggregate_results)
    in_html = category_summary.to_html()
    st.markdown(in_html, unsafe_allow_html=True)
