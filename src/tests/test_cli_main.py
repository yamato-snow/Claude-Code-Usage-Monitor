"""Simplified tests for CLI main module."""

from unittest.mock import Mock, patch

from claude_monitor.cli.main import main


class TestMain:
    """Test cases for main function."""

    def test_version_flag(self):
        """Test --version flag returns 0 and prints version."""
        with patch("builtins.print") as mock_print:
            result = main(["--version"])
            assert result == 0
            mock_print.assert_called_once()
            assert "claude-monitor" in mock_print.call_args[0][0]

    def test_v_flag(self):
        """Test -v flag returns 0 and prints version."""
        with patch("builtins.print") as mock_print:
            result = main(["-v"])
            assert result == 0
            mock_print.assert_called_once()
            assert "claude-monitor" in mock_print.call_args[0][0]

    @patch("claude_monitor.core.settings.Settings.load_with_last_used")
    def test_keyboard_interrupt_handling(self, mock_load):
        """Test keyboard interrupt returns 0."""
        mock_load.side_effect = KeyboardInterrupt()
        with patch("builtins.print") as mock_print:
            result = main(["--plan", "pro"])
            assert result == 0
            mock_print.assert_called_once_with("\n\nMonitoring stopped by user.")

    @patch("claude_monitor.core.settings.Settings.load_with_last_used")
    def test_exception_handling(self, mock_load_settings):
        """Test exception handling returns 1."""
        mock_load_settings.side_effect = Exception("Test error")

        with patch("builtins.print"), patch("traceback.print_exc"):
            result = main(["--plan", "pro"])
            assert result == 1

    @patch("claude_monitor.core.settings.Settings.load_with_last_used")
    @patch("claude_monitor.cli.bootstrap.setup_environment")
    @patch("claude_monitor.cli.bootstrap.ensure_directories")
    @patch("claude_monitor.cli.bootstrap.setup_logging")
    @patch("claude_monitor.cli.bootstrap.init_timezone")
    @patch("claude_monitor.cli.main._run_monitoring")
    def test_successful_main_execution(
        self,
        mock_run_monitoring,
        mock_init_timezone,
        mock_setup_logging,
        mock_ensure_directories,
        mock_setup_environment,
        mock_load_settings,
    ):
        """Test successful main execution."""
        mock_settings = Mock()
        mock_settings.log_file = None
        mock_settings.log_level = "INFO"
        mock_settings.timezone = "UTC"
        mock_settings.to_namespace.return_value = Mock()
        mock_load_settings.return_value = mock_settings

        result = main(["--plan", "pro"])

        assert result == 0
        mock_setup_environment.assert_called_once()
        mock_ensure_directories.assert_called_once()
        mock_setup_logging.assert_called_once()
        mock_init_timezone.assert_called_once_with("UTC")
        mock_run_monitoring.assert_called_once()


class TestFunctions:
    """Test module functions."""

    def test_get_standard_claude_paths(self):
        """Test getting standard Claude paths."""
        from claude_monitor.cli.main import get_standard_claude_paths

        paths = get_standard_claude_paths()
        assert isinstance(paths, list)
        assert len(paths) > 0
        assert "~/.claude/projects" in paths

    def test_discover_claude_data_paths_no_paths(self):
        """Test discover with no existing paths."""
        from claude_monitor.cli.main import discover_claude_data_paths

        with patch("pathlib.Path.exists", return_value=False):
            paths = discover_claude_data_paths()
            assert paths == []

    def test_discover_claude_data_paths_with_custom(self):
        """Test discover with custom paths."""
        from claude_monitor.cli.main import discover_claude_data_paths

        custom_paths = ["/custom/path"]
        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.is_dir", return_value=True),
        ):
            paths = discover_claude_data_paths(custom_paths)
            assert len(paths) == 1
            assert paths[0].name == "path"
