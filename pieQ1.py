import plotly.graph_objects as go
from collections import Counter

# Your data
jobs = ["Student", "Student", "Student", "Student", "Student", "Academician", "Academician", "Academician", "Manager", "Manager"]
answers = [
    "Ethical Responsibilities in Research", "For Privacy and Data Protection",
    "To Learn Ethical Responsibilities in IS Career", "To Learn Ethical Responsibilities in IS Career",
    "For Privacy and Data Protection", "Ethical Responsibilities in Research",
    "To Learn Ethical Responsibilities in IS Career", "To Learn Ethical Responsibilities in IS Career",
    "To Learn Ethical Responsibilities in IS Career", "To Learn Ethical Responsibilities in IS Career"
]  # Added a Student response

# Count the frequency of each answer
answer_counts = Counter(answers)

# Create a pie chart
fig = go.Figure(data=[go.Pie(labels=list(answer_counts.keys()), values=list(answer_counts.values()))])

# Update layout for better readability
fig.update_layout(
    title="Why to have computer ethics course in computer related departments?  Distribution of Answers",
)

# Show the plot
fig.show()
fig.write_html('pie_chart.html')
