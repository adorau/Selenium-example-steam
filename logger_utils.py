from singleton import Singleton
import logging

class LoggerUtils(metaclass=Singleton):
    def __init__(self):
        self.prec_count = 1
        self.test_step_count = 1
        self.clean_up_count = 1
        self.logger = logging.getLogger(__name__)

    def log_precondition(self, text=""):
        if self.prec_count == 1:
            self.logger.info("============PRECONDITIONS=============")
        self.logger.info(f"Precondition {self.prec_count}: {text}")
        self.prec_count += 1

    def log_test_step(self, text=""):
        if self.test_step_count == 1:
            self.logger.info("============TEST_STEPS================")
        self.logger.info(f"Test step {self.test_step_count}: {text}")
        self.test_step_count += 1

    def log_clean_up(self, text=""):
        if self.test_step_count == 1:
            self.logger.info("=============CLEAN_UP=================")
        self.logger.info(f"Clean up {self.clean_up_count}: {text}")
        self.clean_up_count += 1

    @staticmethod
    def log_info_message(text=""):
        LoggerUtils().logger.info(text)

    @staticmethod
    def log_debug_message(text=""):
        LoggerUtils().logger.debug(text)

    @staticmethod
    def log_warning_message(text=""):
        LoggerUtils().logger.warning(text)

    @staticmethod
    def log_error_message(text=""):
        LoggerUtils().logger.error(text)

    @staticmethod
    def log_critical_message(text=""):
        LoggerUtils().logger.critical(text)