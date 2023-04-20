f = """header: 
  seq: 752524
  stamp: 
    secs: 37799
    nsecs: 412432512
  frame_id: "/map"
pose: 
  position: 
    x: 88.427696228
    y: -132.174438477
    z: 0.0258977413177
  orientation: 
    x: 0.00418269732948
    y: -0.000256976539301
    z: 0.997816143848
    w: 0.0659195121555
---

"""

print(f.find("---"))
print(f[:f.find("---")])
