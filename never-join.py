from locust import HttpUser, task
import json
import random,time

class NeverJoinTest(HttpUser):


  @task
  def win_bid_call(self):
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

    time.sleep(65)

    self.client.post('/win',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
      "records":[
        {
          "key":str(a),
          "value":{
            "status":"win",
            "delay":65
          }
        }
      ]
    })
