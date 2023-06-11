import subprocess
import sys

def execute_script(script_name, *args):
    try:
        command = ['python', script_name] + list(args)
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")
    except FileNotFoundError:
        print(f"Script '{script_name}' not found.")

if len(sys.argv) >= 3:
    script_name = sys.argv[1]
    script_args = sys.argv[2:]
    execute_script(script_name, *script_args)
else:
    print("Usage: python main.py <script_name> <script_arguments>")
