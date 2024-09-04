import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.attempt_num = 0
        timer_period = 2 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        self.attempt_num += 1
        msg = String()
        msg.data = f'Hello, ROS 2! Attempt is {self.attempt_num}'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
