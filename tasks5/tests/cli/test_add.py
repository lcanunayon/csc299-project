import subprocess
import sys
import json
from pathlib import Path


def test_cli_add(tmp_path):
    # Use a temporary data path override by setting env var or using default
    # We'll call the module directly
    cmd = [sys.executable, "-m", "taskmgr", "add", "--title", "CLI Test"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0
    assert "CLI Test" in proc.stdout
