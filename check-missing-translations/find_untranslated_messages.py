#!/usr/bin/env python
#
# /// script
# dependencies = [
#     "click~=8.3.0",
# ]
# ///
import json
from pathlib import Path

import click


@click.command()
@click.option(
    "--messages",
    default="i18n/messages",
    help="Path (absolute or relative to the working directory) containing the messages.",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
)
@click.option("--locales", default="nl", help="Comma-separated list of locales")
def main(messages: Path, locales: str):
    any_missing = False
    locales_to_check = (locale.strip() for locale in locales.split(","))
    for locale in locales_to_check:
        click.echo(f"Checking locale: {locale}")
        with (messages / f"{locale}.json").open() as message_catalog:
            translations = json.load(message_catalog)

        for unique_id, trans_object in translations.items():
            # skip translated messages
            if trans_object["defaultMessage"] != trans_object["originalDefault"]:
                continue
            if trans_object.get("isTranslated", False):
                continue

            any_missing = True
            click.secho(
                f"ID '{unique_id}' appears untranslated, defaultMessage: "
                f"{trans_object['originalDefault']}",
                fg="red",
            )

    if any_missing:
        exit(1)
    else:
        click.secho("All good!", fg="green")


if __name__ == "__main__":
    main()
