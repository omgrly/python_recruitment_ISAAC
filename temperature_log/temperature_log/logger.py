import rclpy
from std_msgs.msg import Float32


# add your code here!


def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('temperature_logger')
    node.get_logger().info("Hello! Temperature logger node started!")

    tl = TemperatureLogger('log.txt')
    sub = node.create_subscription(Float32, "temperature", tl.callback, 10)

    rclpy.spin(node)


if __name__ == '__main__':
    tl = TemperatureLogger('log.txt')
    main()
