import argparse
import html
import re
import sys
from pathlib import Path

import requests


def main() -> None:
    args = parse_args()
    post_update(args)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Partner update tool")
    parser.add_argument(
        "--telegram-bot-token",
        required=True,
        type=str,
        help="Telegram Bot API Token",
    )
    parser.add_argument(
        "--telegram-channel-id",
        required=True,
        type=str,
        help="Telegram channel for partner updates",
    )
    parser.add_argument(
        "--message-file",
        required=True,
        type=str,
        help="Path to file with the update message",
    )
    return parser.parse_args()


def post_update(args: argparse.Namespace) -> None:
    message = Path(args.message_file).read_text(encoding="utf-8")
    formatted_message = format_message(message)

    url = f"https://api.telegram.org/bot{args.telegram_bot_token}/sendMessage"
    params = {
        "chat_id": args.telegram_channel_id,
        "text": formatted_message,
        "parse_mode": "HTML",
        "disable_web_page_preview": "true",
    }

    try:
        response = requests.post(url, params=params, timeout=30)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get("ok"):
            print(f"Posted message_id: {response_json['result']['message_id']}")
            return

        print(f"Failed to post message: response = {response_json}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to post message: error = {exc}", file=sys.stderr)
        sys.exit(1)


def format_message(message: str) -> str:
    lines = []
    for raw_line in message.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            lines.append("")
            continue

        if stripped.startswith("## "):
            lines.append(f"<b>{format_inline(stripped[3:])}</b>")
            continue

        if stripped.startswith("# "):
            lines.append(f"<b>{format_inline(stripped[2:])}</b>")
            continue

        if stripped.startswith("- "):
            lines.append(f"• {format_inline(stripped[2:])}")
            continue

        lines.append(format_inline(stripped))

    return "\n".join(lines)


def format_inline(text: str) -> str:
    formatted = html.escape(text, quote=False)
    formatted = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda match: (
            f'<a href="{html.escape(match.group(2), quote=True)}">'
            f"{match.group(1)}</a>"
        ),
        formatted,
    )
    formatted = re.sub(
        r"`([^`]+)`",
        lambda match: f"<code>{match.group(1)}</code>",
        formatted,
    )
    formatted = re.sub(
        r"\*\*([^*]+)\*\*",
        lambda match: f"<b>{match.group(1)}</b>",
        formatted,
    )
    return formatted


if __name__ == "__main__":
    main()
