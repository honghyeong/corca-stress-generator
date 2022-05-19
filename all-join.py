from locust import HttpUser, task
import time
import json
import random

class AllJoinTest(HttpUser):

    @task
    def win_bid_call(self):
        a=random.randint(0,1000000)
        slept_time=random.randint(5,30)
        
        self.client.post('/bid',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
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

        self.client.post('/win',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
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
