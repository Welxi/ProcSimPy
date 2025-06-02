import pytest

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
lineMock = Line(nodeList=[preQueue, middleQueue, postQueue])
lineMock.initialize(env=env)


@pytest.mark.skip('Not Implemented')
def test_Queue() -> None:
    testQueue = Queue('TQ', 'TestQueue')
    lineMock = Line(nodeList=[testQueue])
    lineMock.initialize(Environment())
    assert testQueue.env is not None
