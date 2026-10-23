import os
import re
import sys
from typing import Any

__version__ = "0.2.0"

filename = os.path.basename(__file__)

# Standard colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Extra convenience colors
ORANGE = "\033[38;5;208m"
PURPLE = "\033[38;5;135m"
PINK = "\033[38;5;213m"
TEAL = "\033[38;5;50m"
GRAY = "\033[38;5;244m"

# Text styles
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
STRIKETHROUGH = "\033[9m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Bright background colors
BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"

__all__ = [
    "BLACK",
    "RED",
    "GREEN",
    "YELLOW",
    "BLUE",
    "MAGENTA",
    "CYAN",
    "WHITE",
    "BRIGHT_BLACK",
    "BRIGHT_RED",
    "BRIGHT_GREEN",
    "BRIGHT_YELLOW",
    "BRIGHT_BLUE",
    "BRIGHT_MAGENTA",
    "BRIGHT_CYAN",
    "BRIGHT_WHITE",
    "ORANGE",
    "PURPLE",
    "PINK",
    "TEAL",
    "GRAY",
    "RESET",
    "BOLD",
    "DIM",
    "ITALIC",
    "UNDERLINE",
    "STRIKETHROUGH",
    "BG_BLACK",
    "BG_RED",
    "BG_GREEN",
    "BG_YELLOW",
    "BG_BLUE",
    "BG_MAGENTA",
    "BG_CYAN",
    "BG_WHITE",
    "BG_BRIGHT_BLACK",
    "BG_BRIGHT_RED",
    "BG_BRIGHT_GREEN",
    "BG_BRIGHT_YELLOW",
    "BG_BRIGHT_BLUE",
    "BG_BRIGHT_MAGENTA",
    "BG_BRIGHT_CYAN",
    "BG_BRIGHT_WHITE",
    "style",
    "colorize",
    "strip_ansi",
    "success",
    "warning",
    "error",
    "info",
    "debug",
    "note",
    "critical",
    "question",
    "header",
    "title",
    "separator",
    "box",
    "__version__",
]


def _should_use_color() -> bool:
    if os.getenv("NO_COLOR"):
        return False
    if os.getenv("PYCRISTAL_FORCE_COLOR"):
        return True
    return True


def strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", str(text))


def style(text: Any, *, fg: str | None = None, bg: str | None = None, bold: bool = False, dim: bool = False, italic: bool = False, underline: bool = False, strikethrough: bool = False) -> str:
    if not _should_use_color():
        return str(text)

    codes = []
    if fg:
        codes.append(fg)
    if bg:
        codes.append(bg)
    if bold:
        codes.append(BOLD)
    if dim:
        codes.append(DIM)
    if italic:
        codes.append(ITALIC)
    if underline:
        codes.append(UNDERLINE)
    if strikethrough:
        codes.append(STRIKETHROUGH)

    if not codes:
        return str(text)

    return f"{''.join(codes)}{text}{RESET}"


def colorize(text: Any, color: str | None = None, *, background: str | None = None, bold: bool = False, dim: bool = False, italic: bool = False, underline: bool = False, strikethrough: bool = False) -> str:
    return style(text, fg=color, bg=background, bold=bold, dim=dim, italic=italic, underline=underline, strikethrough=strikethrough)


def _format_message(label: str, text: Any, color: str, *, bold: bool = True, label_color: str | None = None) -> str:
    message = str(text)
    if label:
        prefix = f"[{label}]" if label_color is None else style(f"[{label}]", fg=label_color, bold=True)
        return style(f"{prefix} {message}", fg=color, bold=bold)
    return style(message, fg=color, bold=bold)


def success(text: Any, *, label: str = "SUCCESS", color: str = GREEN, label_color: str | None = None, end: str = "\n") -> None:
    print(_format_message(label, text, color, label_color=label_color or GREEN), end=end)


def warning(text: Any, *, label: str = "WARNING", color: str = YELLOW, label_color: str | None = None, end: str = "\n") -> None:
    print(_format_message(label, text, color, label_color=label_color or YELLOW), end=end)


def error(text: Any, *, label: str = "ERROR", color: str = RED, label_color: str | None = None, end: str = "\n") -> None:
    print(_format_message(label, text, color, label_color=label_color or RED), end=end)


def info(text: Any, *, label: str = "INFO", color: str = CYAN, label_color: str | None = None, end: str = "\n") -> None:
    print(_format_message(label, text, color, label_color=label_color or CYAN), end=end)


def debug(text: Any, *, label: str = "DEBUG", color: str = BRIGHT_BLUE, label_color: str | None = None, end: str = "\n") -> None:
    print(_format_message(label, text, color, label_color=label_color or BRIGHT_BLUE), end=end)


def note(text: Any, *, label: str = "NOTE", color: str = BLUE, label_color: str | None = None, end: str = "\n") -> None:
    print(_format_message(label, text, color, label_color=label_color or BLUE), end=end)


def critical(text: Any, *, label: str = "CRITICAL", color: str = BRIGHT_RED, label_color: str | None = None, end: str = "\n") -> None:
    print(_format_message(label, text, color, label_color=label_color or BRIGHT_RED), end=end)


def question(text: Any, *, label: str = "QUESTION", color: str = MAGENTA, label_color: str | None = None, end: str = "\n") -> None:
    print(_format_message(label, text, color, label_color=label_color or MAGENTA), end=end)


def header(text: Any, *, char: str = "=", width: int = 60, color: str = CYAN, end: str = "\n") -> None:
    title_text = str(text)
    spacer = max(width - len(strip_ansi(title_text)) - 2, 1)
    left = char * (spacer // 2)
    right = char * (spacer - (spacer // 2))
    print(style(f"{left} {title_text} {right}", fg=color, bold=True), end=end)


def title(text: Any, *, color: str = BRIGHT_CYAN, end: str = "\n") -> None:
    print(style(f"{text}", fg=color, bold=True, underline=True), end=end)


def separator(char: str = "-", width: int = 60, *, color: str = GRAY, end: str = "\n") -> None:
    print(style(char * width, fg=color), end=end)


def box(text: Any, *, title: str | None = None, width: int = 50, color: str = CYAN, border: str = "#", end: str = "\n") -> None:
    content = str(text)
    inner_width = max(10, width - 4)
    title_line = f" {title} " if title else ""
    top = style(f"{border * width}", fg=color)
    body = []
    if title_line:
        body.append(style(f"{border} {title_line:<{inner_width}} {border}", fg=color, bold=True))
    for line in content.splitlines() or [""]:
        safe_line = line[:inner_width]
        body.append(style(f"{border} {safe_line:<{inner_width}} {border}", fg=color))
    body.append(style(f"{border * width}", fg=color))
    print(top)
    print("\n".join(body), end=end)


if __name__ == "__main__":
    title("PyCristal Demo")
    info("Application started successfully.")
    success("Project build completed.")
    warning("A few files were skipped.")
    error("Something went wrong.")
    debug("Debug mode enabled.")
    question("Would you like to continue?")
    header("Status Report", width=42, color=GREEN)
    box("Everything is running smoothly.", title="Summary", color=RED)