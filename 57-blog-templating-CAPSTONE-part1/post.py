class Post:
    def __init__(self, all_posts: list):
        self.all_posts = self.restructure_data(all_posts)

    def restructure_data(self, all_posts: list) -> dict:
        data = {}
        for post in all_posts:
            data[post["id"]] = {
                "title": post["title"],
                "subtitle": post["subtitle"],
                "body": post["body"],
            }
        return data
