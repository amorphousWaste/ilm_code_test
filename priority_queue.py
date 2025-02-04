"""ILM Interview Code Test

Implement a simple priority queue.
Assume an incoming stream of dictionaries containing two keys;
command to be executed and priority. Priority is an integer value [0, 10],
where work items of the same priority are processed in the order they are received.
"""

from queue import PriorityQueue
from typing import Callable


class ILMPriorityQueue(PriorityQueue):
    """Custom Process Queue."""

    def add_to_queue(self, priority: int, command: Callable) -> None:
        """Custom function to add commands to the queue at the given priority.

        Args:
            priority (int): Priority value.
            command (Callable): Command to be executed.
        """
        self.put((priority, command))

    def process(self) -> object:
        """Process a single item in the queue.

        Returns:
            (object): The result of the processed command.
        """
        item: tuple = self.get()
        return item[1](item[0])

    def process_all(self) -> object:
        """Process all items in the queue.

        Returns:
            (object): The result of the processed command.
        """
        while not self.empty():
            self.process()
