import platform

system = platform.system()

if system == 'Linux':
    import install_linux as install_script
elif system == 'Windows':
    import install_windows as install_script
elif system == 'Darwin':
    import install_mac as install_script
else:
    print("Système d'exploitation non pris en charge.")
    exit(1)

if __name__ == "__main__":
    install_script.install()
