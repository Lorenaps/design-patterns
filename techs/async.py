import time
import asyncio

# Referência: https://www.youtube.com/watch?v=ftmdDlwMwwQ&ab_channel=mCoding

async def do_work(task, delay = 1.0):
    print(f'{task} started')
    await asyncio.sleep(delay)
    print(f'{task} done')

async def main():
    start = time.perf_counter()
    
    todo = ['get package', 'laundry', 'bake cake']

    # criar uma lista de tasks para executar as coroutines
    # e fazer o await em todo o bloco que se deseja esperar
    # ao invés de esperar cada iteração de um for normal
    tasks = [asyncio.create_task(do_work(item)) for item in todo]
    done, pending = await asyncio.wait(tasks)

    # forma de pegar o resultado das coroutines
    for task in done:
        result = task.result()

    end = time.perf_counter()
    print(f'it took: {end - start:.2f}s')

if __name__ == '__main__':
    asyncio.run(main())
