from database import db
from flask import Blueprint, jsonify, request

skins_bp = Blueprint("skins", __name__)


def format_skin(skin):
    return {
        "name": skin["name"],
        "weapon": skin["weapon"]["name"],
        "rarity": {
            "name": skin["rarity"]["name"],
            "color": skin["rarity"].get("color", ""),
        },
        "description": skin["description"],
        "category": skin["category"]["name"],
        "pattern": skin["pattern"]["name"],
        "wear": skin["wear"]["name"],
        "min_float": skin.get("min_float"),
        "max_float": skin.get("max_float"),
        "stattrak": skin["stattrak"],
        "souvenir": skin["souvenir"],
        "team": skin["team"]["name"],
        "image": skin["image"],
        "market_hash_name": skin["market_hash_name"],
    }


# Get all skins
@skins_bp.route("/api/skins", methods=["GET"])
def get_skins():
    skins = list(db.skins.find())
    result = [format_skin(skin) for skin in skins]
    return jsonify(result)


@skins_bp.route("/api/skins/name/<skin_name>", methods=["GET"])
def get_skin_by_name(skin_name):
    # Perform a case-insensitive partial match search
    skins = list(db.skins.find({"name": {"$regex": skin_name, "$options": "i"}}))

    if not skins:
        return jsonify({"error": "No skins found matching the given name"}), 404

    result = [format_skin(skin) for skin in skins]
    return jsonify(result)


# Get skins by weapon
@skins_bp.route("/api/skins/weapon/<weapon_name>", methods=["GET"])
def get_skins_by_weapon(weapon_name):
    skins = list(db.skins.find({"weapon.name": weapon_name}))
    if not skins:
        return jsonify({"error": "No skins found for this weapon"}), 404
    result = [format_skin(skin) for skin in skins]
    return jsonify(result)
