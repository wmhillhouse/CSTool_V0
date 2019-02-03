
# Short Text Length Fields
SHORT_TEXT_LEN = 32

# Text Field Length For Tags
TAG_TEXT_LEN = 100

# Text Field Length for Descriptions
DESC_TEXT_LEN = 200

# Text Field Length for Documents
DOC_TEXT_LEN = 100

# Choices for Control Object Type
CTRL_OBJ_TYPE = (
    ('DI', 'Digital Input'),
    ('DO', 'Digital Output'),
    ('AI', 'Analog Input'),
    ('AO', 'Analog Output'),
    ('DRiVE', 'Drive'),
    ('VALVE', 'Valve'),
)

DIGITAL_IO_TYPE = {
    ('DI', 'Digital Input'),
    ('DO', 'Digital Output'),
}

ALARM_TYPES = (
    ('D', 'Digital'),
    ('HH', 'High High'),
    ('H', 'High'),
    ('L', 'Low'),
    ('LL', 'Low Low')
)

ALARM_PRIORITIES = (
    (1, 'Critical'),
    (2, 'High'),
    (3, 'Medium'),
    (4, 'Low')
)