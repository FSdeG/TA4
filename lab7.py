import pandas as pd
import numpy as np


# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.

morg_df = pd.read_csv("morg_d07_strings.csv", index_col="h_id")


# TASKS 2-6
# For each of the tasks, print the value requested in the task.

age = morg_df['age']
_1_2_2 = morg_df.loc['1_2_2']
morg_df_4 = morg_df[:4]

### Task 7
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]
for col in TO_CATEGORICALS:
	morg_df[col] = morg_df[col].astype("category")
d = {}
for col in morg_df.columns:
	if any(morg_df[col].isna()):
		d[col] = 0
morg_df.fillna(d, inplace=True)
# Example use of cut()
boundaries = range(16, 89, 8)
morg_df["age_bin"] = pd.cut(morg_df["age"], 
                            bins=boundaries,
                            labels=range(len(boundaries)-1),
                            include_lowest=True, right=False)

### Task 8

boundaries = list(np.linspace(0, 99, 11))
morg_df["hwpw_bin"] = pd.cut(morg_df["hours_worked_per_week"],
                                    bins=boundaries,
                                    labels=range(len(boundaries)-1),
                                    include_lowest=True, right=True)
print("Morg columns types after Task 8")
print(morg_df.dtypes)


hard_workers = morg_df[morg_df["hours_worked_per_week"] >= 35]
not_working = morg_df[morg_df["employment_status"] != "Working"]
filter = (morg_df["hours_worked_per_week"] >= 35) | (morg_df["earnings_per_week"] >=1000)
hard_workers_or_rich = morg_df[filter]

print(morg_df.race.value_counts()[:3])

race_counts = morg_df.groupby('race').size()
print(race_counts)

students = pd.read_csv("data/students.csv")   
extended_grades = pd.read_csv("data/extended_grades.csv")

merged = pd.merge(students, extended_grades, on="UCID")
grades_by_major = merged.groupby(('Major', 'Grade')).size()
grades_by_major_df = grades_by_major.to_frame()
grades_by_major_df = grades_by_major_df.reset_index()
grades_by_major_df.rename(columns={0:'Count'}, inplace=True)
print(grades_by_major_df)