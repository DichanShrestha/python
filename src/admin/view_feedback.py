import os
FEEDBACK_FILE = 'src/data/feedback_data.txt'
def view_feedback():
    feedback = []
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE) as file:
            feedback = file.readlines
    return feedback
    