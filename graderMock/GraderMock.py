# -*- coding: utf-8 -*-

def validate_task(user_task, user_credential):
    mark, message = grade_task(user_task)
    pipeline_response = {'user_credential': user_credential, 'mark': mark, 'additional_message': message}
    return pipeline_response


# Метод для запуска оценки
def grade_task(user_task):
    try:
        mark = int(user_task)
        if mark < 0:
            return 0, 'To small number'
        if mark > 10:
            return 0, "To large mark. Don't be a cheater"
        return mark, "All ok, your mark is " + str(mark)
    except ValueError:
        return 0, 'Incorrect Task format'
