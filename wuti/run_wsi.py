import subprocess
import sys

from wuti.catch_input import catch_wsi


def run_wsi():
    """Menjalankan perintah, stream output ke layar, dan kembalikan error jika ada."""
    inputWSIUser = catch_wsi()

    if not inputWSIUser:
        return None

    command_str = " ".join(inputWSIUser)

    try:
        proc = subprocess.Popen(
            command_str,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        log_buffer = []

        while True:
            line = proc.stdout.readline()

            if line == "" and proc.poll() is not None:
                break

            if line:
                sys.stdout.write(line)
                sys.stdout.flush()

                log_buffer.append(line)

        exit_code = proc.poll()

        if exit_code != 0:
            return "".join(log_buffer)

        return None

    except KeyboardInterrupt:
        print("\n[INFO] Program stoped by user.")
        return None
    except Exception as e:
        print(f"[ERROR]Internal Wuti Error: {e}")
        return str(e)


if __name__ == "__main__":
    run_wsi()
