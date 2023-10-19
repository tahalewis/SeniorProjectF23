from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from database import db

def average_and_recent_stat(player_id, num_games, stat_column, team_id=None):
    num_games = int(num_games)

    query = db.session.query(stat_column)
    
    if team_id:
        query = query.filter(
            (PlayerStats.game.home_team_id == team_id) | (PlayerStats.game.visitor_team_id == team_id)
        )
    
    recent_stats = (
        query
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(Game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_stats:
        return [0.0, []]

    total_stat = sum(stat[0] for stat in recent_stats)
    average_stat = round(total_stat / num_games, 2)

    return [average_stat, [stat[0] for stat in recent_stats]]

def assistsByNumGames(player_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.ast)

def assistsByNumGames_teams(player_id, team_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.ast, team_id)

def reboundsByNumGames(player_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.reb)

def reboundsByNumGames_team(player_id, team_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.reb, team_id)