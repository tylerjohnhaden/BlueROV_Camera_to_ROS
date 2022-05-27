#! /bin/bash

gst-launch-1.0 -e -v udpsrc port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! autovideosink
