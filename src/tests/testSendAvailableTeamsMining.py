from src.helpers.Games import sendAvailableTeamsMining
from src.common.config import users

# VARS

# TEST FUNCTIONS
def testSendAvailableTeamsMining() -> None:
    nSent = sendAvailableTeamsMining(users[0]['address'])
    print(f'SENT {nSent} TEAMS')

# EXECUTE
testSendAvailableTeamsMining()