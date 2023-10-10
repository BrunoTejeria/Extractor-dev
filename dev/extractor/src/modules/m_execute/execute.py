from ..m_check.check import (
    Check
)

def init():
    file_result = 'extractor/etc/data/processed_data/result.txt'
    file_search = 'extractor/etc/data/raw_data/text.txt'
    check_obj = Check(
        file_search=file_search,
        file_result=file_result,
        url='https://github.com/'
        )
    processed_lines = check_obj.process_lines()
    print(processed_lines)
