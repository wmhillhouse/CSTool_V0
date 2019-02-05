
# Short Text Length Fields
SHORT_TEXT_LEN = 32

# Text Field Length For Tags
TAG_TEXT_LEN = 100

# Text Field Length for Descriptions
DESC_TEXT_LEN = 200

# Text Field Length for Documents
DOC_TEXT_LEN = 100

# Choices for Object Type
OBJ_TYPE = (
    ('DI', 'Digital Input'),
    ('DO', 'Digital Output'),
    ('AI', 'Analog Input'),
    ('AO', 'Analog Output'),
    ('DI_COMM', 'Digital Input via Communications'),
    ('DO_COMM', 'Digital Output via Communications'),
    ('AI_COMM', 'Analog Input via Communications'),
    ('AO_COMM', 'Analog Output via Communications'),
    ('EVENT', 'Event'),
    ('INTERLOCK', 'Interlock'),
    ('DRiVE', 'Drive'),
    ('VALVE', 'Valve'),
    ('CABINET', 'Cabinet'),
)

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

ANALOG_IO_TYPE = {
    ('AI', 'Analog Input'),
    ('AO', 'Analog Output')
}

EVENT_TYPES = (
    ('CUSTOM', 'Custom'),
    ('FLT', 'Fault'),
    ('ON', 'On'),
    ('OFF', 'Off'),
    ('HH', 'High High'),
    ('H', 'High'),
    ('L', 'Low'),
    ('LL', 'Low Low'),
    ('FAIL_TO_START', 'Fail to Start'),
    ('FAIL_TO_STOP', 'Fail to Stop'),
    ('FAIL_TO_OPEN', 'Fail to Open'),
    ('FAIL_TO_CLOSE', 'Fail to Close'),
    ('FBK_FAIL', 'Feedback Fail'),
    ('COM_FAIL', 'Communications Fail'),
)
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