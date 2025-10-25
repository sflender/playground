class MessageHistory:
    '''
    Manages message histories, including multi-retrieval and editing.
    '''
    def __init__(self, messages):
        self.messages = messages  # [{"id": int, "text": str, ...}, ...]

    def get_history(self, message_id, limit=10):
        # gets message w/ limit preceding and (limit-1) following messages
        for idx, msg in enumerate(self.messages):
            if msg["id"] == message_id:
                start = max(0, idx - limit)
                end = min(len(self.messages), idx + limit)
                return self.messages[start:end]
        return []
    
    def get_histories(self, message_ids, limit=10):
        # sort message_ids, then get histories and dedup 
        message_ids = sorted(message_ids)
        all_msgs = []
        seen_ids = set()
        for msg_id in message_ids:
            history = self.get_history(msg_id, limit=limit)
            for msg in history:
                if msg["id"] not in seen_ids:
                    all_msgs.append(msg)
                    seen_ids.add(msg["id"])
        return all_msgs 
    
    def edit_message(self, message_id, new_text):
        for msg in self.messages:
            if msg["id"] == message_id:
                msg["history"] = msg.get("history", []) + [msg["text"]]
                msg["text"] = new_text
                return True
        return False
    
if __name__ == "__main__":
    messages = [
        {"id": 1, "text": "Hello"},
        {"id": 2, "text": "How are you?"},
        {"id": 3, "text": "I'm fine, thanks."},
        {"id": 4, "text": "What about you?"},
        {"id": 5, "text": "Doing well!"},
    ]
    history_manager = MessageHistory(messages)
    print(history_manager.get_history(3, limit=2))
    history_manager.edit_message(2, "How have you been?")
    print(history_manager.get_history(2, limit=2))