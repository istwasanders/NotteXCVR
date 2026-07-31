import pcbnew
board = pcbnew.GetBoard()

# The FPGA is U2.  It might be useful later to make this a parameter
tgt = board.FindFootprintByReference("U2")
pads = tgt.Pads()

# U2 has pads spaced 0.8mm apart, place the vias offset 0.4mm from the pads
via_offset = pcbnew.VECTOR2I(400000,400000)

# Makes 0.2mm width track from pad to via
def add_track(start,end):
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(start)
    track.SetEnd(end)
    track.SetWidth(int(0.2 * 1e6))
    track.SetLayer(pcbnew.F_Cu)
    board.Add(track)

# Makes 18mil via with 8mil hole
def add_via(position):
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(position)
    via.SetDrill(int(0.2032 * 1e6))
    via.SetWidth(int(0.4572 * 1e6))
    board.Add(via)
for pad in pads:
    via_location = pad.GetPosition() + via_offset
    add_via(via_location)
    add_track(pad.GetPosition(),via_location)
pcbnew.Refresh()

