def get_url(url):
    uri = {
        'show': url+':show',
        'create': url+':create',
        'edit': url+':edit',
        'delete': url+':delete',
        'update': url+':update',
        'set': url+':set',
        'change': url+':change',
        'showprofile': url+':showprofile',
        'createprofile': url+':createprofile',
        'editprofile': url+':editprofile',
        'deleteprofile': url+':deleteprofile',
        'home': 'users:home',
        'print': url+':print',
        'sent': url+':sent',
        'search': url+':search',
        'result': url+':result',
    }
    return uri

def get_body(singular, plural):
    title = {
        'show': 'Administrar '+plural,
        'create': 'Agregar '+singular,
        'edit': 'Editar '+singular,
        'delete': 'Borrar '+singular,
        'change': 'Cambiar '+singular,
        'subtitle': 'Panel de control',
        'login': 'Ingresar al sistema',
        'home': 'Dashboard',
        'report': 'Reports',
        'page': 'Principal',
        'search': 'Buscar '+singular,
    }
    return title

def get_button():
    button = ['Enviar', 'Guardar', 'Buscar', 'Borrar']
    return button