import streamlit as st
import pandas as pd
import os

from pages import Mathall


# Set page Title

def show():
    html_header = f"""<h1 style="text-align: center; color: royalblue">PROGRESS ANAYLSIS MATHEMATICS (2023 JUNE - 2024 JUNE).</h1></br>"""
    # You can add more Streamlit elements below
    st.markdown(html_header, unsafe_allow_html=True)

    # Load data files
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

    comparison_df = pd.DataFrame(comparison_results).copy()
    comparison_df['Year Group'] = data_2023['Year']
    # Calculate the percentage of Above, Expected, and Below comparisons


    # Calculate the percentage of Above, Expected, and Below comparisons for each year group

    comparison_counts_excluding_na = comparison_df[comparison_df['Comparison'] != 'N/A'].groupby(
        ['Year Group', 'Comparison']).size().unstack(fill_value=0)
    comparison_counts_excluding_na = comparison_counts_excluding_na.div(comparison_counts_excluding_na.sum(axis=1),
                                                                            axis=0) * 100
    comparison_counts_excluding_na.__round__(0)


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

    # Display the comparison results

    # Display All Data
    Mathall.alldata()

    # Highlight comparison results

    # html_table = f"""
    # <table style='width:100%; font-size:20px; '>
    #   <tr>
    #     <th style='background-color:green;color:white;border:1px solid black;'>Above</th>
    #     <th style='background-color:yellow;color:black;border:1px solid black;'>Expected</th>
    #     <th style='background-color:red;color:white;border:1px solid black;'>Below</th>
    #   </tr>
    #   <tr>
    #     <td style='background-color:green;color:white;border:1px solid black;'>{above_percentage:.2f}%</td>
    #     <td style='background-color:yellow;color:black;border:1px solid black;'>{expected_percentage:.2f}%</td>
    #     <td style='background-color:red;color:white;border:1px solid black;'>{below_percentage:.2f}%</td>
    #   </tr>
    #     <tr>
    #         <th colspan='3' style='background-color:{result_colors};color:{text_colors};
    #         border:1px solid black;text-align: center;'>{results}</td>
    #   </tr>
    # </table>
    # """
    #
    # # Inject the HTML string into the Streamlit app
    # st.markdown(html_table, unsafe_allow_html=True)
    # # Inject the HTML string into the Streamlit app

    to_html = comparison_counts_excluding_na.to_html()
    st.markdown(to_html, unsafe_allow_html=True)
