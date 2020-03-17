class Params(object):
    """ Params object """

    params = []

    def to_dict(self):

        resp = {}
        for param in self.params:
            resp[param] = getattr(self, param)

        return resp
