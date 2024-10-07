import asyncio
import logging

from create_bot import main


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


