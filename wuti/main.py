from wuti.ai import call_ai
from wuti.run_wsi import run_wsi


def main():
    try:
        error = run_wsi()
        if error:
            result = call_ai(error)
            print(result)

    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
