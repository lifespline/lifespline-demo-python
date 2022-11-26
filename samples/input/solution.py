due_date = input("due-date [None]: ") or 'None'
title = input("title: ")
if not title:
    raise ValueError('please insert a title')
