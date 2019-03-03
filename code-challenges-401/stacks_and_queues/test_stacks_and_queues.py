def test_stack_push():
    plate_stack = Stack()

    plate_stack.push('plate_1')

    assert plate_stack.head.value == 'plate_1'