import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from custom_msgs.action import Fibonacci
import time

class SimpleActionServer(Node):
    def __init__(self):
        super().__init__('simple_action_server')
        self.action_server = ActionServer(self, Fibonacci, "fibonacci", self.goalCallback)
        self.get_logger().info("Starting the server.")

    def goalCallback(self, goal_handel):
        self.get_logger().info(f"Recevied goal request with order {goal_handel.request.order}")
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]

        for i in range(1, goal_handel.request.order):
            feedback_msg.partial_sequence.append(feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info(f"Feedback: {feedback_msg.partial_sequence}")
            goal_handel.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handel.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence
        return result


def main(args=None):
    rclpy.init(args=args)
    node = SimpleActionServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()