import plotly.graph_objects as go

# Define the subjects
subjects = [" Real-life Ethical Dilemmas", "Legal Compliance", "Privacy and Data Protection", "Mitigating ethical issues of emerging technologies", "Professional Responsibility", "Social Impact","Philosphical Discussion and history of Ethics"]

# Participant answers and ratings
participant_answers = {
 # Rating on a scale from 1 to 5
	"Doruk Fişek": [5, 2, 3, 4, 4, 3,5,5],
	"Hakan Kılınç": [3, 2, 3, 5, 5, 5,2],
	"Kenan Köroğlu": [5, 2, 2, 2, 4, 2,2],
	"Umut Hüseyinoğlu": [3, 2, 5, 2, 4, 3,5],
	"Seyid Amjad": [3, 3, 3, 5, 5, 5,2],



}

# Calculate average ratings for each subject
average_ratings = {subject: sum(participant_answers[participant][i] for participant in participant_answers) / len(participant_answers) for i, subject in enumerate(subjects)}

# Create a spider chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=list(average_ratings.values()),
    theta=subjects,
    fill='toself',
    line=dict(color='blue'),
    marker=dict(size=8),
))

# Update layout for better readability
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 5]  # Adjust the range based on your scale
        )
    ),
    showlegend=False,
    title="Which subjects are important?(student participants excluded) ",
)

# Show the plot
fig.show()
fig.write_html('spider_excludeStudents.html')
