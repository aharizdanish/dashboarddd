import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #74ebd5, #ACB6E5);
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("banner.jpg", use_container_width=True)
st.title("""Student Performance Dashboard""")


df = pd.read_csv("Students.data.csv")
df.columns = df.columns.str.strip()
print(df.columns)   
#Filters
classes = st.multiselect("Select Class:", options=df["class"].unique(), default=df["class"].unique())
genders = st.multiselect("Select Gender:", options=df["gender"].unique(), default=df["gender"].unique())

filtered_df = df[(df["class"].isin(classes)) & (df["gender"].isin(genders))]

st.subheader("Summary Statistics")
st.dataframe(filtered_df.describe())
 
st.subheader("Average GPA by Class")

# Use a seaborn light color palette (looks gradient-like)
gradient_palette = sns.color_palette("coolwarm", n_colors=2)

fig1, ax1 = plt.subplots()

sns.barplot(
    data=filtered_df,
    x="class",
    y="GPA",
    hue="gender",
    ax=ax1,
    palette=gradient_palette
)

ax1.set_title("Average GPA by Class and Gender")
st.pyplot(fig1)
  
st.subheader("GPA Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df["GPA"], kde=True, bins=10, ax=ax2)
st.pyplot(fig2)

#This coding used to determined the average GPA for every subjects registered using line chart
st.subheader("Subject-Wise Averages")
subject_cols = ["Algebra", "Calculus 1", "Calculus 2", "Statistics", "Probability", "Number Theory", "Functional Analysis"]
filtered_df.columns = filtered_df.columns.str.strip()
print(filtered_df.columns)
available_subjects = [col for col in subject_cols if col in filtered_df.columns]
avg_subjects = filtered_df[available_subjects].mean()
st.line_chart(avg_subjects)
 
#This coding is specifically use for gender distribution using pie chart
st.subheader("Gender Distribution")
gender_counts = filtered_df["gender"].value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
ax3.axis("equal")
st.pyplot(fig3)

#This coding is specifically use scatter chart to compare between GPA/Gender/Class and subject.
st.subheader("Scatter Chart")
x_column = st.selectbox("Choose x-axis column",df.columns)
y_column = st.selectbox("Choose y-axis column",df.columns)
fig, ax = plt.subplots(figsize = (10,6))
df.plot(kind = 'scatter', x=x_column, y=y_column, ax =ax)
st.pyplot(fig)





