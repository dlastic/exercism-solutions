"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    index = 0
    seats = ["A", "B", "C", "D"]
    for _ in range(number):
        yield seats[index]
        index = 0 if index == 3 else index + 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    counter = 0
    row = 1
    seats = generate_seat_letters(number)
    for seat in seats:
        yield f"{row}{seat}"
        counter += 1
        if counter == 4:
            counter = 0
            row += 1
            if row == 13: row += 1 

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    assigned_seats = {}
    seats = generate_seats(len(passengers))
    for index, passenger in enumerate(passengers):
        assigned_seats.update({passenger: seats.__next__()})
    return assigned_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    ticket_id = ""
    for seat in seat_numbers:
        yield seat + flight_id + "".zfill(12 - len(seat + flight_id))
        
        
