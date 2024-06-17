import rospy
from std_msgs.msg import String

def hello_publisher():
    rospy.init_node('hello_publisher', anonymous = True)
    pub = rospy.Publisher('Hello_topic', String, queue_Size=10)  
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        massage = "Hello, Solrac!!!!"
        rospy.loginof(massage)
        pub.publish(massage)
        rate.sleep()

if __name__ == '__main__':
    try:
        hello_publisher()
    except rospy.ROSInterrupException:
            pass