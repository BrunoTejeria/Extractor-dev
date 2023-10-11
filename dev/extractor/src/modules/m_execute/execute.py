from ..m_check.check import (
    Check
)

def init():
    check_obj = Check()
    processed_lines = check_obj.process_lines()
    print(processed_lines)
    print(check_obj.file_result)
