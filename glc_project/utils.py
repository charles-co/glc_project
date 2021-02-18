import uuid

def files_directory_path(instance, filename):
    new_filename = instance.__str__()
    if (instance.__class__.__name__.lower()) == 'event':
        new_filename = instance.__str__() + " " + instance.start.date().strftime('%Y-%m-%d')
    
    if (instance.__class__.__name__.lower()) == 'audio':
        return '/'.join([str(instance.__class__.__name__.lower()), 
                    str(new_filename),
                    str(filename)])

    if (instance.__class__.__name__.lower()) == 'video':
        return '/'.join([str(instance.__class__.__name__.lower()), 
                    str(new_filename),
                    str(filename)])
    if (instance.__class__.__name__.lower()) == 'podcast':
        return '/'.join([str(instance.__class__.__name__.lower()), 
                    str(new_filename),
                    str(filename)])

    return '/'.join([str(instance.__class__.__name__.lower() + "_photos"), 
                    str(new_filename),
                    str(uuid.uuid4().hex + ".jpg")])