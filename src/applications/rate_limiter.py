"""
A simple rate limiter, allowing up to max_calls in a given period (in seconds) per user id

"""

import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self):
        self.calls = defaultdict(deque)  # user_id: deque of call timestamps
        self.max_calls = 10
        self.window = 10  # allow no more than max_calls calls in past window seconds

    def call(self, user_id):
        # dummy function
        print(f"successful call by {user_id}")
        return

    def request_call(self, user_id):
        ts = int(time.time())
        calls = self.calls[user_id]

        # Remove calls outside the window
        while calls and calls[0] < ts - self.window:
            calls.popleft()

        if len(calls) >= self.max_calls:
            print(f"no more calls allowed for user {user_id}")
            return False

        self.call(user_id)
        calls.append(ts)
        return True

if __name__=="__main__":
    rl = RateLimiter()
    for _ in range(20):
        rl.request_call(101)

        

    
