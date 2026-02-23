import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv("student_academic_placement_performance_dataset.csv")

# Basic inspection
print(df.head())
print(df.info())
print(df.describe())


# Styling
sns.set(style="whitegrid")


# 1. Placement vs Academic Performance

academic_vars = [
    "ssc_percentage",
    "hsc_percentage",
    "degree_percentage",
    "cgpa",
    "entrance_exam_score"
]

for var in academic_vars:
    plt.figure()
    sns.boxplot(x="placement_status", y=var, data=df)
    plt.xlabel("Placement Status (0 = Not Placed, 1 = Placed)")
    plt.ylabel(var.replace("_", " ").title())
    plt.title(f"{var.replace('_', ' ').title()} vs Placement Status")
    plt.show()


# 2. Placement vs Skills

skill_vars = [
    "technical_skill_score",
    "soft_skill_score",
    "certifications"
]

for var in skill_vars:
    plt.figure()
    sns.boxplot(x="placement_status", y=var, data=df)
    plt.xlabel("Placement Status (0 = Not Placed, 1 = Placed)")
    plt.ylabel(var.replace("_", " ").title())
    plt.title(f"{var.replace('_', ' ').title()} vs Placement Status")
    plt.show()


# 3. Placement vs Experience

experience_vars = [
    "internship_count",
    "live_projects",
    "work_experience_months"
]

for var in experience_vars:
    plt.figure()
    sns.boxplot(x="placement_status", y=var, data=df)
    plt.xlabel("Placement Status (0 = Not Placed, 1 = Placed)")
    plt.ylabel(var.replace("_", " ").title())
    plt.title(f"{var.replace('_', ' ').title()} vs Placement Status")
    plt.show()


# 4. Correlation Heatmap

corr_columns = [
    "ssc_percentage",
    "hsc_percentage",
    "degree_percentage",
    "cgpa",
    "entrance_exam_score",
    "technical_skill_score",
    "soft_skill_score",
    "internship_count",
    "live_projects",
    "work_experience_months",
    "certifications",
    "attendance_percentage",
    "backlogs",
    "placement_status",
    "salary_package_lpa"
]

corr = df[corr_columns].corr()

plt.figure(figsize=(14, 10))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Student Factors and Placement Outcomes")
plt.show()


# 5. Skills vs Academics (Scatter)

plt.figure()
sns.scatterplot(
    x="cgpa",
    y="technical_skill_score",
    hue="placement_status",
    data=df
)
plt.title("CGPA vs Technical Skill Score by Placement Status")
plt.show()

plt.figure()
sns.scatterplot(
    x="degree_percentage",
    y="soft_skill_score",
    hue="placement_status",
    data=df
)
plt.title("Degree Percentage vs Soft Skill Score by Placement Status")
plt.show()


# 6. Salary Analysis (Placed Students Only)

placed_df = df[df["placement_status"] == 1]

salary_vars = [
    "cgpa",
    "technical_skill_score",
    "soft_skill_score",
    "internship_count",
    "work_experience_months"
]

for var in salary_vars:
    plt.figure()
    sns.scatterplot(
        x=var,
        y="salary_package_lpa",
        data=placed_df
    )
    plt.xlabel(var.replace("_", " ").title())
    plt.ylabel("Salary Package (LPA)")
    plt.title(f"{var.replace('_', ' ').title()} vs Salary Package")
    plt.show()


# 7. Grouped Averages by Placement Status

grouped_means = df.groupby("placement_status")[[
    "cgpa",
    "technical_skill_score",
    "soft_skill_score",
    "internship_count",
    "work_experience_months"
]].mean()

grouped_means.plot(kind="bar")
plt.title("Average Student Metrics by Placement Status")
plt.ylabel("Average Value")
plt.xlabel("Placement Status (0 = Not Placed, 1 = Placed)")
plt.show()
