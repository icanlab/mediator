#!/usr/bin/env python3

import connexion

from mediator_server import encoder
from mediator_server import scan


def main():
    scan.main()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Mediator framework'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
