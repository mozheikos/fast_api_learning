from databases import Database


class BaseRep:
    def __init__(self, database: Database):
        self.session = database
