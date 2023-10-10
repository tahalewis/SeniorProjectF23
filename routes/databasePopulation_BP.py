from flask import Blueprint
from backend.src.models.player import Player
from backend.src.models.game import Game
from backend.src.models.playerStats import PlayerStats

databasePopulate_BP = Blueprint("data_populate", __name__)

@databasePopulate_BP.route('/populate_data', methods=['GET'])
def populate_data():
    PlayerStats.fetch_and_insert_stats()
    return "Data population process initiated."

@databasePopulate_BP.route('/populate_players', methods=['GET'])
def populate_players():
    Player.fetch_and_insert_players()
    return "Player population process initiated."

@databasePopulate_BP.route('/populate_games', methods=['GET'])
def populate_games():
    Game.fetch_and_insert_games()
    return "Game population process initiated."
