import requests
import json
from .result import GenericResult, SeasonalResult
from .platforms import Platform
from .seasons import Seasons


class Stats:
    def __init__(self, key):
        self.key = key


    def get_generic_stats(self, username, platform: Platform):
        headers = {"Authorization": f"Bearer {self.key}"}

        request = requests.get(f'https://api2.r6stats.com/public-api/stats/{username}/{platform}/generic',
                               headers=headers)
        content = json.loads(request.content)

        return GenericResult(
            username=content["username"],
            platform=content["platform"],
            ubisoft_id=content["ubisoft_id"],
            uplay_id=content["uplay_id"],
            avatar_url=content["avatar_url_256"],
            last_updated=content["last_updated"],
            aliases=content["aliases"],
            level=content["progression"]["level"],
            lootbox_probability=content["progression"]["lootbox_probability"],
            total_xp=content["progression"]["total_xp"],
            assists=content["stats"]["general"]["assists"],
            barricades_deployed=content["stats"]["general"]["barricades_deployed"],
            blind_kills=content["stats"]["general"]["blind_kills"],
            bullets_fired=content["stats"]["general"]["bullets_fired"],
            bullets_hit=content["stats"]["general"]["bullets_hit"],
            dbnos=content["stats"]["general"]["dbnos"],
            deaths=content["stats"]["general"]["deaths"],
            distance_travelled=content["stats"]["general"]["distance_travelled"],
            draws=content["stats"]["general"]["draws"],
            gadgets_destroyed=content["stats"]["general"]["gadgets_destroyed"],
            games_played=content["stats"]["general"]["games_played"],
            headshots=content["stats"]["general"]["headshots"],
            kd=content["stats"]["general"]["kd"],
            kills=content["stats"]["general"]["kills"],
            losses=content["stats"]["general"]["losses"],
            melee_kills=content["stats"]["general"]["melee_kills"],
            penetration_kills=content["stats"]["general"]["penetration_kills"],
            playtime=content["stats"]["general"]["playtime"],
            rappel_breaches=content["stats"]["general"]["rappel_breaches"],
            reinforcements_deployed=content["stats"]["general"]["reinforcements_deployed"],
            revives=content["stats"]["general"]["revives"],
            suicides=content["stats"]["general"]["suicides"],
            wins=content["stats"]["general"]["wins"],
            wl=content["stats"]["general"]["wl"],
            casual_data=content["stats"]["queue"]["casual"],
            ranked_data=content["stats"]["queue"]["ranked"],
            unranked_data=content["stats"]["queue"]["other"],
            gamemode_bomb=content["stats"]["gamemode"]["bomb"],
            gamemode_secure=content["stats"]["gamemode"]["secure_area"],
            gamemode_hostage=content["stats"]["gamemode"]["hostage"]
        )


    def get_seasonal_stats(self, username, platform: Platform, season: Seasons):
        headers = {"Authorization": f"Bearer {self.key}"}

        request = requests.get(f'https://api2.r6stats.com/public-api/stats/{username}/{platform}/seasonal',
                               headers=headers)
        content = json.loads(request.content)

        region = content["seasons"][season]["regions"]["ncsa"][0]

        return SeasonalResult(
            username=content["username"],
            platform=content["platform"],
            ubisoft_id=content["ubisoft_id"],
            uplay_id=content["uplay_id"],
            avatar_url=content["avatar_url_256"],
            last_updated=content["last_updated"],
            name=content["seasons"][season]["name"],
            start_date=content["seasons"][season]["start_date"],
            end_date=content["seasons"][season]["end_date"],
            abandons=region["abandons"],
            losses=region["losses"],
            max_rank=region["max_rank"],
            max_mmr=region["max_mmr"],
            mmr=region["mmr"],
            next_rank_mmr=region["next_rank_mmr"],
            prev_rank_mmr=region["prev_rank_mmr"],
            rank=region["rank"],
            skill_mean=region["skill_mean"],
            skill_standard_deviation=region["skill_standard_deviation"],
            created_for_date=region["created_for_date"],
            wins=region["wins"],
            kills=region["kills"],
            deaths=region["deaths"],
            last_match_mmr_change=region["last_match_mmr_change"],
            last_match_result=region["last_match_result"],
            last_match_skill_standard_deviation_change=region[
                                                                        "last_match_skill_standard_deviation_change"],
            last_match_skill_mean_change=region["last_match_skill_mean_change"],
            champions_rank_position=region["champions_rank_position"],
            max_rank_text=region["max_rank_text"],
            max_rank_image=region["max_rank_image"],
            rank_image=region["rank_image"],
            rank_text=region["rank_text"]
        )
