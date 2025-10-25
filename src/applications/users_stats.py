
'''
given a set of logs of the form
"YYYYMMDD user_id page_id"
get the 
- users that have visited the most unique days
- users that have visited the most unique pages
'''

from collections import defaultdict

def users_with_most_unique_days(logs):
    d = defaultdict(set)  # key: user_id, value: set of unique days
    for log in logs:
        date, user_id, page_id = log.split()
        d[user_id].add(date)

    max_days = max(len(days) for days in d.values())
    result = [u for u in d if len(d[u]) == max_days]
    return result, max_days

def users_with_most_unique_pages(logs):
    d = defaultdict(set)  # key: user_id, value: set of unique pages
    for log in logs:
        date, user_id, page_id = log.split()
        d[user_id].add(page_id)

    max_pages = max(len(pages) for pages in d.values())
    result = [u for u in d if len(d[u]) == max_pages]
    return result, max_pages

if __name__ == "__main__":
    logs = [
        "20230101 user1 pageA",
        "20230101 user1 pageB",
        "20230102 user1 pageA",
        "20230101 user2 pageA",
        "20230102 user2 pageB",
        "20230103 user2 pageC",
        "20230101 user3 pageA",
        "20230102 user3 pageA",
        "20230103 user3 pageA",
    ]

    users_days, num_days = users_with_most_unique_days(logs)
    print(f"Users with most unique days ({num_days} days): {users_days}")

    users_pages, num_pages = users_with_most_unique_pages(logs)
    print(f"Users with most unique pages ({num_pages} pages): {users_pages}")