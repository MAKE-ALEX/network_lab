from .demo import send_command_to_device

# 定义交换机的连接信息
devices = {
    'device_type': 'cisco_ios',  # 设备类型，这里是Cisco IOS设备
    'ip': '192.168.66.10',
    'username': 'cisco',
    'password': 'cisco',
    # 'secret': 'cisco',  # 如果有特权模式密码，请提供，否则可以省略
}

def test_happy_path_valid_device_and_command(self, mocker):
    # Mock the ConnectHandler function to return a dummy output
    mocker.patch('netmiko.ConnectHandler', return_value=mocker.Mock(send_command=mocker.Mock(return_value='output')))

    # Call the function with valid device and command inputs
    output = send_command_to_device(devices, 'show version')

    # Assert that the output is not None and is equal to the expected output
    assert output is not None
    assert output == 'output'
