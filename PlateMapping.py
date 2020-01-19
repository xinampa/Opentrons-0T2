from opentrons import protocol_api

metadata = {'apiLevel': '2.0'}


# tiptracks might need custom tip to increase quantity of fluid

def run(protocol: protocol_api.ProtocolContext):
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', 4)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1, tiprack_2])

    # these uL values were created randomly for this example

    # connect sql server with API Call

    water_volumes = [
        1,  2,  3,  4,  5,  6,  7,  8,
        9,  10, 11, 12, 13, 14, 15, 16,
    ]

    p300.distribute(water_volumes, reservoir['A12'], plate.wells())