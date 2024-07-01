# from ..agents.responseAgent import ResponseAgent
# from ..utils import ...


def msg_handler(data):
    messages = data['messages'][:]
    #TODO: Implement the logic for handling messages (fewshots, multi-agents, etc. )
    """
        messages: List[Dict[str, Any]] = [
            {
                "role": "system",
                "content": "Hello! How can I help you today?",
            },
            {
                "role": "user",
                "content": "I want to book a flight",
            },
            ...
        ]
    """ 
    
    
    
    #--------------------------------------------------------------------------
    data['messages'] = messages
    
    return data 