class Router:
    def __init__(self):
        self.routes = {}

    def register_controller(self, path, controller, model, view):
        self.routes[path] = controller(model, view)

    def resolve(self, path):
        callback = self.routes.get(path)
        if callback:
            return callback
        return self.default_controller

    def default_controller(self, *args, **kwargs):
        status = 'Controller not found'
        return status
