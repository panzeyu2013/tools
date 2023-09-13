import socket

# 创建一个UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 设置发送目标的IP地址和端口号
target_ip = 'ip_address'
target_port = 'port'  # Change this to an integer

# 准备要发送的数据
data = 'str'.encode('utf-8')
print(data)

# 发送数据包
while 1:
    try:
        udp_socket.sendto(data, (target_ip, target_port))
        print("Packet sent successfully")
    except Exception as e:
        print(f"Error: {str(e)}")

# 关闭socket连接
udp_socket.close()
