import re

from wuti.run_wsi import run_wsi


def parse_log():
    """fungsi ini untuk memparse log menggunakan regex"""

    logData = str(run_wsi())
    regexPattern = r"(?s)(?P<traceback>Traceback \(most recent call last\):.*?)?(?P<error_type>[A-Z][a-zA-Z0-9_]*(?:Error|Exception|Warning|Exit|Interrupt|Stop|NotFound|Failure))\s*:\s*(?P<error_msg>.*)$"

    try:
        # print("[INFO] parsering at `parser.py'")
        resultParserLog = re.findall(
            regexPattern, logData, re.IGNORECASE | re.MULTILINE
        )

        if not resultParserLog:
            return None

        print(resultParserLog)
        return str(resultParserLog)
    except Exception as e:
        print(e)
        return None
    except KeyboardInterrupt:
        return None


if __name__ == "__main__":
    parse_log()
