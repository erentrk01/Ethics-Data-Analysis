import plotly.graph_objects as go
from collections import defaultdict

# data
jobs = [ "Student","Student","Student", "Student","Student", "Academician", "Academician", "Academician","Manager","Manager"]
answers = [
            "Ethical Responsibilities in Research","For Privacy and Data Protection", "To Learn Ethical Responsibilities in IS Career", "To Learn Ethical Responsibilities in IS Career", "For Privacy and Data Protection", "Ethical Responsibilities in Research","To Learn Ethical Responsibilities in IS Career", "To Learn Ethical Responsibilities in IS Career", "To Learn Ethical Responsibilities in IS Career", "To Learn Ethical Responsibilities in IS Career", "To Learn Ethical Responsibilities in IS Career"]  # Added a Student response

# Create a dictionary to store answer counts for each job
answer_counts_by_job = defaultdict(lambda: defaultdict(int))

# Count the frequency of each answer for each job
for job, answer in zip(jobs, answers):
    answer_counts_by_job[answer][job] += 1

# Define colors for each job type
job_colors = {'Manager': 'blue', 'Academician': 'green', 'Student': 'orange'}

# Create a bar chart
fig = go.Figure()

# Add bars for each answer and job type
for job in set(jobs):
    counts = {answer: answer_counts_by_job[answer][job] for answer in answer_counts_by_job}
    fig.add_trace(go.Bar(x=list(counts.keys()), y=list(counts.values()), name=job, marker=dict(color=job_colors[job])))

# Update layout for better readability
fig.update_layout(
    title="Why to have computer ethics course in computer related departments? Distribution of Answers Based on Jobs",
    xaxis_title="Answer",
    yaxis_title="Frequency",
    barmode="group",  # This creates grouped bars
    xaxis=dict(tickangle=-50),  # Rotate x-axis labels for better readability
    yaxis=dict(dtick=1),  # Set y-axis intervals to 1
)

# Show the plot
fig.show()
fig.write_html('chart.html')
