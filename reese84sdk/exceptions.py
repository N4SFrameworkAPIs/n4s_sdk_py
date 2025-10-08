class Reese84Error(Exception):
    """Eccezione di base per errori di Reese84Client."""
    pass

class Reese84ConnectionError(Reese84Error):
    """Eccezione per errori di connessione o rete."""
    pass

class Reese84APIError(Reese84Error):
    """Eccezione per errori restituiti dall'API."""
    pass