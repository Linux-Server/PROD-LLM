from locust import HttpUser, between, task


class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def root(self):
        self.client.post("/")

    
