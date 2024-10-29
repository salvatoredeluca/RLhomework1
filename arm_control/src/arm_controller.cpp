#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include <vector>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "sensor_msgs/msg/joint_state.hpp"
#include  "std_msgs/msg/float64_multi_array.hpp"

using std::placeholders::_1;
using namespace std::chrono_literals;



class ArmControllerNode : public rclcpp::Node
{
public:
  ArmControllerNode()
  : Node("arm_controller_node")
  {
    subscription_ = this->create_subscription<sensor_msgs::msg::JointState>(
      "joint_states", 10, std::bind(&ArmControllerNode::topic_callback, this, _1));

    publisher_ = this->create_publisher<std_msgs::msg::Float64MultiArray>("/position_controller/commands", 10);

    timer_ = this->create_wall_timer(
      20ms, std::bind(&ArmControllerNode::publish_once, this));

    publish_once();
      
  }

private:
  void topic_callback(const sensor_msgs::msg::JointState::SharedPtr msg) const
  {
    
    RCLCPP_INFO(this->get_logger(), "Received JointState:");
    
    for (size_t i = 0; i < msg->name.size(); ++i) {
      RCLCPP_INFO(this->get_logger(), "Joint: '%s', Position: '%f'", msg->name[i].c_str(), msg->position[i]);
    }
    
    
  }
  rclcpp::Subscription<sensor_msgs::msg::JointState>::SharedPtr subscription_;

   void publish_once()
  {
    auto message = std_msgs::msg::Float64MultiArray();
    message.data = {0 ,-0.5, -0.5 ,0};
   
    publisher_->publish(message);
  }

  rclcpp::Publisher<std_msgs::msg::Float64MultiArray>::SharedPtr publisher_;
  
  rclcpp::TimerBase::SharedPtr timer_;
};
 


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ArmControllerNode>());
  rclcpp::shutdown();
  return 0;
}