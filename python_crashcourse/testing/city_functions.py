def city_country(city, country, population=0):
    '''Returns a nicely formatted City-Country layout.'''
    if population:
        state_name = f"{city}, {country}"
        return state_name.title() + f" - population {population}"
    else:
        state_name = f"{city}, {country}"
    return state_name.title()