"""FastAPI application for the knowledge-base assistant."""

from fastapi import FastAPI

from kb_assistant import __version__
from kb_assistant.config import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create the FastAPI application."""
    app_settings = settings or get_settings()
    application = FastAPI(title="KB Assistant", version=__version__)

    @application.get("/health")
    def health() -> dict[str, str]:
        """Report service liveness and environment."""
        return {
            "status": "ok",
            "env": app_settings.app_env,
            "version": __version__,
        }

    return application


app = create_app()
