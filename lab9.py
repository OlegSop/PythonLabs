import re


def task_1():
    """
   Exercise 1: Matching Characters
   """
    print("Task 1:")
    columns = ['abcdefg', 'abcde', 'abc']
    for col in columns:
        if re.search("abc", col):
            print(f"Matched! - {col}")


def task_1_2():
    """
    Exercise 1½: Matching Digits
    """
    print("Task 1½:")
    columns = ['abc123xyz', 'define "123"', 'var g = 123;']
    for col in columns:
        if re.search("123", col):
            print(f"Matched! - {col}")


def task_2():
    """
    Exercise 2: Matching With Wildcards
    """
    print("Task 2:")
    columns = ['cat.', '896.', '?=+.', 'abc1']
    for col in columns:
        if re.search("\.", col):
            print(f"Matched! - {col}")


def task_3():
    """
    Exercise 3: Matching Characters
    """
    print("Task 3:")
    columns = ['can', 'man', 'fan', 'dan', 'ran', 'pan']
    for col in columns:
        if re.search("[cmf]an", col):
            print(f"Matched! - {col}")


def task_4():
    """
    Exercise 4: Excluding Characters
    """
    print("Task 4:")
    columns = ['hog', 'dog', 'bog']
    for col in columns:
        if re.search("[^b]og", col):
            print(f"Matched! - {col}")


def task_5():
    """
    Exercise 5: Matching Character Ranges
    """
    print("Task 5:")
    columns = ['Ana', 'Bob', 'Cpc', 'aax', 'bby', 'ccz']
    for col in columns:
        if re.search("[A-C][n-p][a-c]", col):
            print(f"Matched! - {col}")


def task_6():
    """
    Exercise 6: Matching Repeated Characters
    """
    print("Task 6:")
    columns = ['wazzzzzup', 'wazzzup', 'wazup']
    for col in columns:
        if re.search("z{3,5}", col):
            print(f"Matched! - {col}")


def task_7():
    """
    Exercise 7: Matching Repeated Characters
    """
    print("Task 7:")
    columns = ['aaaabcc', 'aabbbbc', 'aacc', 'a']
    for col in columns:
        if re.search("aa+[bc]+", col):
            print(f"Matched! - {col}")


def task_8():
    """
    Exercise 8: Matching Optional Characters
    """
    print("Task 8:")
    columns = ['1 file found?', '2 files found?', '24 files found?', '	No files found.']
    for col in columns:
        if re.search("\d+ files? found\?", col):
            print(f"Matched! - {col}")


def task_9():
    """
    Exercise 9: Matching Whitespaces
    """
    print("Task 9:")
    columns = ['1. abc', '2.  abc', '3.     abc', '4.abc']
    for col in columns:
        if re.search("\d.\s+abc", col):
            print(f"Matched! - {col}")


def task_10():
    """
    Exercise 10: Matching Lines
    """
    print("Task 10:")
    columns = ['Mission: successful', '	Last Mission: unsuccessful', 'Next Mission: successful upon capture of target']
    for col in columns:
        if re.search("^Mission:", col):
            print(f"Matched! - {col}")


def task_11():
    """
    Exercise 11: Matching Groups
    """
    print("Task 11:")
    columns = ['file_record_transcript.pdf', 'file_07241999.pdf', 'testfile_fake.pdf.tmp']
    for col in columns:
        if re.search("^(file.+)\.pdf$", col):
            print(f"Matched! - {col}")


def task_12():
    """
    Exercise 12: Matching Nested Groups
    """
    print("Task 12:")
    columns = ['Jan 1987', 'May 1969', 'Aug 2011']
    for col in columns:
        if re.search("^(... (\d+))$", col):
            print(f"Matched! - {col}")


def task_13():
    """
    Exercise 13: Matching Nested Groups
    """
    print("Task 13:")
    columns = ['1280x720', '1920x1600', '1024x768']
    for col in columns:
        if re.search("(\d+)x(\d+)", col):
            print(f"Matched! - {col}")

def task_14():
    """
    Exercise 14: Matching Conditional Text
    """
    print("Task 14:")
    columns = ['I love cats', 'I love dogs', 'I love logs', 'I love cogs']
    for col in columns:
        if re.search("I love (cats|dogs)", col):
            print(f"Matched! - {col}")


def task_15():
    """
    Exercise 15: Matching Other Special Characters
    """
    print("Task 15:")
    columns = ['The quick brown fox jumps over the lazy dog.',
               'There were 614 instances of students getting 90.0% or above.',
               'The FCC had to censor the network for saying &$#*@!.']
    for col in columns:
        if re.search("(\D+)", col):
            print(f"Matched! - {col}")


if __name__ == '__main__':
    task_1()
    task_1_2()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()
    task_11()
    task_12()
    task_13()
    task_14()
    task_15()
