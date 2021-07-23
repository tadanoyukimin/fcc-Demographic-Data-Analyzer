import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = (df["race"].value_counts())

    # What is the average age of men?
    sex_men_mask = df["sex"] == "Male"
    average_age_men = (df[sex_men_mask]["age"].mean()).round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_mask = df["education"] == "Bachelors"
    percentage_bachelors = ((df[bachelors_mask]["education"].count() / df["education"].count()) * 100).round(1)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    high_education_mask = ((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"))
    higher_education = ((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")) & (df["salary"] == ">50K")
    low_education_mask = ((df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")) & (df["salary"] == ">50K")
    lower_education = (df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")
    # a = df[higher_education][greater_than_50]["salary"].count()
    # b = df[lower_education][greater_than_50]["salary"].count()
    # percentage with salary >50K
    higher_education_rich = ((df[higher_education]["education"].count()) / (df[high_education_mask]["education"].count()) * 100).round(1)
    lower_education_rich = ((df[low_education_mask]["education"].count()) / (df[lower_education]["education"].count()) * 100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df["hours-per-week"].min()
    min_work_mask = df["hours-per-week"] == min_work_hours
    min_work_sal = (min_work_mask) & (df["salary"] == ">50K")
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df["hours-per-week"].min()
    rich_percentage = ((df[min_work_mask]["hours-per-week"].count()) / (df[min_work_sal]["salary"].count())).astype(int)

    # What country has the highest percentage of people that earn >50K?
    greater_than_50_mask = df["salary"] == ">50K"
    total_country = df["native-country"].value_counts()
    total_country_50K = df[greater_than_50_mask]["native-country"].value_counts()
    highest_earning_country = (total_country_50K / total_country).idxmax()
    highest_earning_country_percentage = (((total_country_50K / total_country).max()) * 100).round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_mask = (df["native-country"] == "India") & (df["salary"] == ">50K")
    count_india = df[india_mask]["occupation"].value_counts()
    top_IN_occupation = count_india.idxmax()
    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()