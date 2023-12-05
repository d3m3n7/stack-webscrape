class Entry:
    def __init__(
        self, *, title: str, order: int, n_comments: int | None, points: int | None
    ):
        self.title = title
        self.order = order
        self.n_comments = n_comments if n_comments is not None else 0
        self.points = points if points is not None else 0

    def to_dict(self) -> dict:
        return dict(
            title=self.title,
            order=self.order,
            n_comments=self.n_comments,
            points=self.points,
        )
