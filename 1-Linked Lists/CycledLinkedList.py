def hasCycle(self, head: Optional[ListNode]) -> bool:
    current = runner = head
    if current is None:
        return False
    while runner.next and runner.next.next:
        current = current.next
        runner = runner.next.next
        if runner == current:
            return True
    return False