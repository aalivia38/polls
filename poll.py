import os, json, requests

token = os.environ["BOT_TOKEN"]
chat = os.environ["CHAT_ID"]

options = ["10:00", "12:00", "14:00", "16:00",
           "17:00", "18:00", "19:00", "20:00", "👀"]

for question in ["Climbing Nekala", "Climbing Lielahti"]:
    requests.post(
        f"https://api.telegram.org/bot{token}/sendPoll",
        data={
            "chat_id": chat,
            "question": question,
            "options": json.dumps(options),
            "is_anonymous": "false",
            "allows_multiple_answers": "true",
        },
    )
