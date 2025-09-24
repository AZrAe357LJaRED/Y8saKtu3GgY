# 代码生成时间: 2025-09-24 15:16:20
import asyncio
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.asyncio import AsyncIOExecutor


class ScheduledTaskScheduler:
    def __init__(self, app: Starlette):
        """
        Initializes the scheduled task scheduler with a Starlette application.
        """
        self.scheduler = AsyncIOScheduler(
            jobstores={
                'default': MemoryJobStore()
            },
            executors={
                'default': AsyncIOExecutor()
            },
            listener=self.on_scheduler_event
        )
        self.app = app

        self.app.add_route('/start_scheduler', self.start_scheduler)
        self.app.add_route('/stop_scheduler', self.stop_scheduler)

    def on_scheduler_event(self, event):
        """
        Listener for the scheduler event.
        """
        if event.exception:
            print(f'Error occurred in job: {event.exception}')

    async def add_job(self, func, trigger, *args, **kwargs):
        """
        Adds a job to the scheduler.
        "