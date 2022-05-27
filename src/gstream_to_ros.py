#! /bin/python3

import cv2
from cv_bridge import CvBridge, CvBridgeError
import rospy
from sensor_msgs.msg import Image

rov_camera_port = rospy.get_param('/rov_camera_port')
gstreamer_options = f'udpsrc port={rov_camera_port} ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! appsink'
# terminal version: gst-launch-1.0 -e -v udpsrc port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! autovideosink

rospy.init_node('gstream_to_ros_node')
pub = rospy.Publisher('/blue_rov_camera', Image, queue_size=5)
bridge = CvBridge()

cap = cv2.VideoCapture(gstreamer_options)

ret, frame = cap.read()
while ret and not rospy.is_shutdown():

    try:
        img_msg_out = bridge.cv2_to_imgmsg(frame)
        pub.publish(img_msg_out)

    except CvBridgeError as e:
        rospy.logerr(e)
        print(e)
        break
    
    ret, frame = cap.read()

cap.release()

