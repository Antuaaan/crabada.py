from typing import Any, List
from src.libs.CrabadaWeb2Client.types import CrabForLending, Game
from src.strategies.reinforce.ReinforceStrategy import ReinforceStrategy
from src.helpers.general import firstOrNone, fourthOrNone, secondOrNone, thirdOrNone
from src.helpers.price import weiToTus


class HighestMpReinforceStrategy(ReinforceStrategy):
    """
    Strategy that chooses the crab with a price lower than maxPrice
    which has the highest mine point value
    """

    def query(self, game: Game) -> dict[str, Any]:
        return {
            "limit": 200,  # TODO: make it an argument
            "orderBy": "price",
            "order": "asc",
        }

    def crab(self, game: Game, list: List[CrabForLending]) -> CrabForLending:
        affordableCrabs = [c for c in list if weiToTus(c["price"]) < self.maxPrice1]
        if len(affordableCrabs) == 0:
            return None
        sortedAffordableCrabs = sorted(
            affordableCrabs, key=lambda c: (-c["mine_point"], c["price"])
        )
        return (
            fourthOrNone(sortedAffordableCrabs)
            or thirdOrNone(sortedAffordableCrabs)
            or secondOrNone(sortedAffordableCrabs)
            or firstOrNone(sortedAffordableCrabs)
        )
