from neo4j import GraphDatabase, Result
from pympler import muppy, summary, tracker


def print_current_memory_usage():
    all_objects = muppy.get_objects()
    sum_objects = summary.summarize(all_objects)
    summary.print_(sum_objects)


def do_transaction(tx):
    result: Result = tx.run("MATCH (p:Props) RETURN p LIMIT 100000")
    # tr = tracker.SummaryTracker()
    i = 0
    for x in result:
        i += 1
        del x
        if i % 1000 == 0:
            print_current_memory_usage()
            # tr.print_diff()

    # return i


with GraphDatabase.driver(
    "bolt://localhost:3020", auth=("neo4j", "password")
) as driver:
    with driver.session() as session:
        i = session.execute_read(do_transaction)
        print(i)
