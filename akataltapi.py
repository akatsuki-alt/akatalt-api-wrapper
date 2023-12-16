from datetime import datetime, date, timedelta
from enum import Enum
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

class FirstPlacesEnum(str, Enum):
    all = "all"
    new = "new"
    lost = "lost"

class ScoreSortEnum(str, Enum):
    beatmap_id = "beatmap_id"
    score_id = "score_id"
    accuracy = "accuracy"
    mods = "mods"
    pp = "pp"
    score = "score"
    combo = "combo"
    rank = "rank"
    date = "date"

class UserSortEnum(str, Enum):
    user_id = "user_id"
    username = "username"
    registered_on = "registered_on"
    latest_activity = "latest_activity"
    country = "country"
    clan_id = "clan_id"
    followers = "followers"

class BeatmapSortEnum(str, Enum):
    artist = "artist"
    title = "title"
    version = "version"
    mapper = "mapper"
    stars_nm = "stars_nm"
    length = "length"
    ranked_status = "ranked_status"
    approved_date = "approved_date"
    last_checked = "last_checked"

class RankedStatusEnum(int, Enum):
    graveyard = -2
    wip = -1
    pending = 0
    ranked = 1
    approved = 2
    qualified = 3
    loved = 4

class Beatmap:
    
    def __init__(self, beatmap_id: int, beatmap_set_id: int, beatmap_md5: str, artist: str, title: str, version: str, mapper: str, ranked_status: Dict[str, int], nominator: Dict[str, str], last_checked: str, ar: float, od: float, cs: float, length: int, bpm: float, max_combo: int, circles: int, sliders: int, spinners: int, mode: int, tags: str, packs: str, source: str, language: str, genre: str, spotlight: bool, stars_nm: float, stars_ez: float, stars_hr: float, stars_dt: float, stars_dtez: float, stars_dthr: float, approved_date: int) -> None:
        self.beatmap_id = beatmap_id
        self.beatmap_set_id = beatmap_set_id
        self.beatmap_md5 = beatmap_md5
        self.artist = artist
        self.title = title
        self.version = version
        self.mapper = mapper
        self.ranked_status = ranked_status
        self.nominator = nominator
        self.last_checked = last_checked
        self.ar = ar
        self.od = od
        self.cs = cs
        self.length = length
        self.bpm = bpm
        self.max_combo = max_combo
        self.circles = circles
        self.sliders = sliders
        self.spinners = spinners
        self.mode = mode
        self.tags = tags
        self.packs = packs
        self.source = source
        self.genre = genre
        self.language = language
        self.spotlight = spotlight
        self.stars_nm = stars_nm
        self.stars_ez = stars_ez
        self.stars_hr = stars_hr
        self.stars_dt = stars_dt
        self.stars_dtez = stars_dtez
        self.stars_dthr = stars_dthr
        self.approved_date = approved_date

class ServerBeatmaps:
    
    def __init__(self, server_name: str, beatmap_sets: List[str]) -> None:
        self.server_name = server_name
        self.beatmap_sets = beatmap_sets

class UserRank:
    
    def __init__(self, global_rank: int, country_rank: int) -> None:
        self.global_rank = global_rank
        self.country_rank = country_rank

class Score:
    
    def __init__(self, api, beatmap: Beatmap, beatmap_id: int, server: str, user_id: int, mode: int, relax: int, score_id: int, accuracy: float, mods: int, pp: float, score: int, combo: int, rank: str, count_300: int, count_100: int, count_50: int, count_miss: int, completed: int, date: int) -> None:
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
        self.beatmap = beatmap

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
        return self.api.get_clan_info(self.clan_id, self.server)

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

