from locust import HttpUser, between, task


class WorkUser(HttpUser):
    wait_time = between(0, 0)

    @task
    def hit_work(self):
        self.client.get("/work")
