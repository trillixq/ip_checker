import typer
import processing, ip_api


cli = typer.Typer()

@cli.command()
def check_connection():
    """Check connection to ip-api.com"""
    ip_api.check_connection()

@cli.command()
def get_info(ip: str):
    """Get info by ip"""
    ip_info = ip_api.get_info(ip)
    for key, value in ip_info.items():
        print(f'{key} : {value}')


@cli.command()
def process_file(path: str, save_name: str = "latest.log"):
    """Process file with ips"""
    data = processing.process_file(path)
    save_path = f'logs/{save_name}'
    processing.save_output(save_path, data)
    print(f'saved to {save_path}')


@cli.command()
def process_folder(path: str, save_name: str = "latest.log"):
    """Process files with ips in folder"""
    data = processing.process_folder(path)
    save_path = f'logs/{save_name}'
    processing.save_output(save_path, data)
    print(f'saved to {save_path}')

if __name__ == '__main__':
    cli()