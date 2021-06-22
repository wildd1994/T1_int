import asyncio
import random

warehouse = []
max_elements = 10


def is_overflow():
    return len(warehouse) >= max_elements


def is_underflow():
    return len(warehouse) == 0


def add_element(element):
    warehouse.append(element)


def delete_element():
    return warehouse.pop(0)


async def producer():
    while True:
        x = random.randint(a=1, b=10000)
        if not is_overflow():
            add_element(x)
            print(f'Элемент {x} добавлен на склад')
        else:
            print('Склад заполнен')
        await asyncio.sleep(random.randint(a=1, b=10))


async def consumer():
    while True:
        if not is_underflow():
            x = delete_element()
            print(f'Элемент {x} взят со склада')
        else:
            print('Склад пуст')
        await asyncio.sleep(random.randint(a=1, b=10))


async def main():
    # task1 = asyncio.create_task(producer())
    # task2 = asyncio.create_task(consumer())
    #
    # await asyncio.gather(task1, task2)
    tasks = []
    for i in range(10):
        task = asyncio.create_task(producer())
        tasks.append(task)
    for i in range(2):
        task = asyncio.create_task(consumer())
        tasks.append(task)

    await asyncio.gather(*tasks)
if __name__ == '__main__':
    asyncio.run(main())
