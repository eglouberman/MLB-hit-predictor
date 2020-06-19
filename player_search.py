

def player_search(first,last):
    
    from baseball_scraper import playerid_lookup
    a = playerid_lookup(last, first)
    b = a[['key_mlbam']].values
    b = int(b)
    
    return b
    