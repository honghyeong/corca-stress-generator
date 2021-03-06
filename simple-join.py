from locust import HttpUser, task
import json
import random
import time

class SimpleJoinTest(HttpUser):


  @task(4)
  def bid_only_call(self):
    a=time.time()
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
  def win_bid_call(self):
    a=time.time()

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
