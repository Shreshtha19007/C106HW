import plotly.express as px
import csv
 
with open("student_present.csv") as csv_file :
     df=csv.DictReader(csv_file)
     fig=px.scatter(df,
     x="Roll No",
     y="Marks In Percentage,Days Present",)
     fig.show()