"""Message localization system for Claude Monitor.

This module provides a simple message localization system that supports
English and Japanese languages.
"""

import os
from typing import Dict, Any

# Current locale (default to Japanese for Japanese users)
_current_locale = os.environ.get("CLAUDE_MONITOR_LOCALE", "ja")

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
        
        # ヘルプメッセージ
        "help.timezone_examples": "例: UTC, America/New_York, Europe/London, Asia/Tokyo",
        "help.refresh_rate": "更新頻度（秒）（1-60）",
        "help.theme_options": "テーマオプション: light, dark, classic, auto",
    }
}


def set_locale(locale: str) -> None:
    """Set the current locale.
    
    Args:
        locale: Locale code ('en' or 'ja')
    """
    global _current_locale
    if locale in MESSAGES:
        _current_locale = locale
    else:
        _current_locale = "en"  # fallback to English


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
    message = messages.get(key, key)  # fallback to key if not found
    
    if kwargs:
        try:
            return message.format(**kwargs)
        except (KeyError, ValueError):
            return message
    
    return message
