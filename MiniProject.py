import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.image("banner.jpeg", caption=None)
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
fig1, ax1 = plt.subplots()
sns.barplot(data=filtered_df, x="class", y="GPA", hue="gender", ax=ax1)
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





