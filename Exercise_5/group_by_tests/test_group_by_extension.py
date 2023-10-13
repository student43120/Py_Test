import pytest
from file_parser import group_files_by_extension


test_cases_group_files = [
    ("file1.jpg, file2.gif, file3.mid, file4.jpg", "jpg, gif, mid"),
    ("example1.pdf, example2.pdf, example3.pdf", "pdf"),
    ("doc1.docx, doc2.docx, doc3.txt, doc4.txt", "docx, txt"),
    ("image1.png, image2.png, image3.jpg, image4.jpg", "png, jpg"),
]

@pytest.mark.parametrize("file_names, expected_groups", test_cases_group_files)
def test_group_files_by_extension(file_names, expected_groups):
    result = group_files_by_extension(file_names)
    assert result == expected_groups

if __name__ == '__main__':
    pytest.main()
