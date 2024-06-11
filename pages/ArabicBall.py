import streamlit as st
import pandas as pd



# Set page Title

def alldata():
    file_2023 = "data/ArabicB2023.csv"
    file_2024 = "data/ArabicB2024.csv"

    @st.cache_data
    def load_data_all(file):
        data = pd.read_csv(file)
        return data

    # Load data
    data_2023_all = load_data_all(file_2023)
    data_2024_all = load_data_all(file_2024)

    # Ensure subject selection matches columns in both datasets
    common_subjects_all = list(set(data_2023_all.columns[2:]).intersection(set(data_2024_all.columns[2:])))
    common_subjects_all.sort()
    if not common_subjects_all:
        st.error("No common subjects found in the provided data files.")
        st.stop()

    # # Sidebar for customization
    # st.sidebar.title("Settings")
    # subject = st.sidebar.selectbox("Select Subject", common_subjects,index=5)
    # year_group = st.sidebar.selectbox("Select Year Group",
    #                                   ['Year 2', 'Year 3', 'Year 4', 'Year 5', 'Year 6', 'Year 7', 'Year 8',
    #                                    'Year 9', 'Year 10', 'Year 11', 'Year 12',  'Year 13'])

    # Sidebar for customization
    subjects_all = "Arabic"
    year_group = ['Year 2', 'Year 3', 'Year 4', 'Year 5', 'Year 6', 'Year 7', 'Year 8',
                                       'Year 9', 'Year 10', 'Year 11', 'Year 12', 'Year 13']

    # Check if the selected subject exists in the grade boundaries for the selected year group

    # Fixed grade boundaries for 2023 for each subject and year group
    grade_boundaries_2023 = {

        'Year 2': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 3': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 4': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 5': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 6': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 7': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 8': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 9': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 10': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 11': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 12': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 13': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        # Add more years as needed
    }

    # Default grade boundaries for 2024 (customizable)
    grade_boundaries_2024 = {

        'Year 2': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 3': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 4': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 5': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 6': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 7': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 8': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 9': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 10': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 11': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 12': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },
        'Year 13': {
            'Arabic': {'A*': 78, 'A': 65, 'B': 55, 'C': 44, 'D': 33, 'E': 23, 'U': 0},

        },

        # Add more years as needed
    }



    def convert_to_grades(data, boundaries):
        grades = []
        for mark in data:
            try:
                mark = int(mark)
                if pd.isna(mark) or not mark:
                    grades.append('N/A')  # Handle missing or invalid marks
                else:
                    for grade, boundary in boundaries.items():
                        if mark >= boundary:
                            grades.append(grade)
                            break
            except ValueError:
                grades.append('N/A')  # Handle non-numeric marks
        return grades

    # Filter and process data
    data_2023_filtered_all = data_2023_all[['Student', 'Year', subjects_all]].copy()
    data_2024_filtered_all = data_2024_all[['Student', 'Year', subjects_all]].copy()

    # Clean and convert marks to numeric values and coerce errors to NaN
    data_2023_filtered_all[subjects_all] = pd.to_numeric(
        data_2023_filtered_all[subjects_all].apply(lambda x: x.strip() if isinstance(x, str) else x), errors='coerce').fillna(
        0).astype(int)
    data_2024_filtered_all[subjects_all] = pd.to_numeric(
        data_2024_filtered_all[subjects_all].apply(lambda x: x.strip() if isinstance(x, str) else x), errors='coerce').fillna(
        0).astype(int)

    for year in year_group:
        data_2023_filtered_all['Grade'] = convert_to_grades(data_2023_filtered_all[subjects_all],
                                                        grade_boundaries_2023[year][subjects_all])
        data_2024_filtered_all['Grade'] = convert_to_grades(data_2024_filtered_all[subjects_all],
                                                        grade_boundaries_2024[year][subjects_all])

    # Merge data for comparison
    comparison_data = pd.merge(data_2023_filtered_all, data_2024_filtered_all, on=['Student', 'Year'],
                               suffixes=('_2023', '_2024'))

    grade_to_value = {'A*': 8, 'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 1, 'U': 0, '9': 9, '8': 8, '7': 7,
                      '6': 6,
                      '5': 5, '4': 4, '3': 3, '2': 2, '1': 1, '0': 0, 'N/A': 'N/A'}

    # Comparison result
    def compare_grades(grade_2023, grade_2024):

        if grade_to_value[grade_2023] == 'N/A' or grade_to_value[grade_2024] == 'N/A':
            return 'N/A'

        elif grade_to_value[grade_2023] < grade_to_value[grade_2024]:
            return 'Above'

        elif grade_to_value[grade_2023] == grade_to_value[grade_2024]:
            if grade_2023 == 'A*' and grade_2024 == 'A*' or grade_2023 == '9' and grade_2024 == '9':
                return 'Above'
            else:
                return 'Expected'
        else:
            return 'Below'

    comparison_data['Comparison'] = comparison_data.apply(
        lambda row: compare_grades(row['Grade_2023'], row['Grade_2024']),
        axis=1)

    def calculate_group_percentages(data, year_groups):
        grouped_data = data[data['Year'].isin(year_groups)]
        comparison_counts = grouped_data['Comparison'].value_counts()
        filter_data = grouped_data[grouped_data['Comparison'] != 'N/A']
        total_comparisons = len(filter_data)
        above_count = comparison_counts.get('Above', 0)
        expected_count = comparison_counts.get('Expected', 0)
        below_count = comparison_counts.get('Below', 0)

        above_percentage = (above_count / total_comparisons) * 100
        expected_percentage = (expected_count / total_comparisons) * 100
        below_percentage = (below_count / total_comparisons) * 100

        return above_percentage, expected_percentage, below_percentage

    year_groups_1_to_6 = ['Year 2', 'Year 3', 'Year 4', 'Year 5', 'Year 6']
    year_groups_7_to_11 = ['Year 7', 'Year 8', 'Year 9', 'Year 10', 'Year 11']
    year_groups_12_to_13 = ['Year 12', 'Year 13']

    above_percentage_1_to_6, expected_percentage_1_to_6, below_percentage_1_to_6 = calculate_group_percentages(
        comparison_data, year_groups_1_to_6)
    above_percentage_7_to_11, expected_percentage_7_to_11, below_percentage_7_to_11 = calculate_group_percentages(
        comparison_data, year_groups_7_to_11)
    above_percentage_12_to_13, expected_percentage_12_to_13, below_percentage_12_to_13 = calculate_group_percentages(
        comparison_data, year_groups_12_to_13)

    # Display results

    def display_comparison_results(g_above_percentage, g_expected_percentage, g_below_percentage, year_range):
        Above_Expected = g_above_percentage + g_expected_percentage
        result = ""
        result_color = ""
        text_color = "black"
        if g_above_percentage >= 75 and Above_Expected >= 75:
            result = "OUTSTANDING"
            result_color = "royalblue"
        elif 75 > g_above_percentage >= 61 and Above_Expected >= 75:
            result = "VERY GOOD"
            result_color = "darkgreen"
        elif 61 > g_above_percentage >= 50 and Above_Expected >= 75:
            result = "GOOD"
            result_color = "green"
        elif 51 >= g_above_percentage >= 1 and Above_Expected >= 75:
            result = "ACCEPTABLE"
            result_color = "yellow"
        elif 60 >= g_above_percentage >= 15 and Above_Expected < 75:
            result = "WEAK"
            result_color = "lightpink"
        elif g_above_percentage < 15 and Above_Expected < 75:
            result = "VERY WEAK"
            result_color = "magenta"
        html_group = f"""
            <table style='width:25%; font-size:20px;margin-left: auto;margin-right: auto;'>
            <tr>
            <th 
            style='width:150px;background-color:lightblue;color:black;border:1px solid black;'>{year_range}</td>
            <th 
            style='width:150px;background-color:{result_color};color:{text_color};border:1px solid black;'>{result}</td>
            </tr>

            """

        st.markdown(f"{html_group}</table>", unsafe_allow_html=True)

    display_comparison_results(above_percentage_1_to_6, expected_percentage_1_to_6, below_percentage_1_to_6, "Primary")
    display_comparison_results(above_percentage_7_to_11, expected_percentage_7_to_11, below_percentage_7_to_11,
                               "Secondary")
    display_comparison_results(above_percentage_12_to_13, expected_percentage_12_to_13, below_percentage_12_to_13,
                               "POST 16")
