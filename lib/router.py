class Router:
    def __init__(self):
        self.routes = {}

    def register(self, path, controller, model, view):
        model = model(); view = view()
        self.routes[path] = controller(model, view)

    def resolve(self, path):
        if self.routes.get(path):
            controller = self.routes[path]
            return controller
        else:
            raise ValueError("Cannot find path", path)
