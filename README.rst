whosfaster
==========

A simple wrapper module that allows to measure performances of functions sync and async.


For sync functions,
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    @whosfaster.measure
    def example_four(num: int, num2: int) -> List:
        res = []
        for i in range(num):
            if i % num2 == 0:
                res.append(i)
        return res



For async functions,
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    @whosfaster.async_measure
    async def example_one(num: int) -> List:
        res = []
        for i in range(num):
            if i % 12 == 0:
                res.append(i)
        return res

    async def main():
        t1 = example_one(1000)
        t2 = example_one(43)
        t3 = example_one(10)

        for i in asyncio.as_completed([t1, t2, t3]):
            r = await i

    asyncio.run(main())