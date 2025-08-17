# 使用方法ガイド - Claude Code使用量監視ツール

## 基本的なコマンド

### インストール後の基本使用
```bash
# デフォルト設定で起動（自動検出付きCustomプラン）
claude-monitor

# 短縮コマンド
cmonitor
ccmonitor
ccm
```

### プラン指定
```bash
# Proプラン（約19,000トークン）
claude-monitor --plan pro

# Max5プラン（約88,000トークン）
claude-monitor --plan max5

# Max20プラン（約220,000トークン）
claude-monitor --plan max20

# Customプラン（P90自動検出）
claude-monitor --plan custom

# 明示的なトークン制限付きCustomプラン
claude-monitor --plan custom --custom-limit-tokens 100000
```

### 表示モード
```bash
# リアルタイム監視（デフォルト）
claude-monitor --view realtime

# 日次使用量表示
claude-monitor --view daily

# 月次使用量表示
claude-monitor --view monthly
```

### タイムゾーンと時刻設定
```bash
# 東京時間を使用
claude-monitor --timezone Asia/Tokyo

# 24時間表示を強制
claude-monitor --time-format 24h

# 12時間表示を強制
claude-monitor --time-format 12h

# 自動検出（デフォルト）
claude-monitor --timezone auto --time-format auto
```

### 言語設定
```bash
# 日本語を強制（デフォルト）
claude-monitor --locale ja

# 英語を強制
claude-monitor --locale en

# システム設定に基づく自動検出
claude-monitor --locale auto

# 環境変数で設定
export CLAUDE_MONITOR_LOCALE=ja
claude-monitor
```

### テーマ設定
```bash
# ダークテーマを強制
claude-monitor --theme dark

# ライトテーマを強制
claude-monitor --theme light

# クラシックテーマ
claude-monitor --theme classic

# 自動検出（デフォルト）
claude-monitor --theme auto
```

### 更新頻度設定
```bash
# データ更新頻度を5秒に設定
claude-monitor --refresh-rate 5

# 表示更新頻度を1Hzに設定
claude-monitor --refresh-per-second 1.0

# 低CPU使用量設定
claude-monitor --refresh-rate 30 --refresh-per-second 0.5
```

### ログ記録
```bash
# デバッグログを有効
claude-monitor --debug

# ファイルにログ出力
claude-monitor --log-file ~/.claude-monitor/logs/monitor.log

# ログレベルを設定
claude-monitor --log-level WARNING
```

### リセット時刻設定
```bash
# 午前9時にリセット（日本の一般的な始業時間）
claude-monitor --reset-hour 9

# 深夜0時にリセット
claude-monitor --reset-hour 0
```

## 実践的な使用例

### 朝型開発者向け
```bash
# 午前9時開始、東京時間、Proプラン
claude-monitor --plan pro --reset-hour 9 --timezone Asia/Tokyo
```

### 夜型開発者向け
```bash
# 深夜リセット、ダークテーマ
claude-monitor --plan max5 --reset-hour 0 --theme dark
```

### 高負荷開発プロジェクト
```bash
# Max20プラン、高頻度更新、詳細ログ
claude-monitor --plan max20 --refresh-rate 5 --log-level DEBUG
```

### 使用量分析
```bash
# 日次使用量を詳細ログ付きで確認
claude-monitor --view daily --log-file ~/usage-analysis.log

# 月次トレンド分析
claude-monitor --view monthly --timezone Asia/Tokyo
```

### 軽量監視
```bash
# 低CPU使用量で長時間監視
claude-monitor --refresh-rate 60 --refresh-per-second 0.1
```

## 設定の保存と管理

### 設定の自動保存
- 以下の設定は自動的に保存され、次回起動時に復元されます：
  - `--view` (表示モード)
  - `--theme` (テーマ)
  - `--timezone` (タイムゾーン)
  - `--time-format` (時刻形式)
  - `--refresh-rate` (更新頻度)
  - `--reset-hour` (リセット時刻)
  - `--custom-limit-tokens` (カスタムトークン制限)

### 設定のクリア
```bash
# 保存された設定をすべてクリア
claude-monitor --clear
```

### 設定ファイル場所
```
~/.claude-monitor/last_used.json
```

## トラブルシューティング

### よくある問題

#### "アクティブなセッションが見つかりません"
```bash
# Claude Codeで2-3回メッセージを送信してから再試行
claude-monitor --debug
```

#### 文字化けが発生する場合
```bash
# UTF-8エンコーディングを確認
export LANG=ja_JP.UTF-8
claude-monitor
```

#### ターミナルが狭すぎる場合
- 最低80文字幅のターミナルを使用してください
- より良い表示のため100文字以上を推奨

### ヘルプとバージョン情報
```bash
# ヘルプを表示
claude-monitor --help

# バージョン情報を表示
claude-monitor --version
claude-monitor -v
```

## 高度な使用方法

### tmuxとの組み合わせ
```bash
# バックグラウンドで監視を開始
tmux new-session -d -s claude-monitor 'claude-monitor --plan max20'

# 監視画面にアタッチ
tmux attach -t claude-monitor

# 監視セッションを終了
tmux kill-session -t claude-monitor
```

### 複数プロジェクトの監視
```bash
# プロジェクトAの監視
tmux new-session -d -s project-a 'claude-monitor --plan pro --log-file ~/project-a.log'

# プロジェクトBの監視
tmux new-session -d -s project-b 'claude-monitor --plan max5 --log-file ~/project-b.log'
```

### 自動化スクリプト
```bash
#!/bin/bash
# start-claude-monitor.sh

# 時間帯に応じて設定を変更
HOUR=$(date +%H)

if [ $HOUR -lt 12 ]; then
    # 午前中: 軽めの設定
    claude-monitor --plan pro --refresh-rate 15
elif [ $HOUR -lt 18 ]; then
    # 午後: 標準設定
    claude-monitor --plan max5 --refresh-rate 10
else
    # 夜間: 高頻度監視
    claude-monitor --plan max20 --refresh-rate 5
fi
```

## パフォーマンス最適化

### CPU使用量を削減
```bash
# 低頻度更新
claude-monitor --refresh-rate 30 --refresh-per-second 0.25
```

### メモリ使用量を削減
```bash
# ログを無効化
claude-monitor --log-level ERROR
```

### ネットワーク負荷を削減
```bash
# 更新頻度を下げる
claude-monitor --refresh-rate 60
```

このガイドを参考に、あなたの開発スタイルに最適な設定を見つけてください！
