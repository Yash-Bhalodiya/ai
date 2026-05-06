# Job Scheduling Problem

def job_scheduling(jobs):

    # Sort jobs according to profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [-1] * (max_deadline + 1)

    total_profit = 0

    for job in jobs:

        job_id, deadline, profit = job

        for i in range(deadline, 0, -1):

            if slots[i] == -1:
                slots[i] = job_id
                total_profit += profit
                break

    print("Scheduled Jobs:")

    for i in range(1, len(slots)):
        if slots[i] != -1:
            print(slots[i], end=" ")

    print("\nTotal Profit:", total_profit)


jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

job_scheduling(jobs)