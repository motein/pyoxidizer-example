import os
import subprocess
import sys

# 项目路径设置（根据需要修改）
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(PROJECT_ROOT, 'app')
ENTRY_FILE = os.path.join(APP_DIR, 'main.py')
CORELIB_DIR = os.path.join(PROJECT_ROOT, 'corelib')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
ASSETS_DIR = os.path.join(PROJECT_ROOT, 'assets')
ICON_FILE = os.path.join(ASSETS_DIR, 'main.ico')

# 编译命令（你可以根据需要调整参数）
nuitka_command = [
    sys.executable, "-m", "nuitka",
    ENTRY_FILE,
    "--standalone",
    "--onefile",
    f"--output-filename=MyApp.exe",
    "--enable-plugin=pyqt5",
    f"--include-plugin-directory={CORELIB_DIR}",
    f"--include-data-dir={DATA_DIR}=data",
    f"--include-data-dir={ASSETS_DIR}=assets",
    f"--windows-icon-from-ico={ICON_FILE}",
    "--nofollow-import-to=tests",
    "--show-progress",
    "--windows-console-mode=disable"
]

# 执行打包
def build():
    print("Use Nuitka to package PyQt5 app...")
    print("Command\n", ' '.join(nuitka_command))
    result = subprocess.run(nuitka_command)
    if result.returncode == 0:
        print("Successfully build：MyApp.exe")
    else:
        print("Failed to build the application.")

if __name__ == "__main__":
    build()
