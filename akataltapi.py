from datetime import datetime, date
from typing import *
import requests
import time

class UserLeaderboardTypeEnum(str, Enum):
    pp = "pp"
    score = "score"

class UserExtraLeaderboardTypeEnum(str, Enum):
    pp = "pp"
    score = "score"
    total_score = "total_score"
    clears = "clears"
    first_places = "1s"
    xh_count = "xh_count"
    x_count = "x_count"
    sh_count = "sh_count"
    s_count = "s_count"
    a_count = "a_count"
    b_count = "b_count"
    c_count = "c_count"
    d_count = "d_count"

class ClanLeaderboardTypeEnum(str, Enum):
    pp = "pp"
    first_places = "1s"
    score = "score"
    total_score = "total_score"
    play_count = "play_count"

class UserRank:
    
    def __init__(self, global_rank: int, country_rank: int) -> None:
        self.global_rank = global_rank
        self.country_rank = country_rank

class Score:
    
    def __init__(self, api, beatmap_id: int, server: str, user_id: int, mode: int, relax: int, score_id: int, accuracy: float, mods: int, pp: float, score: int, combo: int, rank: str, count_300: int, count_100: int, count_50: int, count_miss: int, completed: int, date: int) -> None:
        self.api = api
        self.beatmap_id = beatmap_id
        self.server = server
        self.user_id = user_id
        self.mode = mode
        self.relax = relax
        self.score_id = score_id
        self.accuracy = accuracy
        self.mods = mods
        self.pp = pp
        self.score = score
        self.combo = combo
        self.rank = rank
        self.count_300 = count_300
        self.count_100 = count_100
        self.count_50 = count_50
        self.count_miss = count_miss
        self.completed = completed
        self.date = date

class User:
    
    def __init__(self, api, user_id, server, username, registered_on, latest_activity, country, clan, followers) -> None:
        self.api = api
        self.user_id = user_id
        self.server = server
        self.username = username
        self.registered_on = registered_on
        self.latest_activity = latest_activity
        self.country = country
        self.clan = clan
        self.followers = followers    

class Clan:
    
    def __init__(self, api, server, clan_id, name, tag, description, icon, owner, status) -> None:
        self.api = api
        self.server = server
        self.clan_id = clan_id
        self.name = name
        self.tag = tag
        self.description = description
        self.icon = icon
        self.owner = owner
        self.status = status
        
    def get_members(self) -> List[User]:
        return self.api.get_clan_members(self.server, self.clan_id)

class ClanStatistics:
    
    def __init__(self, api, server: str, clan_id: int, mode: int, relax: int, date: date, global_rank: int, global_rank_1s: int, ranked_score: int, total_score:int, play_count: int, accuracy: float, first_places: int, pp: int) -> None:
        self.api = api
        self.server = server
        self.clan_id = clan_id
        self.mode = mode
        self.relax = relax
        self.date = date
        self.global_rank = global_rank
        self.global_rank_1s = global_rank_1s
        self.ranked_score = ranked_score
        self.total_score = total_score
        self.play_count = play_count
        self.accuracy = accuracy
        self.first_places = first_places
        self.pp = pp

    def get_clan(self) -> Clan:
        return self.api.get_clan_info()

class UserLeaderboardStats:
    
    def __init__(self, api, server: str, user_id: int, mode: int, relax: int, global_rank: int, country_rank: int, ranked_score: int, total_score: int, play_count: int, replays_watched: int, total_hits: int, level: int, accuracy: float, pp: float) -> None:
        self.api = api
        self.server = server
        self.user_id = user_id
        self.mode = mode 
        self.relax = relax
        self.global_rank = global_rank
        self.country_rank = country_rank
        self.ranked_score = ranked_score
        self.total_score = total_score
        self.play_count = play_count
        self.replays_watched = replays_watched
        self.total_hits = total_hits
        self.level = level
        self.accuracy = accuracy
        self.pp = pp

    def get_user(self) -> User:
        return self.api.get_user_info(server=self.server, user_id=self.user_id)

class UserStatistics:
    
    def __init__(self, api, user_id: int, server: str, mode: int, relax: int, date: str, ranked_score: int, total_score: int, play_count: int, play_time: int, replays_watched: int, total_hits: int, level: float, accuracy: float, pp: int, global_rank: int, country_rank: int, global_score_rank: int, country_score_rank: int, max_combo: int, first_places: int, clears: int, xh_count: int, x_count: int, sh_count: int, s_count: int, a_count: int, b_count: int, c_count: int, d_count: int) -> None:
        self.api = api
        self.user_id = user_id
        self.server = server
        self.mode = mode
        self.relax = relax
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.ranked_score = ranked_score
        self.total_score = total_score
        self.play_count = play_count
        self.play_time = play_time
        self.replays_watched = replays_watched
        self.total_hits = total_hits
        self.level = level
        self.accuracy = accuracy
        self.pp = pp
        self.global_rank = global_rank
        self.country_rank = country_rank
        self.global_score_rank = global_score_rank
        self.country_score_rank = country_score_rank
        self.max_combo = max_combo
        self.first_places = first_places
        self.clears = clears
        self.xh_count = xh_count
        self.x_count = x_count
        self.sh_count = sh_count
        self.s_count = s_count
        self.a_count = a_count
        self.b_count = b_count
        self.c_count = c_count
        self.d_count = d_count

    def get_user(self) -> User:
        return self.api.get_user_info(server=self.server, user_id=self.user_id)


