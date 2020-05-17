def parseFile(input_file, content_length):
    post_data = input_file.read(content_length)
    task_text = str(post_data.decode('utf-8'))
    return task_text