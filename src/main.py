from src.model.entity.post import Post
from src.model.entity.user import User
from src.dao.user_dao import UserDao
from src.dao.post_dao import PostDao

#
# if __name__ == '__main__':
#     # admin_user = User("admin", "fess007")
#     user_dao = UserDao()
#     # user_dao.save_user(admin_user)
#     admin_user = user_dao.get_user_by_login("admin")
#
#     post_dao = PostDao()
#     # header = "Sample post with sample text for testing purposes"
#     post_body = """![image](https://uicdn.toast.com/toastui/img/tui-editor-bi.png)
#
# # Awesome Editor!
#
# It has been _released as opensource in 2018_ and has ~~continually~~ evolved to **receive 10k GitHub ⭐️ Stars**.
#
# ## Create Instance
#
# You can create an instance with the following code and use \`getHtml()\` and \`getMarkdown()\` of the [Editor](https://github.com/nhn/tui.editor).
#
# \`\`\`js
# const editor = new Editor(options);
# \`\`\`
#
# > See the table below for default options
# > > More API information can be found in the document
#
# | name | type | description |
# | --- | --- | --- |
# | el | \`HTMLElement\` | container element |
#
# ## Features
#
# * CommonMark + GFM Specifications
#    * Live Preview
#    * Scroll Sync
#    * Auto Indent
#    * Syntax Highlight
#         1. Markdown
#         2. Preview
#
# ## Support Wrappers
#
# > * Wrappers
# >    1. [x] React
# >    2. [x] Vue
# >    3. [ ] Ember"""
#     post1 = Post("Sample post1 with sample text for testing purposes", post_body, admin_user)
#     post_dao.save_post(post1)
#
#     post2 = Post("Sample post2 with sample text for testing purposes", post_body, admin_user)
#     post_dao.save_post(post2)
#
#     post3 = Post("Sample post3 with sample text for testing purposes", post_body, admin_user)
#     post_dao.save_post(post3)
#
#     post4 = Post("Sample post4 with sample text for testing purposes", post_body, admin_user)
#     post_dao.save_post(post4)
# post_dao = PostDao()
# all_posts = post_dao.get_all_active_posts()
# print(all_posts)
# admin_posts = post_dao.get_posts_by_author_id(39)
# print(admin_posts)

# post_dao = PostDao()
# all_posts = post_dao.get_all_active_posts()
# # print("year:", all_posts[0].creation_date.year)
# # print("month:", all_posts[0].creation_date.month)
# # print("day:", all_posts[0].creation_date.day)
# all_posts = sorted(all_posts, key=lambda post: post.creation_date, reverse=True)
# print(all_posts[0].creation_date.strftime("%d %b %Y"))


user_dao = UserDao()
print(user_dao.get_user_by_login("admin"))