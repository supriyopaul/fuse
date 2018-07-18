import time
import basescript

class TestScript(basescript.BaseScript):
    def run(self):
        counter = 0

        while 1:
            self.log.info('timed_log', counter=counter)
            counter += 1
            time.sleep(1)

if __name__ == '__main__':
    TestScript().start()
