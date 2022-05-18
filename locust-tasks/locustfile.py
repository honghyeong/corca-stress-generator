from copyreg import constructor
from email import header
from locust import HttpUser, task,TaskSet,between
import json
import random


# class MyTaskSet(TaskSet):
#   @task(8)
#   def bid_call(self):
#     self.client.post('/',json={
#       "records":[
#         {
#           "key":str(random.randint(0,10000)),
#           "value":{
#             "status":"normal bid call"
#           }
#         }
#       ]
#     })

#   @task(2)
#   def win_30_after(self):
#     self.client.post('/',json={
#       "records":[
#         {
#           "key":str(random.randint(0,10000)),
#           "value":{
#             "status":"30a win call"
#           }
#         }
#       ]
#     })

#   @task(1)
#   def win_30_after(self):
#     self.client.post('/',json={
#       "records":[
#         {
#           "key":str(random.randint(0,10000)),
#           "value":{
#             "status":"65a win call"
#           }
#         }
#       ]
#     })

#   @task(1)
#   def win_30_after(self):
#     self.client.post('/',json={
#       "records":[
#         {
#           "key":str(random.randint(0,10000)),
#           "value":{
#             "status":"5b win call"
#           }
#         }
#       ]
#     })

class PerformanceTest(HttpUser):

  def setup(self):
      self.client.post('/',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
      "records":[
        {
          "key":"Test Start",
          "value":{
            "--------------":"-------------"
          }
        }
      ]
    })

  @task(8)
  def bid_call(self):
    self.client.post('/',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
      "records":[
        {
          "key":str(random.randint(0,10000)),
          "value":{
            "status":"normal bid call"
          }
        }
      ]
    })



  @task(2)
  def win_30_after(self):

    tmpKey=random.randint(0,10000)



    self.client.post('/',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
      "records":[
        {
          "key":str(tmpKey),
          "value":{
            "status":"30a bid call"
          }
        }
      ]
    })
    between(30,31)

    self.client.post('/',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
      "records":[
        {
          "key":str(tmpKey),
          "value":{
            "status":"30a win call"
          }
        }
      ]
    })

  # @task(1)
  # def win_65_after(self):
  #   self.client.post('/',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
  #     "records":[
  #       {
  #         "key":str(random.randint(0,10000)),
  #         "value":{
  #           "status":"65a win call"
  #         }
  #       }
  #     ]
  #   })

  # @task(1)
  # def win_5_after(self):
  #   self.client.post('/',headers={"Content-Type":"application/vnd.kafka.json.v2+json"},json={
  #     "records":[
  #       {
  #         "key":str(random.randint(0,10000)),
  #         "value":{
  #           "status":"5b win call"
  #         }
  #       }
  #     ]
  #   })