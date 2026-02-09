import rclpy
from rclpy.lifecycle import Node, State, TransitionCallbackReturn
from std_msgs.msg import String
import time

class SimpleLifecycleNode(Node):
    def __init__(self, node_name, **kwargs):
        super().__init__(node_name, **kwargs)

    def on_configure(self, state:State) -> TransitionCallbackReturn:
        self.pub_ = self.create_subscription(String, "chatter", self.msgCallback, 10)
        self.get_logger().info("Lifecycle Node on_configure() called.")
        return TransitionCallbackReturn.SUCCESS

    def on_shutdown(self, state:State) -> TransitionCallbackReturn:
        self.destroy_subscription(self.pub_)
        self.get_logger().info("Lifecycle Node on_shutdown() called.")
        return TransitionCallbackReturn.SUCCESS
    
    def on_cleanup(self, state:State) -> TransitionCallbackReturn:
        self.destroy_subscription(self.pub_)
        self.get_logger().info("Lifecycle Node on_cleanup() called.")
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state:State) -> TransitionCallbackReturn:
        self.get_logger().info("Lifecycle Node on_activate() called.")
        time.sleep(2)
        return super().on_activate(state)
    
    def on_deactivate(self, state:State) -> TransitionCallbackReturn:
        self.get_logger().info("Lifecycle Node on_deactivate() called.")
        return super().on_deactivate(state)
    
    def msgCallback(self, msg):
        current_state = self._state_machine.current_state
        if current_state[1] == "active":
            self.get_logger().info(f"I heared {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    executor = rclpy.executors.SingleThreadedExecutor()

    node = SimpleLifecycleNode("simple_lifecycle_node")
    executor.add_node(node)
    try:
        executor.spin()
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        node.destroy_node()

if __name__ == '__main__':
    main()