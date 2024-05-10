from typing import Type, Any

from pydantic import SecretStr
from pydantic.fields import FieldInfo
from pydantic_settings import BaseSettings, EnvSettingsSource, PydanticBaseSettingsSource


class AdminsParse(EnvSettingsSource):
    def prepare_field_value(
            self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool
    ) -> Any:
        if field_name == 'ADMINS_ID':
            return [int(x) for x in value.split(',')]
        return super().prepare_field_value(field_name, field, value, value_is_complex)


class BotSettings(BaseSettings):
    # Bot
    BOT_TOKEN: SecretStr
    ADMINS_ID: list[int]
    WEB_APP_URL: str


    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: Type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (AdminsParse(settings_cls), )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = BotSettings()
