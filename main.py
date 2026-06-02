from assistant import assistant

last_id = None
history = []

while True:
    user_question = input()
    
    if user_question.lower() == "sair":
        break

    last_id, history = assistant(user_input=user_question, last_interaction_id=last_id, history=history)