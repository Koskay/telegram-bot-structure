from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types.base import TelegramObject

from apscheduler.schedulers.asyncio import AsyncIOScheduler


class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler):
        self.scheduler = scheduler

    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]
                       ) -> Any:
        data['apscheduler'] = self.scheduler
        return await handler(event, data)
