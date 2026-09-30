import os
import re
import json

import ip_api

ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')



def get_ips(text: str):
    ips = re.findall(ip_pattern, text)
    return ips

def process_file(path: os.PathLike | str):
    with open(path, 'r') as f:
        f_data = f.read()
        ips = get_ips(f_data)

        output = {}
        for ip in ips:
            ip_info = ip_api.get_info(ip)
            output[ip] = ip_info

        f.close()
        return output

def process_folder(path: os.PathLike | str):
    folder_data = {}

    with os.scandir(path) as folder:
        for f in folder:
            if f.is_file():
                data = process_file(f)
                folder_data[f.name] = data

    return folder_data

def write_data(path: os.PathLike | str, data: str | dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        f.close()

def save_output(path: os.PathLike | str, data: str | dict):
    if not os.path.isfile(path) or os.path.basename(path) == 'latest.log':
        write_data(path, data)
    else:
        filename, extension = os.path.splitext(path)
        counter = 1

        while os.path.exists(path):
            path = filename + f'_{counter}' + extension
            counter += 1

        write_data(path, data)

if __name__ == '__main__':
    data = process_file('logs/t776261z.beget.tech.access.log.20260927')
    save_output('output_logs/output.log', data)


