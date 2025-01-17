# Copyright (C) 2019 The Raphielscape Company LLC.; Licensed under the Raphielscape Public License, Version 1.d (the "License"); you may not use this file except in compliance with the License.; Port by @moveangel

""" a module for gathering covid patients info. """

from covid import Covid

from userbot import CMD_HELP, trgg
from userbot.events import register


@register(outgoing=True, pattern="^\{trg}covid (.*)".format(trg=trgg))
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
        output_text = (
            f"`Confirmed   : {format_integer(country_data['confirmed'])}`\n"
            + f"`Active      : {format_integer(country_data['active'])}`\n"
            + f"`Deaths      : {format_integer(country_data['deaths'])}`\n"
            + f"`Recovered   : {format_integer(country_data['recovered'])}`\n\n"
            + f"`New Cases   : {format_integer(country_data['new_cases'])}`\n"
            + f"`New Deaths  : {format_integer(country_data['new_deaths'])}`\n"
            + f"`Critical    : {format_integer(country_data['critical'])}`\n"
            + f"`Total Tests : {format_integer(country_data['total_tests'])}`\n\n"
            + f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
        )
        await event.edit(f"Corona Virus Info in {country}:\n\n{output_text}")
    except ValueError:
        await event.edit(
            f"No information found for: {country}!\nCheck your spelling and try again."
        )


def format_integer(number, thousand_separator="."):
    def reverse(string):
        string = "".join(reversed(string))
        return string

    s = reverse(str(number))
    count = 0
    result = ""
    for char in s:
        count = count + 1
        if count % 3 == 0:
            if len(s) == count:
                result = char + result
            else:
                result = thousand_separator + char + result
        else:
            result = char + result
    return result


CMD_HELP.update(
    {
        "covid": ".covid <country>"
        "\nUsage: Get an information about data covid-19 in your country.\n"
    }
)
