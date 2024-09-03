from comment import Comment


class Item:
    def __init__(self, id: int, name: str, owner_id: int, desc: str = None, photo: str = None, available: bool = True):
        self._id = id
        self._name = name
        self._desc = desc
        self._photo = photo
        self._available = available
        self._owner_id = owner_id
        self._comments: dict[int, Comment] = {}

    @property
    def id(self) -> int:
        """get item id"""
        return self._id

    @property
    def owner_id(self) -> int:
        """get owner id"""
        return self._owner_id

    @property
    def name(self) -> str:
        """get item name"""
        return self._name

    @property
    def general_score(self)-> str:
        """get para o preco do item"""
        total = sum([c.score for c in self._comments.values()])
        ammount = len(self._comments)
        score = 0
        if (ammount != 0):
            score = total/ammount
        half_star = (2*score)%2
        rest = 5 - (int(score+half_star))
        return "★"*int(score) + "⋆"*int(half_star)+"☆"*int(rest)

    @property
    def desc(self) -> str:
        """get item description"""
        return self._desc

    @property
    def photo(self) -> str:
        """get item photo"""
        return self._photo

    @property
    def comments(self) -> dict[int, Comment]:
        """get item comments"""
        return self._comments

    @property
    def available(self) -> bool:
        """get item availability"""
        return self._available

    @available.setter
    def available(self, value: bool):
        """set item availability"""
        self._available = value

    @classmethod
    def get_avg_score(self) -> float:
        comment_count: float = float(len(self._comments))
        total_score: float = 0.0
        for c in self._comments.values():
            total_score += c.score
        return total_score/comment_count

    @classmethod
    def add_comment(self, p, c: Comment) -> None:
        self._comments[p.name] = c

    def to_dict(self) -> dict[str, any]:
        """parse object to dict"""
        return {
            "id": self._id,
            "name": self._name,
            "desc": self._desc,
            "photo": self._photo,
            "available": self._available,
            "owner_id": self._owner_id,
            "comments": [c.to_dict() for c in self._comments.values()],
        }
