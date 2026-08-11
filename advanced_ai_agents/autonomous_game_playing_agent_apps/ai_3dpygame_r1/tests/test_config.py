import tempfile
import unittest
import sys
from pathlib import Path
from unittest.mock import patch

PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from config import load_api_settings


class LoadApiSettingsTest(unittest.TestCase):
    def test_loads_openai_proxy_settings_from_env_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            env_path = Path(tmpdir) / ".env"
            env_path.write_text(
                "DEEPSEEK_API_KEY=deepseek-test-key\n"
                "OPENAI_API_KEY=proxy-test-key\n"
                "OPENAI_BASE_URL=https://proxy.example.com/v1\n",
                encoding="utf-8",
            )

            with patch.dict("os.environ", {}, clear=True):
                settings = load_api_settings(env_path)

        self.assertEqual(settings.deepseek_api_key, "deepseek-test-key")
        self.assertEqual(settings.openai_api_key, "proxy-test-key")
        self.assertEqual(settings.openai_base_url, "https://proxy.example.com/v1")


if __name__ == "__main__":
    unittest.main()
