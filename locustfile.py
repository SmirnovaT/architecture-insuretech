from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:46797/"

    @task
    def index(self):
        self.client.get("/")