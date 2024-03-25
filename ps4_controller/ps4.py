import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class PS4ControllerNode(Node):
    def __init__(self):
        super().__init__('ps4_controller_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10)
        self.subscription  # prevent unused variable warning

    def joy_callback(self, msg):
        twist = Twist()
        twist.linear.x = msg.axes[1]  # Left stick vertical axis
        twist.angular.z = msg.axes[3]  # Right stick horizontal axis
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    ps4_controller_node = PS4ControllerNode()
    rclpy.spin(ps4_controller_node)
    ps4_controller_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
