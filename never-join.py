from ast import Constant
from copyreg import constructor
from email import header
from locust import HttpUser, task,TaskSet,constant,SequentialTaskSet,between
import json
import random

class NeverJoinTest(HttpUser):

    @task
    class NeverJoinTaskSet(SequentialTaskSet):
        wait_time=constant(65)
        key=0
        tmp="never_join"+str(key)

        @task
        def bid_call(self):
            a=self.tmp
            self.client.post('/bid-test',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
            "records":[
                {
                "key":str(a),
                "value":{
                    "status":"lose",
                    "version":"blue",
                    "adset_id":f"adset_{a}",
                    "campaign_id":f"campaign_{a}",
                    "delay":f"{self.wait_time}"
                }
                }
            ]
            })

        @task
        def win_call(self):
            a=self.tmp
            self.client.post('/win-test',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
            "records":[
                {
                "key":str(a),
                "value":{
                    "status":"win"
                }
                }
            ]
            })
            self.key+=1
        
        @task
        def stop(self):
            self.interrupt()
