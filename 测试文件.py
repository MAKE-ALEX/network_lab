import paramiko
import time
import datetime


class CiscoDevOperator:
    """
    This class is applicable to Cisco ASA and IOS software,
    NX-OS and others are not be test.
    """

    def __init__(
        self,
        ipaddress,
        username,
        password,
        enable_password,
        step_time_sleep=None,
        commands=None,
    ):
        self.enable_password = enable_password
        self.commands = commands

        if step_time_sleep is not None:
            self.step_time_sleep = step_time_sleep
        else:
            self.step_time_sleep = 0.5

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        client.connect(hostname=ipaddress, port=22,
                       username=username, password=password)

        self.channel = client.invoke_shell()
        self.check_enable_mode = False
        self.check_conf_mode = False

    #
    def entering_enable_mode(self):
        self.channel.send("\n")
        time.sleep(self.step_time_sleep)
        first_few_rows = self.channel.recv(500).decode("utf-8")
        if ">" in first_few_rows:
            print("User Mode.")
            if self.enable_password is None:
                print("Missing ENABLE Password")
                self.channel.close()
                return 113
            else:
                self.enable_password = self.enable_password + "\n"
                self.channel.send("enable\n")
                self.channel.send(self.enable_password)
                self.channel.send("\n")
                time.sleep(self.step_time_sleep)
                enter_enable_rows = self.channel.recv(500).decode("utf-8")
                if "#" in enter_enable_rows:
                    print("Entered ENABLE mode SUCCESS!")
                    self.check_enable_mode = True
                else:
                    print(enter_enable_rows)

        elif "#" in first_few_rows:
            print("Enable Mode.")
            self.check_enable_mode = True

        else:
            print(first_few_rows)

    def entering_conf_mode(self):
        if self.check_enable_mode:
            self.channel.send("config terminal\n")
            self.channel.send("\n")
            time.sleep(self.step_time_sleep)
            enter_conf_rows = self.channel.recv(500).decode("utf-8")
            if "(config)#" in enter_conf_rows:
                print("Entered CONFIG mode SUCCESS! ")
                self.check_conf_mode = True
            else:
                print(enter_conf_rows)
        else:
            print("You should enter ENABLE mode before entering "
                  "config mode.")

    def send_commands(self) -> List[List[str]]:
        # Send Multiple Commands
        if not self.enable_mode:
            self.enter_enable_mode()

        _result: List[str] = []
        for command in self.commands:
            # print(command)
            self.channel.send(command + '\n')
            raw_rows, _ = self._boundary_for_interactive(prompt='#')

            self._print_debug_data(
                debug_title=' ISSUE COMMAND: \'%s\' ' % command,
                echo_data=raw_rows
            )

            _raw_rows = raw_rows.split('\n')
            _result.append(_raw_rows)

        return _result

    def send_show_commands(self):
        if self.check_enable_mode:
            self.channel.send("\n")
            echo_raw_data = self.send_commands(command_type="show")
            return echo_raw_data
        else:
            print("You should enter ENABLE mode before excuting the "
                  "show command.")

    def send_config_commands(self):
        if self.check_conf_mode:
            self.channel.send("\n")
            echo_raw_data = self.send_commands(command_type="conf")
            return echo_raw_data
        else:
            print("You should enter CONFIG mode before excuting the "
                  "config command.")

    def _flush_buffer(self, expired_time: int = 30) -> str:
        now = datetime.now().timestamp()
        while not self.channel.recv_ready():
            time.sleep(0.1)
            # When the time took over the expired_time, raise an exception.
            after_while = datetime.now().timestamp()
            print(after_while)
            if after_while - now >= expired_time:
                raise ConnectCiscoDeviceException(
                    'It takes too long to get data from the remote device.')
            else:
                ...

        data = self.channel.recv(1000).decode('utf-8')
        return data

    def _boundary_for_interactive(self, expired_time: int = 30, prompt: str = '') -> Tuple[str, List[str]]:
        boundary_partten = self.boundary_partten + prompt
        target_string = ''
        data = ''
        while re.match(boundary_partten, target_string, re.IGNORECASE) is None:
            time.sleep(0.1)
            data += self._flush_buffer(expired_time=expired_time)
            data_split = data.split('\n')
            target_string = data_split[-1].lstrip(
                '\r').lstrip('\n').rstrip('\r').rstrip('\n')

        return data, data_split

    def close(self):
        self.channel.close()
        self.client.close()