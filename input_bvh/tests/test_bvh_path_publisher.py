import sys
import unittest
import time
import rospy
import rostest
from input_bvh import bvh_path_publisher
    
class TestBvhInput(unittest.TestCase):
    def __init__(self, *args):
        rospy.init_node('test_path_publisher', anonymous=True)
        self.path_pub = rospy.Publisher('bvh_path_topic', String, queue_size=10)

    # Tests if valid file path is sent and published to the bvh_path_topic 
    def test_valid_file_path(self):
        valid_path = '/path/to/valid/file.bvh'
        bvh_path_publisher.path_publisher(valid_path) 
        rospy.sleep(5)  # Allow some time for the message to be published

        # Check if the message was published
        self.assertEqual(rospy.get_published_topics('/bvh_path_topic'), [(u'/bvh_path_topic', 'std_msgs/String')])

    # There should be nothing in bvh_path_topic if invalid input is passed
    def test_invalid_file_path(self):
        invalid_path = '/path/to/invalid/file.bvh'
        bvh_path_publisher.path_publisher(invalid_path)
        rospy.sleep(5)  # Allow some time for the message to be published

        # Check if the message was not published
        self.assertEqual(rospy.get_published_topics('/bvh_path_topic'), [])

if __name__ == "__main__":
    rostest.rosrun('input_bvh', 'test_bvh_path_publisher', TestBvhInput)
