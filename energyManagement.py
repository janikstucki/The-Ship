import requests

# data = {
#   "thruster_back": 2,
#   "thruster_front": 1,
#   "thruster_bottom_left": 1,
#   "thruster_front_right": 1,
#   "thruster_bottom_right": 1,
#   "thruster_front_left": 1,
#   "laser": 1,
#   "nuclear_reactor": ,
#   "subspace_tachyon_scanner": 0,
#   "sensor_atomic_field": 0,
#   "matter_stabilizer": 0,
#   "jumpdrive": 0,
#   "sensor_plasma_radiation": 1,
#   "laser_amplifier": 0,
#   "cargo_bot": 1,
#   "scanner": 0,
#   "shield_generator": 0,
#   "sensor_void_energy": 1,
#   "sensor_antimatter": 1,
#   "analyzer_gamma": 0
# }


data = {
  "thruster_back": 2,
  "thruster_front": 1,
  "thruster_bottom_left": 1,
  "thruster_front_right": 1,
  "thruster_bottom_right": 1,
  "thruster_front_left": 1,
  "laser": 1, 
  "nuclear_reactor": 1, 
  "subspace_tachyon_scanner": 0,
  "sensor_atomic_field": 0,
  "matter_stabilizer": 0,
  "jumpdrive": 0,
  "sensor_plasma_radiation": 1,
  "laser_amplifier": 0,
  "cargo_bot": 1, 
  "scanner": 1,
  "shield_generator": 1,
  "sensor_void_energy": 1,
  "sensor_antimatter": 1,
  "analyzer_delta": 1,
  "subspace_tachyon_scanner": 1,
  "sensor_atomic_field": 1,
  "matter_stabilizer": 1,
  "jumpdrive": 0,
  "engine_overdrive": 1,
  "sensor_newton_depth": 1,
}


# data = {
#   "thruster_back": 0,
#   "thruster_front": 0,
#   "thruster_bottom_left": 0,
#   "thruster_front_right": 0,
#   "thruster_bottom_right": 0,
#   "thruster_front_left": 0,
#   "laser": 0, 
#   "nuclear_reactor": 1, 
#   "subspace_tachyon_scanner": 0,
#   "sensor_atomic_field": 0,
#   "matter_stabilizer": 0,
#   "jumpdrive": 0,
#   "sensor_plasma_radiation": 0,
#   "laser_amplifier": 0,
#   "cargo_bot": 0, 
#   "scanner": 0,
#   "shield_generator": 0,
#   "sensor_void_energy": 0,
#   "sensor_antimatter": 1,
#   "analyzer_gamma": 0,
#   "subspace_tachyon_scanner": 0,
#   "sensor_atomic_field": 1,
#   "matter_stabilizer": 1,
#   "jumpdrive": 0.5,
# }




response = requests.put("http://10.255.255.254:2032/limits", json=data)

if response.json()["kind"] == "error":
    response = requests.put("http://10.255.255.254:2033/limits", json=data)

print(response.json())