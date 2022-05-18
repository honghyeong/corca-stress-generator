from copyreg import constructor
from email import header
from locust import HttpUser, task,TaskSet,between
import json
import random

class PerformanceTest(HttpUser):



  @task(4)
  def bid_call(self):
    a=random.randint(0,1000000)
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



  @task(1)
  def win_call(self):
    a=random.randint(0,1000000)
    self.client.post('/win',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
      "records":[
        {
          "key":str(a),
          "value":{
            "status":"win"
          }
        }
      ]
    })
