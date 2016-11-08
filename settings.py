DOMAIN = {
    'user': {
        'schema': {
            'name': {
                'type': 'string'
            },
            'email': {
                'type': 'string',
                 'unique': True
            },
            'pass': {
                'type': 'string'
            },
            'phone': {
                'type': 'string'
            },
            'image': {
                'type': 'string'
            },
            'role': {
                'type': 'string'
            }
        }
    }
}
RESOURCE_METHODS = ['GET', 'POST']