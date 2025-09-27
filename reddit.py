"""
a simple toy implementation of reddit with post, comment, upvote, downvote functionality.
"""

class Reddit:
    def __init__(self):
        self.posts = {}  # id:(title,content,comment ids)
        self.comments = {}
        self.num_posts = 0  # number of posts, also used as id
        self.num_comments = 0

    def post(self,title,content):
        self.posts[self.num_posts] = {
            'title': title,
            'content': content,
            'upvotes': 0,
            'downvotes': 0,
            'comments': [],  # list of comment ids
        }
        self.num_posts += 1

    def comment(self,post_id,content):
        comment_id = self.num_comments
        self.comments[comment_id] = {
            'content':content,
            'upvotes':0,
            'downvotes':0
        }
        self.posts[post_id]['comments'].append(comment_id)
        self.num_comments += 1

    def upvote_post(self,post_id):
        self.posts[post_id]['upvotes'] += 1

    def downvote_post(self,post_id):
        self.posts[post_id]['downvotes'] += 1   

    def upvote_comment(self,comment_id):
        self.comments[comment_id]['upvotes'] += 1

    def downvote_comment(self,comment_id):
        self.comments[comment_id]['downvotes'] += 1

    def show_post(self,post_id):
        post = self.posts[post_id]
        print(f"Post ID: {post_id}")
        print(f"Title: {post['title']}")
        print(f"Content: {post['content']}")
        print(f"Upvotes: {post['upvotes']}, Downvotes: {post['downvotes']}")
        print("Comments:")
        for comment_id in post['comments']:
            comment = self.comments[comment_id]
            print(f"  Comment ID: {comment_id}, Content: {comment['content']}, Upvotes: {comment['upvotes']}, Downvotes: {comment['downvotes']}")

if __name__ == '__main__':
    reddit = Reddit()
    reddit.post("Hello World","This is my first post")
    reddit.post("Another Post","This is another post")
    reddit.comment(0,"Nice post!")
    reddit.comment(0,"Thanks for sharing")
    reddit.upvote_post(0)
    reddit.upvote_post(0)
    reddit.downvote_post(1)
    reddit.upvote_comment(0)
    reddit.show_post(0)
    reddit.show_post(1)