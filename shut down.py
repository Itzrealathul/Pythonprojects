def shutdown(input_str):
    if input_str == "Yes":
        return "Shutting down"
    elif input_str == "No":
        return "Canceling shutdown"
    else:
        return "Sorry"