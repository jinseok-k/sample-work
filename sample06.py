from prefect import flow, task

@task(log_prints=True)
def check_value(name: str):
    print(f"Hello World!!, {name}!")

@flow
def hello_check(names: list[str]):
    for name in names:
        check_value(name)

if __name__ == "__main__":
    hello_check(['Marvin', 'Trillian', 'Ford'])
