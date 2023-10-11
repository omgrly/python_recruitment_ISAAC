import rclpy
from std_msgs.msg import Float32
from datetime import datetime


class TemperatureLogger:
    def __init__(self, filename: str):
        self.filename = filename
    
    def callback(self, temperature: Float32):
        temp = temperature.float
        if temp>=50:
            with open(self.filename, 'a') as f:
                f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' - TEMP REACHED: ' + str(temp) + '\n')


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
