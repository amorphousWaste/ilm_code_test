"""ILM Interview Code Test

Implement a simple priority queue.
Assume an incoming stream of dictionaries containing two keys;
command to be executed and priority. Priority is an integer value [0, 10],
where work items of the same priority are processed in the order they are received.
"""

from random import randint

from priority_queue import ILMPriorityQueue

QUEUE: ILMPriorityQueue = ILMPriorityQueue()


def command_to_run(value: int) -> int:
    """Simple command to run from the process queue.

    Args:
        value (int): A number, most likely the priority.

    Returns:
        value (int): The given value.
    """
    print(value)


def add_data_stream_to_queue(data_stream: list[dict]) -> None:
    """Take in a data stream of dictionaries and add them to the queue.

    Args:
        data_stream (list[dict]): Dictionary of data in the form of:
            {'priority': int, 'command': function}
    """
    for item in data_stream:
        QUEUE.add_to_queue(item['priority'], item['command'])


def demo() -> None:
    """Demo function."""
    data_stream: list = []
    for i in range(10):
        r: int = randint(0, 10)
        data_stream.append({'priority': r, 'command': command_to_run})

    add_data_stream_to_queue(data_stream)
    QUEUE.process_all()


if __name__ == '__main__':
    demo()
