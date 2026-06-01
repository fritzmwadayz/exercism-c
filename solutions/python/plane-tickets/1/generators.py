"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    seat_letters = ['A', 'B', 'C', 'D']
    index = 0

    seats_count = 0

    while seats_count < number:
        current_seat = seat_letters[index]
        yield(current_seat)
        seats_count += 1
        index += 1

        if index > 3:
            index = 0


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    seat_letters = ['A', 'B', 'C', 'D']
    index = 0
    seats_count = 0
    row = 1

    while seats_count < number:
        current_seat = seat_letters[index]
        yield(f'{row}{current_seat}')
        seats_count += 1
        index += 1

        if seats_count%4 == 0:
            row += 1

        if row == 13:
            row +=1

        if index > 3:
            index = 0


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    assigned = {}

    seat = generate_seats(len(passengers))

    for passenger in passengers:
        assigned[passenger] = seat.__next__()

    return assigned
    
def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        ticket_code = seat_number+flight_id
        remainders = 12-len(ticket_code)
        ticket_code += ('0'*remainders)

        yield(ticket_code)
