#!/usr/bin/env python3
# Copyright (c) 2018 Intel Corporation. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from datetime import datetime
from nav_msgs.srv import *

def main():
  rclpy.init()

  times = input('How many times do you want to run? ')
  print(
    'The client will send a GetMap request continuously(response contains a size of 10MB array) until receiving %s response times.' % times)
  print('Begin at ' + str(datetime.now()))
  node = rclpy.create_node('stress_client_rclpy')
  client = node.create_client(GetMap, 'get_map')
  request = GetMap.Request()
  totalTimes = int(times)
  receivedTimes = 0

  while rclpy.ok():
    if receivedTimes > totalTimes:
      node.destroy_node()
      rclpy.shutdown()
      print('End at ' + str(datetime.now()))
    else:
      future = client.call_async(request)
      rclpy.spin_until_future_complete(node, future)
      if future.result() is not None:
        receivedTimes += 1

if __name__ == '__main__':
  main()
