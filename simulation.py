import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT_SIZE = 20
MARGIN_X, MARGIN_Y = 20, 20

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seating Chart Visualization")

# Sample data representing tables and people
tables = [
    {"name": "Table 1", "people": [("Alice", "CS"), ("Bob", "EE"), ("Carol", "ME")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 2", "people": [("David", "CE"), ("Eva", "BioMed"), ("Frank", "CS")]},
    {"name": "Table 3", "people": [("Grace", "CE"), ("Harry", "EE"), ("Irene", "BioMed"), ("Jack", "CE")]}
]

font = pygame.font.Font(None, FONT_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw tables and people as text
    x_offset, y_offset = MARGIN_X, MARGIN_Y

    for table in tables:
        table_name_surface = font.render(table["name"], True, (0, 0, 0))
        table_width, table_height = table_name_surface.get_width(), table_name_surface.get_height()

        # Check if the table fits within the window width, move to the next row if it doesn't
        if x_offset + table_width > WIDTH - MARGIN_X:
            x_offset = MARGIN_X
            y_offset += table_height + MARGIN_Y

        screen.blit(table_name_surface, (x_offset, y_offset))

        y_offset += FONT_SIZE + MARGIN_Y  # Move to the next row for people

        for person, person_type in table["people"]:
            person_surface = font.render(f"{person} ({person_type})", True, (0, 0, 0))
            screen.blit(person_surface, (x_offset, y_offset))

            y_offset += FONT_SIZE

            # If the next person exceeds the window height, move to the next column
            if y_offset > HEIGHT - MARGIN_Y:
                y_offset = MARGIN_Y
                x_offset += max(table_width, person_surface.get_width()) + MARGIN_X  # Move to the next column

        # Move to the next row for the next table
        y_offset = MARGIN_Y
        x_offset += max(table_width, person_surface.get_width()) + MARGIN_X  # Move to the next column

    # Update the display
    pygame.display.flip()

    # Add a delay to control the frame rate
    pygame.time.delay(30)
