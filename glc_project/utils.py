import uuid

import uuid

def files_directory_path(instance, filename):
    new_filename = instance.__str__()
    if (instance.__class__.__name__.lower()) == 'event':
        new_filename = instance.__str__() + " " + instance.start.date().strftime('%Y-%m-%d')
    
    elif (instance.__class__.__name__.lower()) != 'event' and (instance.__class__.__name__.lower()) != 'profile' and (instance.__class__.__name__.lower()) != 'tv':
        return '/'.join([str(instance.__class__.__name__.lower()), 
                    str(new_filename),
                    str(filename)])
    return '/'.join([str(instance.__class__.__name__.lower() + "_photos"), 
                    str(new_filename),
                    str(uuid.uuid4().hex + ".jpg")])