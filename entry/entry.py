class Entry:
    def __init__(
        self, *, title: str, order: int, n_comments: int | None, points: int | None
    ):
        self.title = title
        self.order = order
        self.n_comments = n_comments
        self.points = points
