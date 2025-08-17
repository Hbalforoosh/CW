class UserProfile:
    def __init__(self, name, email, data_member):
        self.name = name
        self.email = email
        self.data = data_member
    def __str__(self):
        return f'Name: {self.name} | Email: {self.email} | Data: {self.data}'
    


class PremiumUser:


   
    def delete(self):

    def edite(self):


class Post:
    def __init__(self, content):
        self.content = content
        self.likes = 0
        self.shares = 0
    def like(self):
        self.likes += 1
    def Share(self):
        self.shares += 1

        




class StandardUser:



########################################33
from datetime import datetime

# کلاس پروفایل کاربر
class Profile:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.join_date = datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Joined: {self.join_date}"


# کلاس پست
class Post:
    def __init__(self, content):
        self.content = content
        self.likes = 0
        self.shares = 0

    def like(self):
        self.likes += 1

    def share(self):
        self.shares += 1

    def __str__(self):
        return f"Post: {self.content} | Likes: {self.likes}, Shares: {self.shares}"


# کلاس پایه برای کاربر
class User:
    def __init__(self, profile: Profile):
        self.profile = profile
        self.posts = []  # لیست پست‌های کاربر

    def add_post(self, content):
        post = Post(content)
        self.posts.append(post)
        return post

    def view_posts(self):
        return "\n".join(str(post) for post in self.posts)


# کلاس کاربر استاندارد
class StandardUser(User):
    def __init__(self, profile):
        super().__init__(profile)

    def show_info(self):
        return f"Standard User:\n{self.profile}\nPosts:\n{self.view_posts()}"


# کلاس کاربر ویژه
class PremiumUser(User):
    def __init__(self, profile):
        super().__init__(profile)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            removed = self.posts.pop(index)
            print(f"Deleted Post: {removed.content}")
        else:
            print("Invalid post index!")

    def edit_post(self, index, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].content = new_content
            print("Post updated successfully!")
        else:
            print("Invalid post index!")

    def stats(self):
        total_likes = sum(post.likes for post in self.posts)
        total_shares = sum(post.shares for post in self.posts)
        return f"Total Likes: {total_likes}, Total Shares: {total_shares}"

    def show_info(self):
        return f"Premium User:\n{self.profile}\nPosts:\n{self.view_posts()}\n{self.stats()}"
