from datetime import datetime
from sqlalchemy import func, or_
from sqlalchemy.orm import joinedload
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from database import db

def average_and_recent_stat(player_id, num_games, stat_column, team_id=None):
    query = db.session.query(stat_column)

    query = query.filter(PlayerStats.player_id == player_id)
    if team_id is not None:
        query = query.join(PlayerStats.game).filter(
            or_(PlayerStats.game.home_team_id == team_id, PlayerStats.game.visitor_team_id == team_id)
        )
    query = query.filter(PlayerStats.min != '00:00', PlayerStats.min != '00')
    query = query.join(PlayerStats.game).order_by(Game.date.desc()).limit(num_games)
    recent_stats = query.all()

    if not recent_stats:
        return [0.0, []]

    total_stat = sum(stat[0] for stat in recent_stats)
    average_stat = round(total_stat / num_games, 2)

    return [average_stat, [stat[0] for stat in recent_stats]]

def FTMByNumGames(player_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.ftm)

def FTMByNumGames_team(player_id, team_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.ftm, team_id)

def threesByNumGames(player_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.fg3m)

def threesByNumGames_team(player_id, team_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.fg3m, team_id)
