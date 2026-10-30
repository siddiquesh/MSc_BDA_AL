import os
import sys
import subprocess

root = os.path.dirname(os.path.abspath(__file__))
python_exe = sys.executable

print(f"Testing execution with: {python_exe}")
results = {}

for i in range(1, 10):
    fn = os.path.join(root, f"practical_{i}.py")
    print(f"\n==================================================")
    print(f"RUNNING PRACTICAL {i}: {fn}")
    print(f"==================================================")
    
    # Run script with non-interactive backend so plt.show() does not block
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    
    # We prepend matplotlib.use('Agg') and plt.show = lambda: None
    test_wrapper = f"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.show = lambda *args, **kwargs: None

with open(r'{fn}', 'r', encoding='utf-8') as f:
    code = f.read()
exec(code)
"""
    
    proc = subprocess.run(
        [python_exe, "-c", test_wrapper],
        cwd=root,
        capture_output=True,
        text=True,
        env=env,
        timeout=120
    )
    
    status = "SUCCESS" if proc.returncode == 0 else "FAILED"
    results[i] = (status, proc.returncode, proc.stdout, proc.stderr)
    
    print(f"Status: {status} (Code {proc.returncode})")
    if proc.stdout:
        lines = proc.stdout.strip().splitlines()
        print(f"STDOUT preview ({len(lines)} lines):")
        for line in lines[:8]:
            print(f"  [OUT] {line}")
        if len(lines) > 8:
            print(f"  ... ({len(lines)-8} more lines)")
            for line in lines[-4:]:
                print(f"  [OUT] {line}")
    if proc.stderr:
        print("STDERR:")
        for line in proc.stderr.strip().splitlines()[:5]:
            print(f"  [ERR] {line}")

print("\n" + "="*60)
print("FINAL TEST EXECUTION SUMMARY:")
print("="*60)
all_pass = True
for i in range(1, 10):
    status, code, _, _ = results[i]
    print(f"Practical {i}: {status} (Exit Code: {code})")
    if status != "SUCCESS":
        all_pass = False

if all_pass:
    print("\n>>> ALL 9 PRACTICALS EXECUTED PERFECTLY WITH ZERO ERRORS! <<<")
else:
    print("\n>>> SOME PRACTICALS FAILED <<<")
    sys.exit(1)
