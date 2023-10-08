

from ..m_logic.check import (
    Check
)

def init():
    file_result = 'etc/data/processed_data/result.txt'
    file_search = 'etc/data/raw_data/text.txt'
    check_obj = Check(
        file_search=file_search,
        file_result=file_result,
        url='1'
        )
    processed_lines = check_obj.process_lines()
    print(processed_lines)
