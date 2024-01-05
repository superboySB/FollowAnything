import airsim
import cv2
import follow_anything

# 初始化AirSim客户端和Follow Anything
client = airsim.MultirotorClient()
fa = follow_anything.initialize()

while True:
    # 从AirSim获取图像
    img = client.simGetImage(camera_name, image_type)

    # 处理图像并获取跟踪信息
    tracking_info = fa.process_image(img)

    # 根据跟踪信息生成控制指令
    control_commands = generate_control_commands(tracking_info)

    # 向无人机发送控制指令
    client.moveToPositionAsync(control_commands.x, control_commands.y, control_commands.z, velocity)