import os

import requests
from PIL import Image, ImageDraw, ImageOps, ImageFont

from poker.constants import player_places, right_panel_start, avatar_size, right_panel_avatar_size


def draw_text_on_image(current_game, poker_background, font_path):
    # Display general stats
    font = ImageFont.truetype(font_path, 32)
    draw = ImageDraw.Draw(poker_background)
    text = f"Players: {len(current_game.players)}\nBlind: {current_game.small_blind}\nPot: {current_game.pot}"
    text_color = (255, 255, 255)
    draw.text(right_panel_start, text, fill=text_color, font=font)

    # Display player credits
    # font = ImageFont.truetype(font_path, 85)
    # text = ""
    # text += "\n".join([f"{player.name[:10]}: {player.amount_of_credits}" for player in current_game.players])
    # draw.text(text_position, text, fill=text_color, font=font)

    return poker_background


def draw_player_action_on_image(poker_background, font_path, action):
    font = ImageFont.truetype(font_path, 24)
    draw = ImageDraw.Draw(poker_background)
    text_position = (54, 354)
    text_color = (255, 255, 255)
    draw.text(text_position, action, fill=text_color, font=font)

    return poker_background


def circular_avatar(image, size):
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    return output


async def create_avatars_for_player(client, player, current_game, player_background):
    for p, player_place in zip(current_game.players[current_game.get_player_index(player.player_id):] + current_game.players[:current_game.get_player_index(player.player_id)], player_places):
        discord_user = await client.fetch_user(p.player_id)
        if not os.path.exists(f"data_pictures/avatars/{discord_user.id}.png") or not os.path.exists(f"data_pictures/avatars/{discord_user.id}_right_panel.png"):
            avatar = discord_user.display_avatar
            if avatar is None:
                avatar = discord_user.default_avatar

            with requests.get(avatar.url) as r:
                img_data = r.content
            with open(f"data_pictures/avatars/{discord_user.id}.png", 'wb') as handler:
                handler.write(img_data)

            player_avatar = circular_avatar(Image.open(f"data_pictures/avatars/{discord_user.id}.png").convert('RGBA').resize(avatar_size), avatar_size)
            player_avatar.save(f"data_pictures/avatars/{discord_user.id}.png")
            player_avatar_right_panel = player_avatar.resize(right_panel_avatar_size)
            player_avatar_right_panel.save(f"data_pictures/avatars/{discord_user.id}_right_panel.png")
            player_avatar.close()
            player_avatar_right_panel.close()

        player_avatar = Image.open(f"data_pictures/avatars/{discord_user.id}.png")
        player_avatar_right_panel = Image.open(f"data_pictures/avatars/{discord_user.id}_right_panel.png")
        if p.player_id != player.player_id:
            player_background.paste(player_avatar, player_place[0], player_avatar)
        player_background.paste(player_avatar_right_panel, player_place[1], player_avatar_right_panel)
        player_avatar.close()

    return player_background


def draw_cross(image, cross_upper_left_position, cross_upper_right_position, cross_bottom_right_position, cross_bottom_left_position):
    draw = ImageDraw.Draw(image)
    draw.line([cross_upper_left_position, cross_bottom_right_position], fill="black", width=8)

    # Draw the vertical line of the cross
    draw.line([cross_upper_right_position, cross_bottom_left_position], fill="black", width=8)
