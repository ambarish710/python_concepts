

def exclusiveTime(self, n, logs):
    """
    :type n: int
    :type logs: List[str]
    :rtype: List[int]
    """
    res = [0] * n
    stack = []
    prevTime = 0
    for log in logs:
        idx, type, time = log.split(':')
        if type == 'start':
            if stack:
                res[stack[-1]] += int(time) - prevTime
            stack.append(int(idx))
            prevTime = int(time)
        else:
            res[stack[-1]] += int(time) - prevTime + 1
            stack.pop()
            prevTime = int(time) + 1
    return res




# keep just the id on stack
# check index type for every iteration
# And also maintain

def exclusiveTime(n, logs):
    if not logs:
        return []

    ret_list = [0]*n
    stack = []
    previous_time = 0

    for log in logs:
        idx, type, time = logs.split(":")
        if type == "start":
            if stack:
                ret_list[stack[-1]] += int(time) - previous_time
            stack.append(idx)
            previous_time = int(time)
        else:
            ret_list[stack[-1]] += int(time) - previous_time + 1
            stack.pop()
            previous_time = int(time) + 1
    return ret_list