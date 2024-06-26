import streamlit as st
import pandas as pd
import os
from pages import ArabicAall

# Set page Title
def show():
    html_header = f"""<h1 style="text-align: center; color: royalblue">PROGRESS ANAYLSIS ARABIC (ARAB) (2023 JUNE - 2024 JUNE).</h1></br>"""
    # You can add more Streamlit elements below
    st.markdown(html_header, unsafe_allow_html=True)

    # Load data files
    file_2023 = "data/ArabicA2023.csv"
    file_2024 = "data/ArabicA2024.csv"

    @st.cache_data
    def load_data(file):
        data = pd.read_csv(file)
        return data

    # Load data
    data_2023 = load_data(file_2023)
    data_2024 = load_data(file_2024)
    # Ensure subject selection matches columns in both datasets
    common_subjects = list(set(data_2023.columns[2:]).intersection(set(data_2024.columns[2:])))
    common_subjects.sort()
    if not common_subjects:
        st.error("No common subjects found in the provided data files.")
        st.stop()

    # Sidebar for customization
    st.sidebar.title("Subject")
    subject = "Arabic"
    st.sidebar.subheader(subject)
    year_group = st.sidebar.selectbox("Select Year Group",
                                      ['Year 3', 'Year 4', 'Year 5', 'Year 6', 'Year 7', 'Year 8',
                                       'Year 9', 'Year 10','Year 11', 'Year 12', 'Year 13'])

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

    if subject not in grade_boundaries_2023[year_group] or subject not in grade_boundaries_2024[year_group]:
        st.error(f"The subject {subject} is not available in {year_group}.")
        st.stop()
    # Allow customization of grade boundaries for 2024 only
    # Display grade boundaries for 2023
    st.sidebar.subheader("Grade Boundaries for 2023")
    boundaries_2023 = grade_boundaries_2023[year_group][subject]
    for grade, boundary in boundaries_2023.items():
        st.sidebar.text(f"Boundary for {grade}: {boundary}")

    # Display grade boundaries for 2024
    st.sidebar.subheader("Grade Boundaries for 2024")
    boundaries_2024 = grade_boundaries_2024[year_group][subject]
    for grade, boundary in boundaries_2024.items():
        st.sidebar.text(f"Boundary for {grade}: {boundary}")

    # Convert marks to grades based on defined boundaries
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
    data_2023_filtered = data_2023[['Student', 'Year', subject]].copy()
    data_2024_filtered = data_2024[['Student', 'Year', subject]].copy()

    # Clean and convert marks to numeric values and coerce errors to NaN
    data_2023_filtered[subject] = pd.to_numeric(
        data_2023_filtered[subject].apply(lambda x: x.strip() if isinstance(x, str) else x), errors='coerce').fillna(
        0).astype(int)
    data_2024_filtered[subject] = pd.to_numeric(
        data_2024_filtered[subject].apply(lambda x: x.strip() if isinstance(x, str) else x), errors='coerce').fillna(
        0).astype(int)

    data_2023_filtered['Grade'] = convert_to_grades(data_2023_filtered[subject],
                                                    grade_boundaries_2023[year_group][subject])
    data_2024_filtered['Grade'] = convert_to_grades(data_2024_filtered[subject], boundaries_2024)

    # Merge data for comparison
    comparison_data = pd.merge(data_2023_filtered, data_2024_filtered, on=['Student', 'Year'],
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
    st.subheader("Student's Progress (June 2023 - June 2024) in Arabic (Arab)")

    ArabicAall.alldata()

    # Display data

    # Highlight comparison results
    def color_comparison(val):
        color = 'black'
        if val == 'Above':
            color = 'green'
        elif val == 'Expected':
            color = 'yellow'
        elif val == 'Below':
            color = 'red'
        elif val == 'N/A':
            color = 'grey'
        return f'background-color: {color}'



    year_comparison_data = comparison_data[comparison_data['Year'] == year_group]

    st.subheader(f"Grades Comparison for (2023 June and 2024 June in Arabic (Arab) {year_group}")
    st.markdown("</br>", unsafe_allow_html=True)
    st.dataframe(year_comparison_data.style.applymap(color_comparison, subset=['Comparison']))

    with pd.ExcelWriter('styled_dataframe.xlsx', engine='openpyxl') as writer:
        year_comparison_data.style.applymap(color_comparison, subset=['Comparison']).to_excel(writer, index=False)

    # Provide a download link for the Excel file
    with open('styled_dataframe.xlsx', 'rb') as f:
        st.download_button(
            label="Download Data as Excel",
            data=f,
            file_name='styled_dataframe.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

    # Remove the temporary file
    os.remove('styled_dataframe.xlsx')

    # Bar Graph for Comparison
    comparison_counts = year_comparison_data['Comparison'].value_counts()

    # Calculate percentages for Above, Expected, and Below
    filter_data = year_comparison_data[year_comparison_data['Comparison'] != 'N/A']
    total_comparisons = len(filter_data)
    above_count = comparison_counts.get('Above', 0)
    expected_count = comparison_counts.get('Expected', 0)
    below_count = comparison_counts.get('Below', 0)

    above_percentage = (above_count / total_comparisons) * 100
    expected_percentage = (expected_count / total_comparisons) * 100
    below_percentage = (below_count / total_comparisons) * 100
    Progress_Evaluation = above_percentage + expected_percentage
    results = ""
    result_colors = ""
    text_colors = "black"
    Above_Expected = above_percentage + expected_percentage

    st.subheader(f"Comparison Results for {year_group}")

    # Define the HTML string for the table
    if above_percentage >= 75 and Above_Expected >= 75:
        results = "OUTSTANDING"
        result_colors = "royalblue"
    elif 75 > above_percentage >= 61 and Above_Expected >= 75:
        results = "VERY GOOD"
        result_colors = "darkgreen"
    elif 60 > above_percentage >= 50 and Above_Expected >= 75:
        results = "GOOD"
        result_colors = "green"
    elif 51 >= above_percentage >= 1 and Above_Expected >= 75:
        results = "ACCEPTABLE"
        result_colors = "yellow"
    elif 65 >= above_percentage >= 15 and Above_Expected < 75:
        results = "WEAK"
        result_colors = "lightpink"
    elif above_percentage < 15 and Above_Expected < 75:
        results = "VERY WEAK"
        result_colors = "magenta"
    html_table = f"""
    <table style='width:100%; font-size:20px; '>
      <tr>
        <th style='background-color:green;color:white;border:1px solid black;'>Above</th>
        <th style='background-color:yellow;color:black;border:1px solid black;'>Expected</th> 
        <th style='background-color:red;color:white;border:1px solid black;'>Below</th>
      </tr>
      <tr>
        <td style='background-color:green;color:white;border:1px solid black;'>{above_percentage:.2f}%</td>
        <td style='background-color:yellow;color:black;border:1px solid black;'>{expected_percentage:.2f}%</td> 
        <td style='background-color:red;color:white;border:1px solid black;'>{below_percentage:.2f}%</td>
      </tr>
        <tr>
            <th colspan='3' style='background-color:{result_colors};color:{text_colors};
            border:1px solid black;text-align: center;'>{results}</td>
      </tr>
    </table>
    """

    # Inject the HTML string into the Streamlit app
    st.markdown(html_table, unsafe_allow_html=True)
    # Inject the HTML string into the Streamlit app
