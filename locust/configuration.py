from locust import HttpUser, task

class main_routes(HttpUser):
    @task
    def main_route(self):
        self.client.get("/")

class ml_routes(HttpUser):
    @task
    def liveness_check_route(self):
        self.client.get("/liveness_check")