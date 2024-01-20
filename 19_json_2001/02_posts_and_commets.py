import requests as req


posts = 'https://jsonplaceholder.typicode.com/posts'
comments = 'https://jsonplaceholder.typicode.com/comments'
posts = req.get(posts)
comments = req.get(comments)
posts_json = posts.json()
comments_json = comments.json()

posts_with_comments = []
for post in posts_json:
    comment_count = 0
    for comment in comments_json:
        if comment['postId'] == post['id']:
            comment_count += 1
    posts_with_comments.append({'id': post['id'], 'post_title': post['title'], 'comments': comment_count})

print(posts_with_comments)
