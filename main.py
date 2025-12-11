# Speedium Services 2025. Developed by mirayakdogan.
import requests


def get_user_pfp(bot_token: str, user_id: str):
    url = f"https://discord.com/api/v10/users/{user_id}"
    headers = {"Authorization": f"Bot {bot_token}"}

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("Error:", r.status_code, r.text)
        return

    data = r.json()

    avatar_hash = data.get("avatar")
    if avatar_hash is None:
        print("User has no avatar.")
        return

    # Choose image format
    if avatar_hash.startswith("a_"):
        fmt = "gif"
    else:
        fmt = "png"

    avatar_url = (
        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.{fmt}?size=4096"
    )

    print("Avatar URL:", avatar_url)

    # Download it
    img = requests.get(avatar_url)
    filename = f"{user_id}.{fmt}"

    with open(filename, "wb") as f:
        f.write(img.content)

    print(f"Saved as {filename}")


if __name__ == "__main__":
    token = input("Bot Token: ")
    uid = input("User ID: ")
    get_user_pfp(token, uid)
