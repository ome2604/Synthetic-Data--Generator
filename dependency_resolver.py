from collections import deque


def topological_sort(graph):

    all_tables = set()

    for table, deps in graph.items():

        all_tables.add(table)

        for dep in deps:
            all_tables.add(dep)

    in_degree = {
        table: 0
        for table in all_tables
    }

    for table, deps in graph.items():

        for dep in deps:

            if dep != table:
                in_degree[table] += 1

    queue = deque(
        [
            table
            for table in all_tables
            if in_degree[table] == 0
        ]
    )

    order = []

    while queue:

        current = queue.popleft()

        order.append(current)

        for child, deps in graph.items():

            if current in deps:

                in_degree[child] -= 1

                if in_degree[child] == 0:

                    queue.append(child)

    return order