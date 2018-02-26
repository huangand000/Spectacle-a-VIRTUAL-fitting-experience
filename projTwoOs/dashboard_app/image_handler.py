
def save_image(f):
    with open('file1.png', 'wb+') as destination:
        print 'a2'
        for chunk in f.chunks():
            destination.write(chunk)