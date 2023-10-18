from cx_Freeze import setup, Executable

setup(
    name="TicketSwipe",
    version="2.4",
    description="TicketSwap more like TicketSwipe, Snipe tickets using TicketSwipe so you dont have to tryhard to get a ticket.",
    executables=[Executable("TSpremium.py")]
)
