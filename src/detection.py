# detection.py

def detect_available_managers():
    """
    Detects all supported package managers and returns a list of their 
    interface module names, including AppImage as a constant option.
    """
    found_managers = []
    
    # Check for system packages

    if os.path.exists('/etc/debian_version'):
        found_managers.append("launch-dpkg-apt")

    if os.path.exists('')
    
    if os.path.exists('/etc/arch-release'):
        found_managers.append("launch-pacman")

    if os.path.exists('/etc/gentoo-release'):
        found_managers.append("launch-portage")
    
    found_managers.append("launch-appimage") 
    
    return found_managers