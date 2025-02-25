import streamlit as st
from collections import Counter

# Define the mapping of responses to blended learning models
response_to_model_mapping = {
    "question_1": {  # How do you prefer to learn new concepts?
        "a": ["Station Rotation", "Flipped Classroom"],  # Live classroom with direct teacher interaction
        "b": ["Flex Model", "A La Carte", "Enriched Virtual"],  # Self-paced online modules
        "c": ["Enriched Virtual"]  # Mix of live sessions and online resources
    },
    "question_2": {  # How much self-motivation do you have to complete tasks?
        "a": ["Flex Model", "Enriched Virtual"],  # High
        "b": ["Flipped Classroom"],  # Moderate
        "c": ["Station Rotation", "Face-to-Face Driver"]  # Low
    },
    "question_3": {  # How comfortable are you with technology?
        "a": ["Flex Model", "A La Carte", "Enriched Virtual"],  # Very comfortable
        "b": ["Enriched Virtual", "Flipped Classroom"],  # Somewhat comfortable
        "c": ["Face-to-Face Driver"]  # Not comfortable
    },
    "question_4": {  # Does the content involve hands-on activities or labs?
        "a": ["Lab Rotation"],  # Yes
        "b": ["Flex Model", "Flipped Classroom", "Enriched Virtual"]  # No
    },
    "question_5": {  # Is the subject theoretical or skills-based?
        "a": ["Enriched Virtual", "Flipped Classroom"],  # Mostly theoretical
        "b": ["Lab Rotation", "Station Rotation"]  # Mostly skills-based
    },
    "question_6": {  # Does the content require real-time collaboration?
        "a": ["Station Rotation", "Flipped Classroom"],  # Frequently
        "b": ["Enriched Virtual"],  # Occasionally
        "c": ["Flex Model", "Enriched Virtual"]  # Rarely
    },
    "question_7": {  # How important is flexibility?
        "a": ["Flex Model", "A La Carte"],  # Gaining theoretical knowledge
        "b": ["Flipped Classroom", "Enriched Virtual"],  # Developing practical skills
        "c": ["Station Rotation", "Face-to-Face Driver"]  # Preparing for exams or certifications
    }
}

# Function to recommend the most suitable blended learning model(s)
def recommend_model(responses):
    # Validate input
    if len(responses) != 7:
        return "Error: Please provide exactly 7 responses (one for each question)."

    # Aggregate model recommendations
    model_counts = Counter()
    for i, response in enumerate(responses):
        question_key = f"question_{i + 1}"
        if response in response_to_model_mapping[question_key]:
            model_counts.update(response_to_model_mapping[question_key][response])

    # Get the top 3 most frequent models
    top_models = model_counts.most_common(3)

    # Calculate total count of the top 3 models
    total_top_counts = sum(count for model, count in top_models)

    # Format the top models with their percentages
    recommended_models = []
    for model, count in top_models:
        percentage = (count / total_top_counts) * 100
        recommended_models.append(f"{model} ({percentage:.1f}%)")

    return recommended_models

# Streamlit UI
st.title("Blended Learning Model Recommendation System")

# Questions and options
questions = [
    "How do you prefer to learn new concepts?",
    "How much self-motivation do you have to complete tasks?",
    "How comfortable are you with technology?",
    "Does the content involve hands-on activities or labs?",
    "Is the subject theoretical or skills-based?",
    "Does the content require real-time collaboration?",
    "How important is flexibility?"
]

options = [
    ["a) In a live classroom with direct teacher interaction", "b) Through self-paced online modules", "c) A mix of live sessions and online resources"],
    ["a) High", "b) Moderate", "c) Low"],
    ["a) Very comfortable", "b) Somewhat comfortable", "c) Not comfortable"],
    ["a) Yes", "b) No"],
    ["a) Mostly theoretical", "b) Mostly skills-based"],
    ["a) Frequently", "b) Occasionally", "c) Rarely"],
    ["a) Gaining theoretical knowledge", "b) Developing practical skills", "c) Preparing for exams or certifications"]
]

# Collect user responses
responses = []
for i, question in enumerate(questions):
    st.write(f"**Question {i + 1}:** {question}")
    response = st.radio(f"Select an option for Question {i + 1}:", options[i], index=None, key=f"q{i + 1}")  # No preselected option
    if response is None:
        st.warning("Please select an option for all questions.")
        st.stop()  # Stop execution if any question is unanswered
    responses.append(response[0])  # Extract the first character (a, b, c) from the selected option

# Submit button
if st.button("Submit"):
    # Get recommended models
    recommended_models = recommend_model(responses)
    
    # Display the result
    if isinstance(recommended_models, str):  # Error message
        st.error(recommended_models)
    else:
        st.success("Recommended Blended Learning Models:")
        for model in recommended_models:
            st.write(f"- {model}")
