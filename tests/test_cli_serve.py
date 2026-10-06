import os
import subprocess
import sys


def test_serve_subcommand_registered():
    env = dict(os.environ, FHIR_JWT_SECRET="x" * 40)
    p = subprocess.run([sys.executable, "-m", "fhir_server", "serve", "--help"],
                       capture_output=True, text=True, env=env, cwd=os.getcwd())
    # argparse rejects an unknown subcommand with exit code 2
    assert p.returncode == 0, p.stderr
    assert "serve" in p.stdout
