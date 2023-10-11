from datetime import datetime
import random
from time import sleep


class TemperatureLogger:
    def __init__(self, filename: str):
        self.filename = filename
    
    def callback(self, temperature: float):
        if temperature>=50:
            with open(self.filename, 'a') as f:
                f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' - TEMP REACHED: ' + str(temperature) + '\n')


def test_without_ros():
    tl = TemperatureLogger('log.txt')
    for i in range(20):
        temp = random.uniform(10, 70)
        tl.callback(temp)
        print('temp: ' + str(temp))
        sleep(random.uniform(0.2, 2.2))


if __name__ == '__main__':
    test_without_ros()
