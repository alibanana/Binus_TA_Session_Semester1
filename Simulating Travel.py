time = int(input ("Time Spent = "))
acc = int(input ("Acceleration = "))
dist = int(input ("Distance = "))
velocity = time * acc
s = (1/2)*acc*time**2

for i in range (0, time + 1) :
    dist_sec = (1 / 2) * acc * i * i
    star = int(dist_sec/10)
    print("Duration: ", i,"Distance: ", "*" * star)

#final velocity
if velocity > 60:
    print ("The person went over the speed limit.", "(Max speed was",velocity, "m/s)")
else:
    print ("The person did not went over the speed limit.", "(Max speed was",velocity, "m/s)")

#final distance
if s >= dist :
    print ("The person reached the destination."," (Reached",s,"m)")
elif s < dist:
    print ("The person did not reached the destination.", " (Reached", s, "m)")