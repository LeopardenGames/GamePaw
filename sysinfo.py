import platform
import psutil
import subprocess

def get_system_info():
    info = {}

    # Betriebssystem
    info['OS'] = platform.system()
    info['OS_version'] = platform.version()
    info['OS_release'] = platform.release()
    info['Architecture'] = platform.architecture()[0]

    # CPU
    info['CPU'] = platform.processor()
    info['CPU_cores'] = psutil.cpu_count(logical=False)
    info['Logical_cores'] = psutil.cpu_count(logical=True)
    info['CPU_frequency'] = psutil.cpu_freq().current

    # RAM
    mem = psutil.virtual_memory()
    info['RAM_total'] = mem.total
    info['RAM_available'] = mem.available

    # GPU
    try:
        # Versucht die GPU-Informationen mit 'lspci' (Linux) oder 'wmic' (Windows) zu ermitteln
        if info['OS'] == 'Linux':
            gpu_info = subprocess.check_output("lspci | grep VGA", shell=True).decode().strip()
            info['GPU'] = gpu_info
        elif info['OS'] == 'Windows':
            gpu_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode().strip().split('\n')[1]
            info['GPU'] = gpu_info
        else:
            info['GPU'] = 'Unbekannt'
    except Exception as e:
        info['GPU'] = f'Fehler beim Abrufen der GPU-Informationen: {e}'

    return info

def write_conf_file(filename, info):
    with open(filename, 'w') as f:
        for key, value in info.items():
            f.write(f"{key} = {value}\n")

if __name__ == '__main__':
    system_info = get_system_info()
    write_conf_file('config/system_info.conf', system_info)
    print("Systeminformationen wurden in 'system_info.conf' gespeichert.")
