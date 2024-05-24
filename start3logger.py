import os
import subprocess
import sys
import psutil
import logging

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VIRTUALENV_ROOT = os.path.join(SCRIPT_DIR, '.venv') 
LOG_FILE = os.path.join(SCRIPT_DIR, 'start_log.txt')

SERVICES = {
    'bus': 'mycroft.messagebus.service',
    'skills': 'mycroft.skills',
    'audio': 'mycroft.audio',
    'voice': 'mycroft.client.speech',
    'cli': 'mycroft.client.text',
    'audiotest': 'mycroft.util.audio_test',
    'wakewordtest': 'test.wake_word',
    'enclosure': 'mycroft.client.enclosure'
}

# Configuration du logging pour inclure des détails supplémentaires dans un fichier start_log.txt
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def help():
    print(f"{sys.argv[0]}: Mycroft command/service launcher")
    print("usage: {} [COMMAND] [restart] [params]".format(sys.argv[0]))
    print()
    print("Services COMMANDs:")
    # print commands
    print()
    print("Tool COMMANDs:") 
    # print tool commands
    print()
    print("Options:")
    print(" restart                  (optional) Force the service to restart if running")
    print()
    print("Examples:")
    print(f" {sys.argv[0]} all")
    print(f" {sys.argv[0]} all restart")
    print(f" {sys.argv[0]} cli")
    sys.exit(1)

def process_running(name):
    module = SERVICES[name]
    
    for p in psutil.process_iter(['cmdline']):
        try:
            cmdline = p.info.get('cmdline')
            if cmdline and module in cmdline: # Windows
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

def launch_process(name, args):
    module = SERVICES[name]
    logging.info("Starting %s", name)
    subprocess.call(['python', '-m', module] + args)

def require_process(name):
    module = SERVICES[name]
    if not any(module in p.name() for p in psutil.process_iter()):
        launch_background(name)

def launch_background(name):
    module = SERVICES[name]
    
    log_dir = os.path.join(SCRIPT_DIR, 'log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, f'{name}.log')

    if not process_running(name):
        logging.info("Starting background service %s", name)
        with open(log_file, 'w') as log:
            try:
                subprocess.Popen(['python', '-m', module], stdout=log, stderr=subprocess.STDOUT)
            except Exception as e:
                logging.error("Error starting %s: %s", name, e)
    elif force_restart:
        logging.info("Restarting: %s", name)
        subprocess.call([f"{SCRIPT_DIR}/stop-mycroft.sh", name])
        launch_background(name)

def launch_all():
    logging.info("Starting all mycroft-core services")
    for name in SERVICES:
        if name != 'cli':
            launch_background(name)

def main(command, restart=False):
    global force_restart
    force_restart = restart
    
    if command == 'all':
        launch_all()
    elif command in SERVICES:
        launch_background(command)
    elif command == 'debug':
        launch_all()
        launch_process('cli', sys.argv[2:])
    elif command == 'cli':
        require_process('bus')
        require_process('skills')
        launch_process(command, sys.argv[2:])
    # other commands...

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        help()
    
    restart = False
    if sys.argv[2:] and sys.argv[2] == 'restart':
        restart = True
    
    command = sys.argv[1]
    main(command, restart)
