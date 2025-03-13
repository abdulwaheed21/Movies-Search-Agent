import json

def save_session_log(user_query, ai_response, tool_results):
    """
    Saves session data including user input, AI response, and tool usage.
    """
    session_data = {
        "user_query": user_query,
        "ai_response": ai_response,
        "tool_results": tool_results
    }
    with open("session_log.json", "a") as log_file:
        json.dump(session_data, log_file)
        log_file.write("\n")
