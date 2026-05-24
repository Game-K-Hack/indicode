import os
import json
import locale

# Dossier contenant les fichiers de langue (un .json par langue)
LANGS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "langs")

# Langue de repli si la traduction demandée est introuvable
FALLBACK_LANG = "en"

_translations: dict = {}
_fallback: dict = {}
_current_lang: str = FALLBACK_LANG


def available_languages() -> list[str]:
    """Retourne la liste des codes de langue disponibles (ex: ['en', 'fr'])."""
    if not os.path.isdir(LANGS_DIR):
        return []
    return sorted(
        f[:-5] for f in os.listdir(LANGS_DIR) if f.endswith(".json")
    )


def _load(lang: str) -> dict:
    path = os.path.join(LANGS_DIR, f"{lang}.json")
    if not os.path.isfile(path):
        return {}
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def detect_language() -> str:
    """Détecte la langue à utiliser.

    Priorité : variable d'environnement INDICODE_LANG, puis langue du
    système, puis langue de repli.
    """
    langs = available_languages()

    env = os.environ.get("INDICODE_LANG")
    if env and env[:2].lower() in langs:
        return env[:2].lower()

    try:
        sys_lang = (locale.getlocale()[0] or locale.getdefaultlocale()[0] or "")
    except Exception:
        sys_lang = ""
    if sys_lang and sys_lang[:2].lower() in langs:
        return sys_lang[:2].lower()

    return FALLBACK_LANG


def set_language(lang: str) -> None:
    """Charge la langue donnée (et la langue de repli)."""
    global _translations, _fallback, _current_lang
    _fallback = _load(FALLBACK_LANG)
    _translations = _load(lang) if lang != FALLBACK_LANG else _fallback
    _current_lang = lang


def current_language() -> str:
    return _current_lang


def t(key: str, **kwargs) -> str:
    """Traduit une clé. Les paramètres nommés sont injectés via str.format."""
    text = _translations.get(key) or _fallback.get(key) or key
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass
    return text


# Chargement automatique à l'import
set_language(detect_language())
