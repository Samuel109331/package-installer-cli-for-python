import argparse
import subprocess
import requests

def check_package_exists(package_name):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    return response.status_code == 200

def install_package(package_name):
    if check_package_exists(package_name):
        subprocess.run(["pip", "install", package_name])
        print(f"Package '{package_name}' has been installed successfully.")
    else:
        print(f"Package '{package_name}' not found on PyPI.")

def main():
    parser = argparse.ArgumentParser(description="Install Python package from PyPI")
    parser.add_argument("package", help="Name of the package to install")

    args = parser.parse_args()

    install_package(args.package)

if __name__ == "__main__":
    main()