class AkatAltAPI:
    
    def __init__(self, url="http://akatalt.lekuru.xyz") -> None:
        self._last = 0
        self.url = url
        self.delay = 60/60
        
    def _get(self, url):
        diff = time.time() - self._last
        if diff < self.delay:
            time.sleep(self.delay - diff)
        self._last = time.time()
        return requests.get(url)
    
    def get_user_leaderboard(self, server="akatsuki", mode=0, relax=0, page=1, length=100, type: UserLeaderboardTypeEnum = UserLeaderboardTypeEnum.pp) -> List[UserLeaderboardStats]:
        req = self._get(f"{self.url}/leaderboard/user?server={server}&mode={mode}&relax={relax}&page={page}&length={length}&type={type}")
        if not req.ok:
            return
        stats = list()
        for user in req.json():
            stats.append(UserLeaderboardStats(self, **user))
        return stats

    def get_user_extra_leaderboard(self, server="akatsuki", mode=0, relax=0, page=1, length=100, date: date=date.today(), type: UserExtraLeaderboardTypeEnum = UserExtraLeaderboardTypeEnum.pp) -> List[UserStatistics]:
        req = self._get(f"{self.url}/leaderboard/user_extra?server={server}&date={date.strftime('%Y-%m-%d')}&mode={mode}&relax={relax}&page={page}&length={length}&type={type}")
        if not req.ok:
            return
        stats = list()
        for user in req.json():
            stats.append(UserStatistics(self, **user))
        return stats

    def get_clan_leaderboard(self, server="akatsuki", mode=0, relax=0, page=1, length=100, type: ClanLeaderboardTypeEnum = ClanLeaderboardTypeEnum.pp):
        req = self._get(f"{self.url}/leaderboard/clan?server={server}&mode={mode}&relax={relax}&page={page}&length={length}&type={type}")
        if not req.ok or not req.content:
            return
        stats = list()
        for user in req.json():
            stats.append(ClanStatistics(self, **user))
        return stats

    def get_user_info(self, user_id, server="akatsuki") -> User:
        req = self._get(f"{self.url}/user/info?user_id={user_id}&server={server}")
        if not req.ok or req.content:
            return
        return User(self, **req.json())

    def get_user_statistics(self, user_id, server="akatsuki", mode=0, relax=0, date=date.today()):
        req = self._get(f"{self.url}/user/stats?server={server}&user_id={user_id}&mode={mode}&relax={relax}&date={date.strftime('%Y-%m-%d')}")
        if not req.ok or req.content:
            return
        return UserStatistics(self, **req.json())

    def get_user_1s(self, user_id, server="akatsuki", mode=0, relax=0, date=date.today(), page=1, length=100):
        req = self._get(f"{self.url}/user/first_places?server={server}&user_id={user_id}&mode={mode}&relax={relax}&date={date.strftime('%Y-%m-%d')}&page={page}&length={length}")
        if not req.ok or not req.content:
            return
        data = req.json()
        scores = list()
        for score in data['scores']:
            scores.append(Score(self, **score))
        return data['total'], scores

    def get_user_clears(self, user_id, server="akatsuki", mode=0, relax=0, date=date.today(), page=1, length=100) -> Tuple[int, List[Score]]:
        req = self._get(f"{self.url}/user/clears?server={server}&user_id={user_id}&mode={mode}&relax={relax}&date={date.strftime('%Y-%m-%d')}&page={page}&length={length}")
        if not req.ok or not req.content:
            return
        data = req.json()
        scores = list()
        for score in data['scores']:
            scores.append(Score(self, **score))
        return data['total'], scores

    def get_user_rank(self, user_id, server="akatsuki", mode=0, relax=0, type: UserLeaderboardTypeEnum=UserLeaderboardTypeEnum.pp):
        req = self._get(f"{self.url}/user/rank?server={server}&user_id={user_id}&mode={mode}&relax={relax}&type={type}")
        if not req.ok or not req.content:
            return
        return UserRank(**req.json())

    def get_clan_info(self, clan_id, server="akatsuki") -> Clan | None:
        req = self._get(f"{self.url}/clan/info?server={server}&clan_id={clan_id}")
        if not req.ok or not req.content:
            return
        return Clan(self, **req.json())

    def get_clan_members(self, clan_id, server="akatsuki") -> List[User]:
        req = self._get(f"{self.url}/clan/members?server={server}&clan_id={clan_id}")
        if not req.ok or not req.content:
            return
        members = list()
        for user in req.json():
            members.append(User(self, **user))
        return members
    
    def get_clan_stats(self, clan_id, server="akatsuki", mode=0, relax=0, date=date.today()) -> ClanStatistics:
        req = self._get(f"{self.url}/clan/stats?server={server}&clan_id={clan_id}&mode={mode}&relax={relax}&date={date.strftime('%Y-%m-%d')}")
        if not req.ok or not req.content:
            return
        return ClanStatistics(self, **req.json())