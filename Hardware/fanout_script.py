import pcbnew
board = pcbnew.GetBoard()

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

def do_fanning_out(reference):
    tgt = board.FindFootprintByReference(reference)
    pads = tgt.Pads()

    center_x = tgt.GetX()
    center_y = tgt.GetY()

    for pad in pads:
        pad_x = pad.GetX()
        pad_y = pad.GetY()

        if(pad_x > center_x): via_x = pad_x + 400000
        else: via_x = pad_x - 400000

        if(pad_y > center_y): via_y = pad_y + 400000
        else: via_y = pad_y - 400000

        via_location = pcbnew.VECTOR2I(via_x,via_y)
        add_via(via_location)
        add_track(pad.GetPosition(),via_location)
    pcbnew.Refresh()

