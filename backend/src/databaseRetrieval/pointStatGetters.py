from datetime import datetime
from sqlalchemy import or_
from sqlalchemy import desc
from ..models.playerStats import PlayerStats
from ..models.game import Game
from database import db

def average_and_recent_stat(player_id, num_games, stat_column, team_id=None):
    num_games = int(num_games)
    query = db.session.query(stat_column).join(Game)

    if team_id:
        query = query.filter(
            or_(
                Game.home_team_id == team_id,
                Game.visitor_team_id == team_id
            )
        )

    recent_stats = (
        query
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(Game.date.desc())
        .limit(num_games)
        .all()
    )

    num_games_available = len(recent_stats)
    if num_games_available < num_games:
        num_games = num_games_available

    if not recent_stats:
        return [0.0, []]

    total_stat = sum(stat[0] for stat in recent_stats)
    average_stat = round(total_stat / num_games, 1)

    return [average_stat, [stat[0] for stat in recent_stats]]


def pointsByNumGames(player_id, num_games):
    result = {
        'points': average_and_recent_stat(player_id, num_games, PlayerStats.pts)
    }
    return result

def pointsByNumGames_teams(player_id, num_games, team_id):
    result = {
        'points': average_and_recent_stat(player_id, num_games, PlayerStats.pts, team_id)
    }
    return result

def allByNumGames(player_id, num_games):
    result = {
        'average_points': round(average_and_recent_stat(player_id, num_games, PlayerStats.pts)[0], 1),
        'assists': round(average_and_recent_stat(player_id, num_games, PlayerStats.ast)[0], 1),
        'rebounds': round(average_and_recent_stat(player_id, num_games, PlayerStats.reb)[0], 1),
        'free_throws': round(average_and_recent_stat(player_id, num_games, PlayerStats.ftm)[0], 1),
        'three_pointers': round(average_and_recent_stat(player_id, num_games, PlayerStats.fg3m)[0], 1),
    }

    result['PRA'] = round(result['average_points'] + result['rebounds'] + result['assists'], 1)

    return result

def allByNumGamesByTeam(player_id, num_games, team_id):
    result = {
        'average_points': round(average_and_recent_stat(player_id, num_games, PlayerStats.pts, team_id)[0], 1),
        'assists': round(average_and_recent_stat(player_id, num_games, PlayerStats.ast, team_id)[0], 1),
        'rebounds': round(average_and_recent_stat(player_id, num_games, PlayerStats.reb, team_id)[0], 1),
        'free_throws': round(average_and_recent_stat(player_id, num_games, PlayerStats.ftm, team_id)[0], 1),
        'three_pointers': round(average_and_recent_stat(player_id, num_games, PlayerStats.fg3m, team_id)[0], 1),
   
    }