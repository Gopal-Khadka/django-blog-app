import tempfile
import os
import logging
from io import StringIO
from django.test import TestCase
from pathlib import Path


class LoggingTestCase(TestCase):

    def setUp(self):
        # Create a temporary file in the current working directory
        self.temp_dir = os.path.join(
            Path(__file__).resolve().parent, "test_logs"
        )  # Use the current working directory
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)

        self.log_file = tempfile.NamedTemporaryFile(
            dir=self.temp_dir, delete=True, suffix=".log"
        )
        self.log_file_path = self.log_file.name
        self.log_file.close()  # Close the file to avoid locking issues

        # Setup the logger
        self.logger = logging.getLogger("django")
        self.file_handler = logging.FileHandler(self.log_file_path)
        self.file_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.file_handler)

    def tearDown(self):
        # Remove handlers to close files
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)

    def test_logging_console(self):
        log_output = StringIO()
        console_handler = logging.StreamHandler(log_output)
        self.logger.addHandler(console_handler)

        self.logger.debug("This is a debug message for the console.")
        self.logger.error("This is an error message for the console.")

        log_output.seek(0)
        log_contents = log_output.getvalue()

        self.assertIn("This is a debug message for the console.", log_contents)
        self.assertIn("This is an error message for the console.", log_contents)

        # Cleanup
        self.logger.removeHandler(console_handler)

    def test_logging_file(self):
        import time

        self.logger.debug("This is a debug message for the file.")
        self.logger.error("This is an error message for the file.")

        # Wait to ensure the log is written
        time.sleep(1)

        with open(self.log_file_path, "r") as file:
            log_contents = file.read()

        self.assertIn("This is a debug message for the file.", log_contents)
        self.assertIn("This is an error message for the file.", log_contents)