class UserFilter:
    
    def __init__(self, user_id: int, mode: int, relax: int, server: str) -> None:
        self.user_id = user_id
        self.mode = mode
        self.relax = relax
        self.server = server

    def format(self):
        return f"{self.mode},{self.relax},{self.user_id},{self.server}"

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
    
    def get_user_leaderboard(self, server="akatsuki", mode=0, relax=0, page=1, length=100, type: UserLeaderboardTypeEnum = UserLeaderboardTypeEnum.pp) -> Tuple[int, List[UserLeaderboardStats]] | None:
        req = self._get(f"{self.url}/leaderboard/user?server={server}&mode={mode}&relax={relax}&page={page}&length={length}&type={type}")
        if not req.ok:
            return
        try:
            data = req.json()
            stats = list()
            for user in data['users']:
                stats.append(UserLeaderboardStats(self, **user))
            return data['total'], stats
        except:
            return

    def get_user_extra_leaderboard(self, server="akatsuki", mode=0, relax=0, page=1, length=100, date: date=date.today(), type: UserExtraLeaderboardTypeEnum = UserExtraLeaderboardTypeEnum.pp) -> Tuple[int, List[UserStatistics]] | None:
        req = self._get(f"{self.url}/leaderboard/user_extra?server={server}&date={date.strftime('%Y-%m-%d')}&mode={mode}&relax={relax}&page={page}&length={length}&type={type}")
        if not req.ok:
            return
        stats = list()
        try:
            data = req.json()
            for user in data['users']:
                stats.append(UserStatistics(self, **user))
            return data['total'], stats
        except:
            return

    def get_clan_leaderboard(self, server="akatsuki", mode=0, relax=0, page=1, length=100, type: ClanLeaderboardTypeEnum = ClanLeaderboardTypeEnum.pp) -> Tuple[int, List[ClanStatistics]] | None:
        req = self._get(f"{self.url}/leaderboard/clan?server={server}&mode={mode}&relax={relax}&page={page}&length={length}&type={type}")
        if not req.ok or not req.content:
            return
        stats = list()
        try:
            data = req.json()
            for user in data['clans']:
                stats.append(ClanStatistics(self, **user))
            return data['total'], stats
        except:
            return

    def get_user_info(self, user_id, server="akatsuki") -> User | None:
        req = self._get(f"{self.url}/user/info?user_id={user_id}&server={server}")
        if not req.ok or not req.content:
            return
        try:
            return User(self, **req.json())
        except:
            return

    def get_user_list(self, server="akatsuki", page=1, length=100, desc=True, sort: UserSortEnum = "user_id", filter="") -> Tuple[int, List[User]] | None:
        req = self._get(f"{self.url}/user/list?server={server}&page={page}&length={length}&desc={desc}&sort={sort}&filter={filter}")
        if not req.ok or not req.content:
            return
        data = req.json()
        return data['total'], [User(self, **user) for user in data['users']]

    def get_user_statistics(self, user_id, server="akatsuki", mode=0, relax=0, date=date.today()) -> UserStatistics | None:
        req = self._get(f"{self.url}/user/stats?server={server}&user_id={user_id}&mode={mode}&relax={relax}&date={date.strftime('%Y-%m-%d')}")
        if not req.ok or not req.content:
            return
        try:
            return UserStatistics(self, **req.json())
        except:
            return

    def get_user_1s(self, user_id, server="akatsuki", mode=0, relax=0, date=(date.today()-timedelta(days=1)), score_filter='', beatmap_filter='', sort: ScoreSortEnum = 'date', desc: bool = True, type: FirstPlacesEnum = "all", page=1, length=100, download_link=False) -> Tuple[int, List[Score]] | Dict[str, str] | None:
        url = f"{self.url}/user/first_places?server={server}&user_id={user_id}&mode={mode}&relax={relax}&type={type}&sort={sort}&desc={desc}&date={date.strftime('%Y-%m-%d')}&beatmap_filter={beatmap_filter}&score_filter={score_filter}&page={page}&length={length}"
        if download_link:
            return {'csv': url+"&download_as=csv", 'collection': url+"&download_as=collection"}
        req = self._get(url)
        if not req.ok or not req.content:
            return
        data = req.json()
        scores = list()
        try:
            for score in data['scores']:
                beatmap = Beatmap(**score['beatmap'])
                del score['beatmap']
                scores.append(Score(self, **score, beatmap=beatmap))
            return data['total'], scores
        except Exception as e:
            print(e)
            
    def get_all_1s(self, server="akatsuki", mode=0, relax=0, date=(date.today()-timedelta(days=1)), score_filter='', beatmap_filter='', sort: ScoreSortEnum = 'date', desc: bool = True, page=1, length=100, download_link=False) -> Tuple[int, List[Score]] | Dict[str, str] | None:
        url = f"{self.url}/user/first_places/all?server={server}&mode={mode}&relax={relax}&sort={sort}&desc={desc}&date={date.strftime('%Y-%m-%d')}&beatmap_filter={beatmap_filter}&score_filter={score_filter}&page={page}&length={length}"
        if download_link:
            return {'csv': url+"&download_as=csv", 'collection': url+"&download_as=collection"}
        req = self._get(url)
        if not req.ok or not req.content:
            return
        data = req.json()
        scores = list()
        try:
            for score in data['scores']:
                beatmap = Beatmap(**score['beatmap'])
                del score['beatmap']
                scores.append(Score(self, **score, beatmap=beatmap))
            return data['total'], scores
        except Exception as e:
            print(e)

    def get_user_clears(self, user_id, server="akatsuki", mode=0, relax=0, date=date.today(), beatmap_filter='', score_filter='', sort: ScoreSortEnum = 'date', desc: bool = True, completed=3, page=1, length=100, download_link=False) -> Tuple[int, List[Score]] | Dict[str, str] | None:
        url = f"{self.url}/user/clears?server={server}&user_id={user_id}&mode={mode}&relax={relax}&date={date.strftime('%Y-%m-%d')}&beatmap_filter={beatmap_filter}&score_filter={score_filter}&sort={sort}&desc={desc}&completed={completed}&page={page}&length={length}"
        if download_link:
            return {'csv': url+"&download_as=csv", 'collection': url+"&download_as=collection"}
        req = self._get(url)
        if not req.ok or not req.content:
            return
        data = req.json()
        scores = list()
        try:
            for score in data['scores']:
                beatmap = Beatmap(**score['beatmap'])
                del score['beatmap']
                scores.append(Score(self, **score, beatmap=beatmap))
            return data['total'], scores
        except:
            return

    def get_all_clears(self, server="akatsuki", mode=0, relax=0, date=date.today(), beatmap_filter='', score_filter='', sort: ScoreSortEnum = 'date', desc: bool = True, completed=3, page=1, length=100, download_link=False) -> Tuple[int, List[Score]] | Dict[str, str] | None:
        url = f"{self.url}/user/clears/all?server={server}&mode={mode}&relax={relax}&date={date.strftime('%Y-%m-%d')}&beatmap_filter={beatmap_filter}&score_filter={score_filter}&sort={sort}&desc={desc}&completed={completed}&page={page}&length={length}"
        if download_link:
            return {'csv': url+"&download_as=csv", 'collection': url+"&download_as=collection"}
        req = self._get(url)
        if not req.ok or not req.content:
            return
        data = req.json()
        scores = list()
        try:
            for score in data['scores']:
                beatmap = Beatmap(**score['beatmap'])
                del score['beatmap']
                scores.append(Score(self, **score, beatmap=beatmap))
            return data['total'], scores
        except:
            return

    def get_user_rank(self, user_id, server="akatsuki", mode=0, relax=0, type: UserLeaderboardTypeEnum=UserLeaderboardTypeEnum.pp) -> UserRank | None:
        req = self._get(f"{self.url}/user/rank?server={server}&user_id={user_id}&mode={mode}&relax={relax}&type={type}")
        if not req.ok or not req.content:
            return
        return UserRank(**req.json())

    def get_clan_info(self, clan_id, server="akatsuki") -> Clan | None:
        req = self._get(f"{self.url}/clan/info?server={server}&clan_id={clan_id}")
        if not req.ok or not req.content:
            return
        try:
            return Clan(self, **req.json())
        except:
            return

    def get_clan_members(self, clan_id, server="akatsuki") -> List[User] | None:
        req = self._get(f"{self.url}/clan/members?server={server}&clan_id={clan_id}")
        if not req.ok or not req.content:
            return
        members = list()
        try:
            for user in req.json():
                members.append(User(self, **user))
            return members
        except:
            return

    def get_clan_stats(self, clan_id, server="akatsuki", mode=0, relax=0, date=date.today()) -> ClanStatistics | None:
        req = self._get(f"{self.url}/clan/stats?server={server}&clan_id={clan_id}&mode={mode}&relax={relax}&date={date.strftime('%Y-%m-%d')}")
        if not req.ok or not req.content:
            return
        try:
            return ClanStatistics(self, **req.json())
        except:
            return
    
    def get_beatmap_sets(self) -> List[ServerBeatmaps] | None:
        req = self._get(f"{self.url}/beatmaps/server_sets")
        if not req.ok or not req.content:
            return
        servers = list()
        try:
            for server, sets in req.json().items():
                servers.append(ServerBeatmaps(server_name=server, beatmap_sets=sets))
            return servers
        except:
            return
    
    def get_beatmap(self, beatmap_id: int) -> Beatmap | None:
        req = self._get(f"{self.url}/beatmap?beatmap_id={beatmap_id}")
        if not req.ok or not req.content:
            return
        return Beatmap(**req.json())
    
    def get_beatmaps(self, page: int = 1, length: int = 100, sort: BeatmapSortEnum = "title", desc = False, unplayed_by: UserFilter = None, beatmap_filter: str = "", download_link: bool = False) -> Tuple[int, List[Beatmap]] | None:
        url = f"{self.url}/beatmaps/list?page={page}&length={length}&sort={sort}&desc={desc}&beatmap_filter={beatmap_filter}"
        if unplayed_by:
            url += f"&unplayed_by_filter={unplayed_by.format()}"
        if download_link:
            return {'csv': url+"&download_as=csv", 'collection': url+"&download_as=collection"}
        req = self._get(url)
        if not req.ok or not req.content:
            return
        try:
            data = req.json()
            return data['total'], [Beatmap(**beatmap) for beatmap in data['beatmaps']]
        except:
            return