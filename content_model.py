class Content:
    def __init__(self, title, body):
        self.title = title
        self.body = body
    def save(self):
        print(f"Saved content: {self.title}")