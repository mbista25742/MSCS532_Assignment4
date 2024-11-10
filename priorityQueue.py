class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Lower priority value means higher priority in a min-heap
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"

class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        """Inserts a new task and maintains the min-heap property."""
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Removes and returns the task with the lowest priority."""
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, simply remove and return it
        min_task = self.heap[0]
        # Move the last element to the root and reheapify
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_task

    def increase_key(self, task, new_priority):
        """Increases the priority of a task (lower priority value) and adjusts its position."""
        index = self.heap.index(task)
        if index < 0 or new_priority >= self.heap[index].priority:
            print("Error: New priority is not higher than the current priority.")
            return
        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def decrease_key(self, task, new_priority):
        """Decreases the priority of a task (higher priority value) and adjusts its position."""
        index = self.heap.index(task)
        if index < 0 or new_priority <= self.heap[index].priority:
            print("Error: New priority is not lower than the current priority.")
            return
        self.heap[index].priority = new_priority
        self._heapify_down(index)

    def _heapify_up(self, index):
        """Restores the heap property by moving an element up."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """Restores the heap property by moving an element down."""
        child = 2 * index + 1
        while child < len(self.heap):
            right = child + 1
            if right < len(self.heap) and self.heap[right] < self.heap[child]:
                child = right
            if not (self.heap[index] < self.heap[child]):
                break
            self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
            index = child
            child = 2 * index + 1

# Initialize the priority queue (min-heap)
priority_queue = MinHeap()

# Create and insert tasks
priority_queue.insert(Task(task_id=1, priority=10, arrival_time=0, deadline=5))
priority_queue.insert(Task(task_id=2, priority=5, arrival_time=1, deadline=6))
priority_queue.insert(Task(task_id=3, priority=15, arrival_time=2, deadline=7))

# Check if the queue is empty
print("Priority Queue is empty:", priority_queue.is_empty())

# Extract tasks by priority
print("Extracted Task:", priority_queue.extract_min())
print("Extracted Task:", priority_queue.extract_min())

# Modify the priority of a task
task = Task(task_id=4, priority=20, arrival_time=3, deadline=8)
priority_queue.insert(task)

# Test increase_key with invalid new priority
priority_queue.increase_key(task, 25)  # Should print an error

# Test decrease_key with valid new priority
priority_queue.decrease_key(task, 3)

# Extract remaining tasks
while not priority_queue.is_empty():
    print("Extracted Task:", priority_queue.extract_min())
