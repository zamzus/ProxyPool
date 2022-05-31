import multiprocessing
import time
from loguru import logger
# from proxypool.processors.server import app
from proxypool.processors.getter import Getter
from proxypool.processors.tester import Tester
from proxypool.settings import CYCLE_GETTER, CYCLE_TESTER, ENABLE_GETTER, ENABLE_TESTER, IS_WINDOWS
# from proxypool.setting import APP_PROD_METHOD_GEVENT, APP_PROD_METHOD_MEINHELD, APP_PROD_METHOD_TORNADO,
#     CYCLE_GETTER, CYCLE_TESTER, API_HOST, \
#     API_THREADED, API_PORT, ENABLE_SERVER, IS_PROD, APP_PROD_METHOD, \
#     ENABLE_GETTER, ENABLE_TESTER, IS_WINDOWS


if IS_WINDOWS:
    multiprocessing.freeze_support()

tester_process, getter_process, server_process = None, None, None


class Scheduler:
    @staticmethod
    def run_getter(cycle=CYCLE_GETTER):
        if not ENABLE_GETTER:
            logger.info('getter not enabled, exit')
            return
        getter = Getter()
        loop = 0
        while True:
            logger.debug(f'getter loop {loop} start...')
            getter.run()
            loop += 1
            time.sleep(cycle)

    @staticmethod
    def run_tester(cycle=CYCLE_TESTER):
        if not ENABLE_TESTER:
            logger.info('tester not enabled, exit')
            return
        tester = Tester()
        loop = 0
        while True:
            logger.debug(f'tester loop {loop} start...')
            tester.run()
            loop += 1
            time.sleep(cycle)

    def run(self):
        global tester_process, getter_process, server_process
        try:
            logger.info('starting proxypool...')
            if ENABLE_TESTER:
                tester_process = multiprocessing.Process(target=self.run_tester)
                logger.info(f'starting tester, pid {tester_process.pid}...')
                tester_process.start()

            if ENABLE_GETTER:
                getter_process = multiprocessing.Process(target=self.run_getter)
                logger.info(f'starting getter, pid {getter_process.pid}...')
                getter_process.start()

            tester_process.join()
            getter_process.join()
        except KeyboardInterrupt:
            logger.info('received keyboard interrupt signal')
            tester_process.terminate()
            getter_process.terminate()
        finally:
            # must call join method before calling is_alive
            tester_process.join()
            getter_process.join()
            logger.info(f'tester is {"alive" if tester_process.is_alive() else "dead"}')
            logger.info(f'getter is {"alive" if getter_process.is_alive() else "dead"}')
            logger.info('proxy terminated')


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()
