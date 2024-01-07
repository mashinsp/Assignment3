class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def like_post(self, post):
        post.add_like(self)

class Admin(User):
    def __init__(self, user_id, username, email, password):
        super().__init__(user_id, username, email, password)

    def manage_user_roles(self, user, role):
        # Implementation to manage user roles (e.g., promote to admin, demote to regular user)
        pass

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []

    def add_like(self, user):
        self.likes.append(user)

# Example usage:
regular_user = User(1, "user123", "user123@example.com", "password123")
admin_user = Admin(2, "admin123", "admin123@example.com", "adminpassword")

post1 = regular_user.create_post("This is a regular user's post.")
admin_user.like_post(post1)
