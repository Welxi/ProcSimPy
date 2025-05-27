from procsimpy.Line import Line
from procsimpy.Queue import Queue
from simpy import Environment

preQueue = Queue('Q1', 'PreQueue')
middleQueue = Queue('Q2', 'MiddleQueue')
postQueue = Queue('Q3', 'PostQueue')

preQueue.defineRouting(successorList=[middleQueue])
middleQueue.defineRouting(predecessorList=[preQueue], successorList=[postQueue])
postQueue.defineRouting(predecessorList=[middleQueue])

env = Environment()
objectList = [preQueue, middleQueue, postQueue]
lineMock = Line(objectList=objectList)
lineMock.initialize(env=env)


def test_Queue() -> None:
    testQueue = Queue('TQ', 'TestQueue')
    lineMock = Line([testQueue])
    lineMock.initialize(Environment())
    assert testQueue.env is not None
