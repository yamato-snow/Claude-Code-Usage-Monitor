# 🎯 Claude Code使用量監視ツール
[![PyPI Version](https://img.shields.io/pypi/v/claude-monitor.svg)](https://pypi.org/project/claude-monitor/)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![codecov](https://codecov.io/gh/Maciek-roboblog/Claude-Code-Usage-Monitor/branch/main/graph/badge.svg)](https://codecov.io/gh/Maciek-roboblog/Claude-Code-Usage-Monitor)

Claude AIのトークン使用量をリアルタイムで監視する美しいターミナルツールです。高度な分析機能、機械学習ベースの予測、Rich UIを搭載しています。トークン消費、バーンレート、コスト分析を追跡し、セッション制限に関するインテリジェントな予測を提供します。

![Claude Token Monitor Screenshot](https://raw.githubusercontent.com/Maciek-roboblog/Claude-Code-Usage-Monitor/main/doc/scnew.png)

---

## 📑 目次

- [✨ 主な機能](#-主な機能)
- [🚀 インストール](#-インストール)
  - [⚡ uvによるモダンなインストール（推奨）](#-uvによるモダンなインストール推奨)
  - [📦 pipによるインストール](#-pipによるインストール)
  - [🛠️ その他のパッケージマネージャー](#️-その他のパッケージマネージャー)
- [📖 使い方](#-使い方)
  - [ヘルプを表示](#ヘルプを表示)
  - [基本的な使用方法](#基本的な使用方法)
  - [設定オプション](#設定オプション)
  - [利用可能なプラン](#利用可能なプラン)
- [🙏 このリリースのテストにご協力ください！](#-このリリースのテストにご協力ください)
- [✨ 機能と動作原理](#-機能と動作原理)
  - [現在の機能](#現在の機能)
  - [Claudeセッションについて理解する](#claudeセッションについて理解する)
  - [プラン別トークン制限](#プラン別トークン制限)
  - [スマート検出機能](#スマート検出機能)
- [🚀 使用例](#-使用例)
  - [一般的なシナリオ](#一般的なシナリオ)
  - [ベストプラクティス](#ベストプラクティス)
- [🔧 開発者向けインストール](#-開発者向けインストール)
- [トラブルシューティング](#トラブルシューティング)
  - [インストール時の問題](#インストール時の問題)
  - [実行時の問題](#実行時の問題)
- [📞 お問い合わせ](#-お問い合わせ)
- [📚 追加ドキュメント](#-追加ドキュメント)
- [📝 ライセンス](#-ライセンス)
- [🤝 貢献者](#-貢献者)
- [🙏 謝辞](#-謝辞)

## ✨ 主な機能

### 🚀 **v3.0.0 メジャーアップデート - 完全なアーキテクチャ再構築**

- **🌐 完全日本語化対応** - 日本語と英語の完全なローカライゼーション、自動言語検出
- **🔮 ML（機械学習）ベースの予測** - P90パーセンタイル計算とインテリジェントなセッション制限検出
- **🔄 リアルタイム監視** - 設定可能な更新頻度（0.1-20 Hz）とインテリジェントな表示更新
- **📊 高度なRich UI** - 美しいカラーコード付きプログレスバー、テーブル、レイアウト（WCAG準拠コントラスト）
- **🤖 スマート自動検出** - カスタム制限発見による自動プラン切り替え
- **📋 強化されたプランサポート** - 更新された制限：Pro（44k）、Max5（88k）、Max20（220k）、Custom（P90ベース）
- **⚠️ 高度な警告システム** - コストと時間予測を含む多段階アラート
- **💼 プロフェッショナルアーキテクチャ** - 単一責任原則（SRP）準拠のモジュラー設計
- **🎨 インテリジェントテーマ** - 自動ターミナル背景検出による科学的カラースキーム
- **⏰ 高度なスケジューリング** - 自動検出されるシステムタイムゾーンと時刻形式設定
- **📈 コスト分析** - キャッシュトークン計算を含むモデル固有の価格設定
- **🔧 Pydantic検証** - 自動検証付きタイプセーフ設定
- **📝 包括的ログ記録** - 設定可能レベルでのオプションファイルログ記録
- **🧪 広範囲テスト** - 完全カバレッジの100+テストケース
- **🎯 エラーレポート** - 本番環境監視用オプションSentry統合
- **⚡ パフォーマンス最適化** - 高度なキャッシングと効率的なデータ処理

### 📋 デフォルトCustomプラン

**Custom プラン**が新しいデフォルトオプションで、5時間のClaude Codeセッション専用に設計されています。3つの重要な指標を監視します：
- **トークン使用量** - トークン消費を追跡
- **メッセージ使用量** - メッセージ数を監視
- **コスト使用量** - 長時間セッションで最も重要な指標

Customプランは、過去192時間（8日間）のすべてのセッションを分析し、実際の使用量に基づいてパーソナライズされた制限を計算することで、使用パターンに自動的に適応します。これにより、特定のワークフローに合わせた正確な予測と警告が提供されます。

## 🚀 インストール
### ⚡ uvによるモダンなインストール（推奨）

**uvが最良の選択である理由：**
- ✅ 自動的に分離された環境を作成（システム競合なし）
- ✅ Pythonバージョンの問題なし
- ✅ "externally-managed-environment"エラーなし
- ✅ 簡単な更新とアンインストール
- ✅ すべてのプラットフォームで動作

監視ツールをインストールして使用する最も速く簡単な方法：

[![PyPI](https://img.shields.io/pypi/v/claude-monitor.svg)](https://pypi.org/project/claude-monitor/)

#### PyPIからインストール

```bash
# uvでPyPIから直接インストール（最も簡単）
uv tool install claude-monitor

# どこからでも実行
claude-monitor  # または短縮形：cmonitor、ccmonitor
```

#### ソースからインストール

```bash
# ソースからクローンしてインストール
git clone https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor.git
cd Claude-Code-Usage-Monitor
uv tool install .

# どこからでも実行
claude-monitor
```

#### uv初回ユーザー
uvがまだインストールされていない場合は、1つのコマンドで取得できます：

```bash
# Linux/macOS:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# インストール後、ターミナルを再起動してください
```

### 📦 pipによるインストール

```bash
# PyPIからインストール
pip install claude-monitor

# claude-monitorコマンドが見つからない場合、~/.local/binをPATHに追加：
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc  # またはターミナルを再起動

# どこからでも実行
claude-monitor  # または短縮形：cmonitor、ccmonitor
```

> **⚠️ PATH設定**: WARNING: The script claude-monitor is installed in '/home/username/.local/bin' which is not on PATHが表示された場合、上記のexport PATHコマンドを実行してください。
>
> **⚠️ 重要**: 最新のLinuxディストリビューション（Ubuntu 23.04+、Debian 12+、Fedora 38+）では、"externally-managed-environment"エラーが発生する場合があります。--break-system-packagesを使用する代わりに、以下を強く推奨します：
> 1. **代わりにuvを使用**（上記参照） - より安全で簡単
> 2. **仮想環境を使用** - python3 -m venv myenv && source myenv/bin/activate
> 3. **pipxを使用** - pipx install claude-monitor
>
> 詳細な解決策については、トラブルシューティングセクションをご覧ください。

### 🛠️ その他のパッケージマネージャー

#### pipx（分離された環境）
```bash
# pipxでインストール
pipx install claude-monitor

# どこからでも実行
claude-monitor  # または短縮形：claude-code-monitor、cmonitor、ccmonitor、ccm
```

#### conda/mamba
```bash
# conda環境でpipを使用してインストール
pip install claude-monitor

# どこからでも実行
claude-monitor  # または短縮形：cmonitor、ccmonitor
```

## 📖 使い方

### ヘルプを表示

```bash
# ヘルプ情報を表示
claude-monitor --help
```

#### 利用可能なコマンドラインパラメータ

| パラメータ | 型 | デフォルト | 説明 |
|-----------|------|---------|-------------|
| --plan | string | custom | プランタイプ: pro、max5、max20、またはcustom |
| --custom-limit-tokens | int | None | customプラン用のトークン制限（0より大きい必要があります） |
| --view | string | realtime | 表示タイプ: realtime、daily、またはmonthly |
| --timezone | string | auto | タイムゾーン（自動検出）。例: UTC、America/New_York、Europe/London |
| --time-format | string | auto | 時刻形式: 12h、24h、またはauto |
| --theme | string | auto | 表示テーマ: light、dark、classic、またはauto |
| --refresh-rate | int | 10 | データ更新頻度（秒）（1-60） |
| --refresh-per-second | float | 0.75 | 表示更新頻度（Hz）（0.1-20.0） |
| --reset-hour | int | None | 日次リセット時刻（0-23） |
| --log-level | string | INFO | ログレベル: DEBUG、INFO、WARNING、ERROR、CRITICAL |
| --log-file | path | None | ログファイルパス |
| --debug | flag | False | デバッグログを有効にする |
| --version, -v | flag | False | バージョン情報を表示 |
| --clear | flag | False | 保存された設定をクリア |

#### プランオプション

| プラン | トークン制限 | コスト制限 | 説明 |
|------|-------------|------------------|-------------|
| pro | 19,000 | $18.00 | Claude Pro サブスクリプション |
| max5 | 88,000 | $35.00 | Claude Max5 サブスクリプション |
| max20 | 220,000 | $140.00 | Claude Max20 サブスクリプション |
| custom | P90ベース | (デフォルト) $50.00 | ML分析による自動検出 |

#### コマンドエイリアス

このツールは以下のコマンドで呼び出すことができます：
- claude-monitor（メイン）
- claude-code-monitor（完全名）
- cmonitor（短縮形）
- ccmonitor（短縮形代替）
- ccm（最短）

#### 設定保存機能

監視ツールは設定を自動的に保存し、毎回再指定する必要がありません：

**保存される項目：**
- 表示タイプ（--view）
- テーマ設定（--theme）
- タイムゾーン設定（--timezone）
- 時刻形式（--time-format）
- 更新頻度（--refresh-rate、--refresh-per-second）
- リセット時刻（--reset-hour）
- カスタムトークン制限（--custom-limit-tokens）

**設定場所:** ~/.claude-monitor/last_used.json

**使用例：**
```bash
# 初回実行 - 設定を指定
claude-monitor --plan pro --theme dark --timezone "Asia/Tokyo"

# 以降の実行 - 設定が自動的に復元
claude-monitor --plan pro

# このセッションで保存設定を上書き
claude-monitor --plan pro --theme light

# 保存されたすべての設定をクリア
claude-monitor --clear
```

**主な機能：**
- ✅ セッション間での自動パラメータ永続化
- ✅ CLIオプションは常に保存設定を上書き
- ✅ 破損を防ぐアトミックファイル操作
- ✅ 設定ファイルが破損した場合のグレースフルフォールバック
- ✅ プランパラメータは保存されません（毎回指定が必要）

### 基本的な使用方法

#### uvツールインストール（推奨）
```bash
# デフォルト（自動検出付きCustomプラン）
claude-monitor

# 代替コマンド
claude-code-monitor  # 完全な説明名
cmonitor             # 短縮エイリアス
ccmonitor            # 短縮代替
ccm                  # 最短エイリアス

# 監視ツールを終了
# Ctrl+Cを押して正常に終了
```

#### 開発モード
ソースから実行する場合は、src/ディレクトリからpython -m claude_monitorを使用してください。

### 設定オプション

#### プランを指定

```bash
# P90自動検出付きCustomプラン（デフォルト）
claude-monitor --plan custom

# Proプラン（約44,000トークン）
claude-monitor --plan pro

# Max5プラン（約88,000トークン）
claude-monitor --plan max5

# Max20プラン（約220,000トークン）
claude-monitor --plan max20

# 明示的なトークン制限付きCustomプラン
claude-monitor --plan custom --custom-limit-tokens 100000
```

#### カスタムリセット時刻

```bash
# 午前3時にリセット
claude-monitor --reset-hour 3

# 午後10時にリセット
claude-monitor --reset-hour 22
```

#### 使用量表示設定

```bash
# ライブ更新付きリアルタイム監視（デフォルト）
claude-monitor --view realtime

# テーブル形式で集計された日次トークン使用量
claude-monitor --view daily

# テーブル形式で集計された月次トークン使用量
claude-monitor --view monthly
```

#### パフォーマンスと表示設定

```bash
# 更新頻度を調整（1-60秒、デフォルト: 10）
claude-monitor --refresh-rate 5

# 表示更新頻度を調整（0.1-20 Hz、デフォルト: 0.75）
claude-monitor --refresh-per-second 1.0

# 時刻形式を設定（デフォルトで自動検出）
claude-monitor --time-format 24h  # または12h

# 特定のテーマを強制
claude-monitor --theme dark  # light、dark、classic、auto

# 保存された設定をクリア
claude-monitor --clear
```

#### 言語設定

ツールは日本語と英語の両方をサポートしています。デフォルトでは日本語が使用されます：

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

#### タイムゾーン設定

デフォルトのタイムゾーンは**システムから自動検出**されます。有効なタイムゾーンで上書き可能：

```bash
# 東京時間を使用
claude-monitor --timezone Asia/Tokyo

# 米国東部時間を使用
claude-monitor --timezone America/New_York

# UTCを使用
claude-monitor --timezone UTC

# ロンドン時間を使用
claude-monitor --timezone Europe/London
```

#### ログ記録とデバッグ

```bash
# デバッグログを有効
claude-monitor --debug

# ファイルにログ出力
claude-monitor --log-file ~/.claude-monitor/logs/monitor.log

# ログレベルを設定
claude-monitor --log-level WARNING  # DEBUG、INFO、WARNING、ERROR、CRITICAL
```

### 利用可能なプラン

| プラン | トークン制限 | 最適な用途 |
|------|-----------------|----------|
| **custom** | P90自動検出 | インテリジェント制限検出（デフォルト） |
| **pro** | 約19,000 | Claude Pro サブスクリプション |
| **max5** | 約88,000 | Claude Max5 サブスクリプション |
| **max20** | 約220,000 | Claude Max20 サブスクリプション |

#### 高度なプラン機能

- **P90分析**: Customプランは使用履歴から90パーセンタイル計算を使用
- **コスト追跡**: キャッシュトークン計算を含むモデル固有の価格設定
- **制限検出**: 95%信頼度でのインテリジェント閾値検出

## 🚀 v3.0.0の新機能

### 主な変更点

#### **完全なアーキテクチャ再構築**
- 単一責任原則（SRP）準拠のモジュラー設計
- タイプセーフティと検証付きPydanticベース設定
- オプションSentry統合による高度なエラーハンドリング
- 100+テストケースによる包括的テストスイート

#### **機能強化**
- **P90分析**: 90パーセンタイル計算を使用した機械学習ベースの制限検出
- **更新されたプラン制限**: Pro（44k）、Max5（88k）、Max20（220k）トークン
- **コスト分析**: キャッシュトークン計算を含むモデル固有の価格設定
- **Rich UI**: 自動ターミナル背景検出によるWCAG準拠テーマ

#### **新しいCLIオプション**
- --refresh-per-second: 設定可能な表示更新頻度（0.1-20 Hz）
- --time-format: 自動12h/24h形式検出
- --custom-limit-tokens: customプラン用の明示的なトークン制限
- --log-fileと--log-level: 高度なログ記録機能
- --clear: 保存された設定をリセット
- 便利なコマンドエイリアス: claude-code-monitor、cmonitor、ccmonitor、ccm

#### **破壊的変更**
- パッケージ名がclaude-usage-monitorからclaude-monitorに変更
- デフォルトプランがproからcustom（自動検出付き）に変更
- 最小Pythonバージョンが3.9+に引き上げ
- コマンド構造が更新（上記の例を参照）

## ✨ 機能と動作原理

### v3.0.0アーキテクチャ概要

新バージョンでは、単一責任原則（SRP）に従ったモジュラーアーキテクチャによる完全な再構築が特徴です：

### 🖥️ ユーザーインターフェース層

| コンポーネント | 説明 |
| -------------------- | --------------------- |
| **CLIモジュール** | Pydanticベース |
| **設定/コンフィグ** | タイプセーフ |
| **エラーハンドリング** | Sentry対応 |
| **Rich Terminal UI** | 適応テーマ |

---

### 🎛️ 監視オーケストレーター

| コンポーネント | 主な責任 |
| ------------------------ | ---------------------------------------------------------------- |
| **中央制御ハブ** | セッション管理・リアルタイムデータフロー・コンポーネント調整 |
| **データマネージャー** | キャッシュ管理・ファイルI/O・状態永続化 |
| **セッション監視** | リアルタイム・5時間ウィンドウ・トークン追跡 |
| **UI制御** | Rich表示・プログレスバー・テーマシステム |
| **分析** | P90計算機・バーンレート・予測 |

---

### 🏗️ 基盤層

| コンポーネント | コア機能 |
| ------------------- | ------------------------------------------------------- |
| **コアモデル** | セッションデータ・設定スキーマ・タイプセーフティ |
| **分析エンジン** | MLアルゴリズム・統計・予測 |
| **ターミナルテーマ** | 自動検出・WCAGカラー・コントラスト最適化 |
| **Claude APIデータ** | トークン追跡・コスト計算・セッションブロック |

---

**🔄 データフロー:**
Claude設定ファイル → データ層 → 分析エンジン → UIコンポーネント → ターミナル表示

### 現在の機能

#### 🔄 高度なリアルタイム監視
- 設定可能な更新間隔（1-60秒）
- 高精度表示更新（0.1-20 Hz）
- CPU使用量を最小化するインテリジェント変更検出
- コールバックシステム付きマルチスレッドオーケストレーション

#### 📊 Rich UIコンポーネント
- **プログレスバー**: 科学的コントラスト比によるWCAG準拠カラースキーム
- **データテーブル**: モデル固有統計による並び替え可能な列
- **レイアウトマネージャー**: ターミナルサイズに適応するレスポンシブデザイン
- **テーマシステム**: 最適な可読性のためのターミナル背景自動検出

#### 📈 複数の使用量表示
- **リアルタイム表示**（デフォルト）: プログレスバー、現在のセッションデータ、バーンレート分析によるライブ監視
- **日次表示**: 日付、モデル、入力/出力/キャッシュトークン、総トークン、コストを表示する日次統計集計
- **月次表示**: 長期トレンド分析と予算計画のための月次集計データ

#### 🔮 機械学習予測
- **P90計算機**: インテリジェント制限検出のための90パーセンタイル分析
- **バーンレート分析**: マルチセッション消費パターン分析
- **コスト予測**: キャッシュトークン計算を含むモデル固有価格設定
- **セッション予測**: 使用パターンに基づいてセッション期限を予測

#### 🤖 インテリジェント自動検出
- **背景検出**: ターミナルテーマ（明/暗）を自動判定
- **システム統合**: タイムゾーンと時刻形式設定を自動検出
- **プラン認識**: 使用パターンを分析して最適なプランを提案
- **制限発見**: 履歴データをスキャンして実際のトークン制限を発見

### Claudeセッションについて理解する

#### Claude Codeセッションの仕組み

Claude Codeは**5時間のローリングセッションウィンドウシステム**で動作します：

1. **セッション開始**: Claudeへの最初のメッセージで開始
2. **セッション期間**: その最初のメッセージから正確に5時間継続
3. **トークン制限**: 各5時間セッションウィンドウ内で適用
4. **複数セッション**: 複数のアクティブセッションを同時に持つことが可能
5. **ローリングウィンドウ**: 他のセッションがまだアクティブな間に新しいセッションを開始可能

#### セッションリセットスケジュール

**セッションタイムラインの例:**
10:30 AM - 最初のメッセージ（セッションAが10 AMに開始）
03:00 PM - セッションA期限切れ（5時間後）

12:15 PM - 最初のメッセージ（セッションBが12PMに開始）
05:15 PM - セッションB期限切れ（5時間後の5PM）

#### バーンレート計算

監視ツールは洗練された分析を使用してバーンレートを計算します：

1. **データ収集**: 過去1時間のすべてのセッションからトークン使用量を収集
2. **パターン分析**: 重複するセッション間での消費トレンドを特定
3. **速度追跡**: 1分あたりのトークン消費を計算
4. **予測エンジン**: 現在のセッショントークンがいつ枯渇するかを推定
5. **リアルタイム更新**: 使用パターンの変化に応じて予測を調整

### プラン別トークン制限

#### v3.0.0更新されたプラン制限

| プラン | 制限（トークン） | コスト制限 | メッセージ | アルゴリズム |
|------|----------------|------------------|----------|-----------|
| **Claude Pro** | 19,000 | $18.00 | 250 | 固定制限 |
| **Claude Max5** | 88,000 | $35.00 | 1,000 | 固定制限 |
| **Claude Max20** | 220,000 | $140.00 | 2,000 | 固定制限 |
| **Custom** | P90ベース | (デフォルト) $50.00 | 250+ | 機械学習 |

#### 高度な制限検出

- **P90分析**: 履歴使用量の90パーセンタイルを使用
- **信頼度閾値**: 制限検出で95%の精度
- **キャッシュサポート**: キャッシュ作成と読み取りトークンコストを含む
- **モデル固有**: Claude 3.5、Claude 4、将来のモデルに適応

### 技術要件

#### 依存関係（v3.0.0）

```toml
# コア依存関係（自動インストール）
pytz>=2023.3                # タイムゾーン処理
rich>=13.7.0                # Rich ターミナルUI
pydantic>=2.0.0             # タイプ検証
pydantic-settings>=2.0.0    # 設定管理
numpy>=1.21.0               # 統計計算
sentry-sdk>=1.40.0          # エラーレポート（オプション）
pyyaml>=6.0                 # 設定ファイル
tzdata                      # Windows タイムゾーンデータ
```

#### Python要件

- **最小**: Python 3.9+
- **推奨**: Python 3.11+
- **テスト済み**: Python 3.9、3.10、3.11、3.12、3.13

### スマート検出機能

#### 自動プラン切り替え

デフォルトのProプランを使用している場合：

1. **検出**: 監視ツールがトークン使用量が7,000を超えることを検知
2. **分析**: 実際の制限について以前のセッションをスキャン
3. **切り替え**: 自動的にcustom_maxモードに変更
4. **通知**: 変更について明確なメッセージを表示
5. **継続**: 新しい、より高い制限で監視を継続

#### 制限発見プロセス

自動検出システム：

1. **履歴をスキャン**: 利用可能なすべてのセッションブロックを調査
2. **ピークを発見**: 達成された最高のトークン使用量を特定
3. **データを検証**: データ品質と最新性を確保
4. **制限を設定**: 発見された最大値を新しい制限として使用
5. **パターンを学習**: 実際の使用能力に適応

## 🚀 使用例

### 一般的なシナリオ

#### 🌅 朝型開発者
**シナリオ**: 午前9時に作業を開始し、スケジュールに合わせてトークンをリセットしたい。

```bash
# カスタムリセット時刻を午前9時に設定
claude-monitor --reset-hour 9

# タイムゾーンと合わせて
claude-monitor --reset-hour 9 --timezone Asia/Tokyo
```

**メリット**:
- リセット時刻が作業スケジュールに合致
- 日次トークン配分のより良い計画
- 予測可能なセッションウィンドウ

#### 🌙 夜型コーダー
**シナリオ**: しばしば深夜過ぎまで作業し、柔軟なリセットスケジューリングが必要。

```bash
# 明確な日次境界のため深夜にリセット
claude-monitor --reset-hour 0

# 夜遅くのリセット（午後11時）
claude-monitor --reset-hour 23
```

**戦略**:
- リセット時刻周辺で重いコーディングセッションを計画
- 深夜の作業セッションをまたぐため遅いリセットを使用
- ピーク時間中のバーンレートを監視

#### 🔄 制限が変動するヘビーユーザー
**シナリオ**: トークン制限が変化しているようで、正確なプランが不明。

```bash
# 最高の過去使用量を自動検出
claude-monitor --plan custom

# カスタムスケジューリングで監視
claude-monitor --plan custom --reset-hour 6
```

**アプローチ**:
- 自動検出に実際の制限を発見させる
- 1週間監視してパターンを理解
- 制限が変化またはリセットする時を記録

#### 🌍 国際ユーザー
**シナリオ**: 異なるタイムゾーンで作業または旅行中。

```bash
# 米国東海岸
claude-monitor --timezone America/New_York

# ヨーロッパ
claude-monitor --timezone Europe/London

# アジア太平洋
claude-monitor --timezone Asia/Singapore

# 国際チーム調整のためUTC
claude-monitor --timezone UTC --reset-hour 12
```

#### ⚡ クイックチェック
**シナリオ**: 設定なしで現在の状態を確認したい。

```bash
# デフォルトでそのまま実行
claude-monitor

# 状態確認後Ctrl+Cを押す
```

#### 📊 使用量分析表示
**シナリオ**: 異なる期間でのトークン使用パターンを分析。

```bash
# 詳細統計付き日次使用量内訳を表示
claude-monitor --view daily

# 月次トークン消費トレンドを分析
claude-monitor --view monthly --plan max20

# 分析用に日次使用データをログファイルにエクスポート
claude-monitor --view daily --log-file ~/daily-usage.log

# 異なるタイムゾーンで使用量を確認
claude-monitor --view daily --timezone America/New_York
```

**用途**:
- **リアルタイム**: 現在のセッションとバーンレートのライブ監視
- **日次**: 日次消費パターンを分析し、ピーク使用日を特定
- **月次**: 長期トレンド分析と月次予算計画

### プラン選択戦略

#### プランの選び方

**デフォルトから開始（新規ユーザー推奨）**
```bash
# 自動切り替え付きProプラン検出
claude-monitor
```

- Pro制限を超えた場合、監視ツールが検出
- 必要に応じて自動的にcustom_maxに切り替え
- 切り替え発生時に通知を表示

**既知のサブスクリプションユーザー**
```bash
# Max5を持っていることが分かっている場合
claude-monitor --plan max5

# Max20を持っていることが分かっている場合
claude-monitor --plan max20
```

**不明な制限**
```bash
# 過去の使用量から自動検出
claude-monitor --plan custom
```

### ベストプラクティス

#### セットアップのベストプラクティス

1. **セッション早期開始**

```bash
   # Claude作業開始時に監視を開始（uvインストール）
   claude-monitor

   # または開発モード
   claude-monitor
   ```

   - 開始からの正確なセッション追跡
   - より良いバーンレート計算
   - 制限接近の早期警告

2. **モダンインストールを使用（推奨）**

```bash
   # uvでの簡単なインストールと更新
   uv tool install claude-monitor
   claude-monitor --plan max5
   ```

   - クリーンなシステムインストール
   - 簡単な更新とメンテナンス
   - どこからでも利用可能

3. **カスタムシェルエイリアス（レガシーセットアップ）**

```bash
   # ~/.bashrcまたは~/.zshrcに追加（開発セットアップのみ）
   alias claude-monitor='cd ~/Claude-Code-Usage-Monitor && source venv/bin/activate && claude-monitor'
   ```

#### 使用のベストプラクティス

1. **バーンレート速度の監視**
   - トークン消費の急激な増加に注意
   - 残り時間に基づいてコーディング強度を調整
   - セッションリセット周辺で大きなリファクタリングを計画

2. **戦略的セッション計画**

```bash
   # リセット時刻周辺で重い使用量を計画
   claude-monitor --reset-hour 9
   ```

   - リセット後に大きなタスクをスケジュール
   - 制限に近づいている時は軽いタスクを使用
   - 複数の重複するセッションを活用

3. **タイムゾーン認識**

```bash
   # 常に実際のタイムゾーンを使用
   claude-monitor --timezone Asia/Tokyo
   ```

   - 正確なリセット時刻予測
   - 作業スケジュールのより良い計画
   - 正確なセッション期限推定

#### 最適化のヒント

1. **ターミナルセットアップ**
   - 少なくとも80文字幅のターミナルを使用
   - より良い視覚的フィードバックのためカラーサポートを有効（COLORTERM環境変数を確認）
   - 監視専用のターミナルウィンドウを検討
   - 最高のテーマ体験のためtruecolorサポート付きターミナルを使用

2. **ワークフロー統合**

```bash
   # 開発セッションと一緒に監視を開始（uvインストール）
   tmux new-session -d -s claude-monitor 'claude-monitor'

   # または開発モード
   tmux new-session -d -s claude-monitor 'claude-monitor'

   # いつでも状態を確認
   tmux attach -t claude-monitor
   ```

3. **マルチセッション戦略**
   - セッションは正確に5時間継続することを覚えておく
   - 複数の重複するセッションを持つことができる
   - セッション境界をまたいで作業を計画

#### 実世界のワークフロー

**大規模プロジェクト開発**
```bash
# 持続的開発のためのセットアップ
claude-monitor --plan max20 --reset-hour 8 --timezone Asia/Tokyo
```

**日次ルーチン**:
1. **8:00 AM**: 新しいトークン、主要機能を開始
2. **10:00 AM**: バーンレートを確認、強度を調整
3. **12:00 PM**: 午後のセッション計画のため監視
4. **2:00 PM**: 新しいセッションウィンドウ、複雑な問題に取り組む
5. **4:00 PM**: 軽いタスク、夕方のセッション準備

**学習と実験**
```bash
# 学習のための柔軟なセットアップ
claude-monitor --plan pro
```

**スプリント開発**
```bash
# 高強度開発セットアップ
claude-monitor --plan max20 --reset-hour 6
```

## 🔧 開発者向けインストール

ソースコードで作業したい貢献者と開発者向け：

### クイックスタート（開発/テスト）

```bash
# リポジトリをクローン
git clone https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor.git
cd Claude-Code-Usage-Monitor

# 開発モードでインストール
pip install -e .

# ソースから実行
python -m claude_monitor
```

### v3.0.0テスト機能

新バージョンには包括的なテストスイートが含まれています：

- **100+テストケース**の完全カバレッジ
- すべてのコンポーネントの**ユニットテスト**
- エンドツーエンドワークフローの**統合テスト**
- ベンチマーク付き**パフォーマンステスト**
- 分離されたテストのための**モックオブジェクト**

```bash
# テストを実行
cd src/
python -m pytest

# カバレッジ付きで実行
python -m pytest --cov=claude_monitor --cov-report=html

# 特定のテストモジュールを実行
python -m pytest tests/test_analysis.py -v
```

### 前提条件

1. システムに**Python 3.9+**がインストールされている
2. リポジトリクローンのための**Git**

### 仮想環境セットアップ

#### なぜ仮想環境を使用するのか？

仮想環境の使用は**強く推奨**されます。理由：

- **🛡️ 分離**: システムPythonをクリーンに保ち、依存関係の競合を防ぐ
- **📦 ポータビリティ**: 異なるマシンで正確な環境を簡単に複製
- **🔄 バージョン管理**: 安定性のため依存関係の特定バージョンをロック
- **🧹 クリーンアンインストール**: すべてを削除するため仮想環境フォルダを単に削除
- **👥 チーム協業**: 全員が同じPythonとパッケージバージョンを使用

#### virtualenvのインストール（必要な場合）

venvモジュールが利用できない場合：

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-venv

# Fedora/RHEL/CentOS
sudo dnf install python3-venv

# macOS（通常Pythonに付属）
# 利用できない場合、HomebrewでPythonをインストール：
brew install python3

# Windows（通常Pythonに付属）
# 利用できない場合、python.orgからPythonを再インストール
# インストール時に「Add Python to PATH」をチェックしてください
```

または、virtualenvパッケージを使用：
```bash
# pipでvirtualenvをインストール
pip install virtualenv

# 次に以下で仮想環境を作成：
virtualenv venv
# 代わりに: python3 -m venv venv
```

#### ステップバイステップセットアップ

```bash
# 1. リポジトリをクローン
git clone https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor.git
cd Claude-Code-Usage-Monitor

# 2. 仮想環境を作成
python3 -m venv venv
# またはvirtualenvパッケージを使用する場合：
# virtualenv venv

# 3. 仮想環境を有効化
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# 4. Python依存関係をインストール
pip install pytz
pip install rich>=13.0.0

# 5. スクリプトを実行可能にする（Linux/Macのみ）
chmod +x claude_monitor.py

# 6. 監視ツールを実行
python claude_monitor.py
```

#### 日常使用

初期セットアップ後は、以下のみが必要：

```bash
# プロジェクトディレクトリに移動
cd Claude-Code-Usage-Monitor

# 仮想環境を有効化
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 監視ツールを実行
claude-monitor  # Linux/Mac
# python claude_monitor.py  # Windows

# 完了したら、非有効化
deactivate
```

#### プロのヒント: シェルエイリアス

クイックアクセス用のエイリアスを作成：
```bash
# ~/.bashrcまたは~/.zshrcに追加
alias claude-monitor='cd ~/Claude-Code-Usage-Monitor && source venv/bin/activate && claude-monitor'

# そして実行するだけ：
claude-monitor
```

## トラブルシューティング

### インストール時の問題

#### "externally-managed-environment"エラー

最新のLinuxディストリビューション（Ubuntu 23.04+、Debian 12+、Fedora 38+）では、以下のエラーが発生する場合があります：
```
error: externally-managed-environment
× This environment is externally managed
```

**解決策（優先順位順）：**

1. **uvを使用（推奨）**

```bash
   # 最初にuvをインストール
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # そしてuvでインストール
   uv tool install claude-monitor
   ```

2. **pipxを使用（分離された環境）**

```bash
   # pipxをインストール
   sudo apt install pipx  # Ubuntu/Debian
   # または
   python3 -m pip install --user pipx

   # claude-monitorをインストール
   pipx install claude-monitor
   ```

3. **仮想環境を使用**

```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install claude-monitor
   ```

4. **強制インストール（推奨しません）**

```bash
   pip install --user claude-monitor --break-system-packages
   ```

   ⚠️ **警告**: これはシステム保護をバイパスし、競合を引き起こす可能性があります。代わりに仮想環境の使用を強く推奨します。

#### pipインストール後にコマンドが見つからない

pipインストール後にclaude-monitorコマンドが見つからない場合：

1. **PATHの問題かどうか確認**

```bash
   # pipインストール中の警告メッセージを探す：
   # WARNING: The script claude-monitor is installed in '/home/username/.local/bin' which is not on PATH
   ```

2. **PATHに追加**

```bash
   # ~/.bashrcまたは~/.zshrcに追加
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

   # シェルを再読み込み
   source ~/.bashrc  # または source ~/.zshrc
   ```

3. **インストール場所を確認**

```bash
   # pipがスクリプトをどこにインストールしたか確認
   pip show -f claude-monitor | grep claude-monitor
   ```

4. **Pythonで直接実行**

```bash
   python3 -m claude_monitor
   ```

#### Pythonバージョンの競合

複数のPythonバージョンがある場合：

1. **Pythonバージョンを確認**

```bash
   python3 --version
   pip3 --version
   ```

2. **特定のPythonバージョンを使用**

```bash
   python3.11 -m pip install claude-monitor
   python3.11 -m claude_monitor
   ```

3. **uvを使用（Pythonバージョンを自動処理）**

```bash
   uv tool install claude-monitor
   ```

### 実行時の問題

#### アクティブなセッションが見つかりません
No active session foundエラーが発生した場合は、以下の手順に従ってください：

1. **初期テスト**:
   Claude Codeを起動し、少なくとも2つのメッセージを送信してください。場合によっては、最初の試行でセッションが正しく初期化されないことがありますが、いくつかのやり取り後に解決されます。

2. **設定パス**:
   問題が続く場合は、カスタム設定パスを指定することを検討してください。デフォルトでは、Claude Codeは~/.config/claudeを使用します。環境に応じてこのパスを調整する必要がある場合があります。

```bash
CLAUDE_CONFIG_DIR=~/.config/claude claude-monitor
```

## 📞 お問い合わせ

ご質問、提案、またはコラボレーションをお考えですか？お気軽にお問い合わせください！

**📧 メール**: [maciek@roboblog.eu](mailto:maciek@roboblog.eu)

セットアップのヘルプが必要、機能リクエスト、バグ発見、または潜在的な改善について議論したい場合は、遠慮なくご連絡ください。Claude Code使用量監視ツールのユーザーからのご連絡をいつでもお待ちしています！

## 📚 追加ドキュメント

- **[開発ロードマップ](DEVELOPMENT.md)** - ML機能、PyPIパッケージ、Docker計画
- **[貢献ガイド](CONTRIBUTING.md)** - 貢献方法、開発ガイドライン
- **[トラブルシューティング](TROUBLESHOOTING.md)** - 一般的な問題と解決策

## 📝 ライセンス

[MITライセンス](LICENSE) - 必要に応じて自由に使用・修正してください。

## 🤝 貢献者

- [@adawalli](https://github.com/adawalli)
- [@taylorwilsdon](https://github.com/taylorwilsdon)
- [@moneroexamples](https://github.com/moneroexamples)

貢献したいですか？[貢献ガイド](CONTRIBUTING.md)をご確認ください！

## 🙏 謝辞

### スポンサー

このプロジェクトを継続させるのに役立つサポーターの皆様に特別な感謝を：

**Ed** - *Buy Me Coffee サポーター*
> 「あなたの作品を世界と共有することに感謝します。これは私が一日を軌道に乗せるのに役立ちます。質の高いreadmeで、本当に素晴らしいものです！」

## Star履歴

[![Star History Chart](https://api.star-history.com/svg?repos=Maciek-roboblog/Claude-Code-Usage-Monitor&type=Date)](https://www.star-history.com/#Maciek-roboblog/Claude-Code-Usage-Monitor&Date)

---

<div align="center">

**⭐ 有用だと思ったらこのリポジトリにスターを付けてください！ ⭐**

[バグ報告](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/issues) • [機能リクエスト](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/issues) • [貢献](CONTRIBUTING.md)

</div>
