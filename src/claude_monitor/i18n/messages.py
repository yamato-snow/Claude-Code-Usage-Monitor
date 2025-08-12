"""Message localization system for Claude Monitor.

This module provides a simple message localization system that supports
English and Japanese languages.
"""

import os
import locale
from typing import Dict, Any

# Determine current locale with env/system detection; fallback to English
def _normalize_locale(value: str) -> str:
    v = (value or "").lower().replace("_", "-")
    if v.startswith("ja"):
        return "ja"
    if v.startswith("en"):
        return "en"
    return "en"

def _detect_default_locale() -> str:
    # Explicit env override
    env = os.environ.get("CLAUDE_MONITOR_LOCALE")
    if env:
        return _normalize_locale(env)
    # Common POSIX locale envs
    for var in ("LC_ALL", "LC_MESSAGES", "LANG"):
        v = os.environ.get(var)
        if v:
            return _normalize_locale(v)
    # Fallback to system default
    try:
        loc = locale.getdefaultlocale()[0] or ""
    except Exception:
        loc = ""
    return _normalize_locale(loc)

_current_locale = _detect_default_locale()

# Message translations
MESSAGES = {
    "en": {
        # Error messages
        "error.failed_to_get_data": "Failed to get usage data",
        "error.possible_causes": "Possible causes:",
        "error.not_logged_in": "You're not logged into Claude",
        "error.network_issues": "Network connection issues",
        "error.retrying": "Retrying in 3 seconds... (Ctrl+C to exit)",
        
        # Loading messages
        "loading.title": "⏳ Loading...",
        "loading.fetching_data": "Fetching Claude usage data...",
        "loading.calculating_limits": "Calculating your P90 session limits from usage history...",
        "loading.please_wait": "This may take a few seconds",
        
        # Session messages
        "session.no_active_session": "No active session found",
        "session.monitoring_stopped": "Monitoring stopped.",
        "session.tokens_used": "Tokens Used",
        "session.burn_rate": "Burn Rate",
        "session.cost": "Cost",
        "session.time_remaining": "Time Remaining",
        "session.session_progress": "Session Progress",
        
        # Plan messages
        "plan.custom": "Custom",
        "plan.pro": "Pro",
        "plan.max5": "Max5", 
        "plan.max20": "Max20",
        
        # Notification messages
        "notification.switching_to_custom": "Switching to custom plan due to higher usage detected",
        "notification.approaching_limit": "Approaching token limit",
        "notification.cost_warning": "Cost approaching limit",
        
        # UI messages
        "ui.title": "CLAUDE CODE USAGE MONITOR",
        "ui.session_based_limits": "📊 Session-Based Dynamic Limits",
        "ui.session_based_limits_desc": "Based on your historical usage patterns when hitting limits (P90)",
        "ui.cost_usage": "💰 Cost Usage:",
        "ui.token_usage": "📊 Token Usage:",
        "ui.messages_usage": "📨 Messages Usage:",
        "ui.time_to_reset": "⏱️  Time to Reset:",
        "ui.model_distribution": "🤖 Model Distribution:",
        "ui.burn_rate": "🔥 Burn Rate:",
        "ui.cost_rate": "💲 Cost Rate:",
        "ui.predictions": "🔮 Predictions:",
        
        # Help messages
        "help.timezone_examples": "Examples: UTC, America/New_York, Europe/London, Asia/Tokyo",
        "help.refresh_rate": "Refresh rate in seconds (1-60)",
        "help.theme_options": "Theme options: light, dark, classic, auto",
    },
    "ja": {
        # エラーメッセージ
        "error.failed_to_get_data": "使用データの取得に失敗しました",
        "error.possible_causes": "考えられる原因:",
        "error.not_logged_in": "Claudeにログインしていません",
        "error.network_issues": "ネットワーク接続の問題",
        "error.retrying": "3秒後に再試行します... (Ctrl+Cで終了)",
        
        # ローディングメッセージ
        "loading.title": "⏳ 読み込み中...",
        "loading.fetching_data": "Claude使用データを取得中...",
        "loading.calculating_limits": "使用履歴からP90セッション制限を計算中...",
        "loading.please_wait": "しばらくお待ちください",
        
        # セッションメッセージ
        "session.no_active_session": "アクティブなセッションが見つかりません",
        "session.monitoring_stopped": "監視を停止しました。",
        "session.tokens_used": "使用トークン数",
        "session.burn_rate": "消費レート",
        "session.cost": "コスト",
        "session.time_remaining": "残り時間",
        "session.session_progress": "セッション進行状況",
        
        # プランメッセージ
        "plan.custom": "カスタム",
        "plan.pro": "Pro",
        "plan.max5": "Max5",
        "plan.max20": "Max20",
        
        # 通知メッセージ
        "notification.switching_to_custom": "より高い使用量が検出されたため、カスタムプランに切り替えます",
        "notification.approaching_limit": "トークン制限に近づいています",
        "notification.cost_warning": "コストが制限に近づいています",
        
        # UIメッセージ
        "ui.title": "🎯 Claude Code使用量監視ツール",
        "ui.session_based_limits": "📊 セッションベース動的制限",
        "ui.session_based_limits_desc": "制限に達した際の履歴使用パターンに基づく（P90）",
        "ui.cost_usage": "💰 コスト使用量:",
        "ui.token_usage": "📊 トークン使用量:",
        "ui.messages_usage": "📨 メッセージ使用量:",
        "ui.time_to_reset": "⏱️  リセットまでの時間:",
        "ui.model_distribution": "🤖 モデル分布:",
        "ui.burn_rate": "🔥 消費レート:",
        "ui.cost_rate": "💲 コストレート:",
        "ui.predictions": "🔮 予測:",
        
        # ヘルプメッセージ
        "help.timezone_examples": "例: UTC, America/New_York, Europe/London, Asia/Tokyo",
        "help.refresh_rate": "更新頻度（秒）（1-60）",
        "help.theme_options": "テーマオプション: light, dark, classic, auto",
    }
}


def set_locale(locale: str) -> None:
    """Set the current locale.
    
    Args:
        locale: Locale code ('en', 'ja', or 'auto'; also accepts variants like 'ja_JP'/'en-US')
    """
    global _current_locale
    if locale and locale.lower() == "auto":
        _current_locale = _detect_default_locale()
        return
    normalized = _normalize_locale(locale)
    _current_locale = normalized if normalized in MESSAGES else "en"  # fallback to English


def get_current_locale() -> str:
    """Get the current locale.
    
    Returns:
        Current locale code
    """
    return _current_locale


def get_message(key: str, **kwargs: Any) -> str:
    """Get a localized message.
    
    Args:
        key: Message key in dot notation (e.g., 'error.failed_to_get_data')
        **kwargs: Format arguments for the message
        
    Returns:
        Localized message string
    """
    messages = MESSAGES.get(_current_locale, MESSAGES["en"])
    message = messages.get(key)
    if message is None:
        # Fallback to English if the key is missing in the active locale
        message = MESSAGES["en"].get(key, key)
    
    if kwargs and isinstance(message, str):
        try:
            return message.format(**kwargs)
        except (KeyError, ValueError):
            return message
    
    return message
