from copyreg import constructor
from email import header
from locust import HttpUser, task,TaskSet,between
import time
import json
import random

class RealisticTimeTest(HttpUser):

    @task(20)
    def bid_only_call(self):
        a=random.randint(0,1000000)
        self.client.post('/bid-test',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
        "records":[
            {
            "key":str(a),
            "value":{
                "status":"lose",
                "version":"blue",
                "adset_id":f"adset_{a}",
                "campaign_id":f"campaign_{a}"
            }
            }
        ]
        })



    @task(5)
    def short_win_bid_call(self):
        a=random.randint(0,1000000)
        slept_time=random.randint(0,5)
        
        self.client.post('/bid-test',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
        "records":[
            {
            "key":str(a),
            "value":{
                "status":"lose",
                "version":"blue",
                "adset_id":f"adset_{a}",
                "campaign_id":f"campaign_{a}"
            }
            }
        ]
        })

        time.sleep(slept_time)

        self.client.post('/win-test',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
        "records":[
            {
            "key":str(a),
            "value":{
                "status":"win",
                "delay":slept_time,
            }
            }
        ]
        })



    @task(1)
    def long_win_bid_call(self):
        a=random.randint(0,1000000)
        slept_time=random.randint(30,70)
        
        self.client.post('/bid-test',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
        "records":[
            {
            "key":str(a),
            "value":{
                "status":"lose",
                "version":"blue",
                "adset_id":f"adset_{a}",
                "campaign_id":f"campaign_{a}"
            }
            }
        ]
        })

        time.sleep(slept_time)

        self.client.post('/win-test',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
        "records":[
            {
            "key":str(a),
            "value":{
                "status":"win",
                "delay":slept_time,
            }
            }
        ]
        })
