#!/usr/bin/python3
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel
import random
import sys
import argparse

console = Console()

callsign = "W5ALC"
name = "Jon"
location = "Pueblo, CO"

default_shl_announcements = [
    "No new Announcements at this time."
]

def get_announcements_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] File '{file_path}' not found.")
        sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description='The Skyhublink Monday night net script')
    parser.add_argument('-t', '--topic', help='File containing net topics (General net topics included no flag)')
    parser.add_argument('-s', '--shl', help='SkyHubLink announcements file')
    return parser.parse_args()

def display_topic(topics):
    if not topics:
        console.print(f"[bold red]Error:[/bold red] No topics available.")
        sys.exit(1)

    selected_topic = random.choice(topics)
    console.print(f"\n[bold green]Selected net question:[/bold green] [bold cyan]{selected_topic}[/bold cyan]")
    
    return selected_topic

def get_shl_announcements(file_path):
    if file_path:
        return get_announcements_from_file(file_path)
    else:
        return default_shl_announcements

def print_section(section):
    panel = Panel(
        Text(section, style="bold cyan"),
        title="[bold magenta]Skyhublink Monday Night Net[/bold magenta]",
        border_style="bold yellow",
        expand=False,
        padding=(1, 2)
    )
    console.print(panel)

def next_section():
    args = parse_arguments()
    
    # Use provided files or defaults
    topics_file = args.topic
    shl_file = args.shl
    
    topics = get_announcements_from_file(topics_file) if topics_file else [
        "Could you tell us about your favorite antenna configuration and why you prefer it?",
        "Have you made any interesting DX contacts recently? Please share your experience.",
        "How have the propagation conditions been in your area? Have you encountered any challenges or successes lately?",
        "Are you working on any new homebrew projects or modifications that you'd like to share with us?",
        "For those who enjoy portable operations, what is your go-to setup when operating in the field?",
        "What has been the most challenging thing you've learned in ham radio, and how did you overcome it?",
        "Do you operate any digital modes? What are your thoughts on the future of digital in amateur radio?",
        "How have you incorporated amateur radio into your emergency preparedness plans?",
        "What is your favorite transceiver, and what makes it stand out to you?",
        "Do you have any tips for setting up effective antennas in small or restricted spaces?",
        "What kind of power supply setups do you use, especially for portable or emergency operations?",
        "If you could have a QSO with anyone, living or passed, who would it be and why?",
        "What’s the most memorable QSO or event you’ve experienced in amateur radio?",
        "Where do you see amateur radio evolving in the next 10-20 years?",
        "How have you used amateur radio to contribute to your community?",
        "In your opinion, what has been the biggest technological leap in amateur radio since you started?"
    ]

    net_question = display_topic(topics)
    shl_announcements = get_shl_announcements(shl_file)

    net_script = [
        f"START OF NET:\nGood evening everyone on the Skyhublink, it is 7pm in the Rocky Mountains. This is {callsign}, {name}, located in {location}. Welcome to the 'SKYHUBLINK' System Wide Monday Night Net. This NET mets every Monday Night to discuss amateur radio and other interesting topics. We are here to have fun on the radio through our communications and help to make the use of many fine repeaters that otherwise might be very underutilized and quiet. That also lets others hear that the repeaters are on the air, and that they are active! SKYHUBLINK is NOT a closed system in any way. We welcome all users in the true spirit of amateur radio. All amateurs, NEW and OLD, this is the place for you!",
        "PLEASE, remember during all use of this multi-mode and MULTI REPEATER LINKING SYSTEM, allow 3-5 seconds between transmissions, 1.5 seconds for keyup and then begin speaking. ALSO, keep the PTT pushed a half second or so after your last word. That allows your last word not to be cut off. When more than 2 people are using the repeaters, please set up a 'rotation' so that you won’t be doubling over the other parties in a 'round table' discussion. It is VERY IMPORTANT to remember you are on many repeaters simultaneously. Good amateur operating practice is remembering to allow all who might want to join in an opportunity to do so, just like using a single stand-alone repeater. Long ragchews are welcome on SkyHubLink, but remember, most of the repeaters have a 3-minute timeout, keep that in mind as you talk to a friend.",
        "(BREAK FOR REPEATER RESET)",
        "And it is very important every so often in your longer QSO’s, to check and see if someone is trying to break into the system or needs one of the other repeaters in an emergency. Or maybe there might simply be someone who is needing to call another station on another repeater during your ongoing QSO. Someone may need to use a repeater you are on thru the system in another area, so always keep that in mind.",
        "You can also check out SkyHubLink.com and click on the 'Status' tab to see all the AllStar and main Hub Links and activity. You can go to the 'Click HERE for YSF-Reflector Status (Opens in NEW TAB)' link to see all YSF links and where others may be coming in digitally, including Wires-X, D-Star, and the other modes. We are on Hamshack Hotline Voice over IP system.",
        "IF you are using a HOTSPOT on SKYHUBLINK please do NOT enable the Wires-X pass-through on your Pi-Star software. Changing YSF Reflectors thru your radio will cause disconnections of SkyHubLink Reflector 92722 and other issues thru the system. ALSO, we do not allow use of DTMF tones during NETS on SkyHubLink.",
        "When monitoring the repeater system, we ask that you DO NOT 'KERCHUNCK' the system or repeater to test to see if you are keying up the system. PLEASE DO come on and ask for a radio check. KERCHUNCKING the system can cause link issues. Once again, to see if you are making the 'repeater' actually come on and ask for a radio check. Most of the time you will get an answer from someone. AND, if YOU hear anyone ask for a radio check and no one responds fairly quickly, then you come on and advise the asking station that they are making the system and can be heard, or give a proper signal report.",
        "(BREAK FOR REPEATER RESET)",
        "You can also utilize the SkyHubLink.com/status page to see if your radio is keying into the system. There are many analytic capabilities of the website that can help you determine if your radio is getting into the system.",
        "This is a directed NET. All check-ins must gp through net control. We will take a few check-ins then do a roundtable of that list, then take another check-in list. We take check-ins by Modes.",
        "IF you are listening on the internet stream, please text Jack with your name and location and callsign at 555-555-5555.",
        "PLEASE LISTEN CAREFULLY TO THESE CHECK-IN INSTRUCTIONS:\nWHEN CHECKING IN SAY ONLY YOUR CALLSIGN PHONETICALLY TWICE. Please to facilitate the system keying up allow a key up time of 1.5 seconds, and hold the PTT a half second or so at the last syllable so that you don’t get cut off. If Net control misses you then please stand by for the next round of check-ins.",
        "\nSKYHUBLINK Announcements, Net Lineup, etc:\n\n" + "\n".join(shl_announcements),
        f"TONIGHT'S NET QUESTION: {net_question}",
        "SHORTTIMERS CHECK IN FIRST.",
        "No-Traffic Check-ins\n\nMake sure to acknowledge check-ins",
        "Repeater Owners and System Operators\n\nMake sure to acknowledge check-ins",
        "Digital Check-ins\n\nMake sure to acknowledge check-ins",
        "Analog Check-ins\n\nMake sure to acknowledge check-ins",
        "When all have been called:",
        "Did we miss anyone?",
        "Last call:",
        "This has been the the “SKYHUBLINK” Monday Night Net,  Thanks again to Skyler, WØSKY Chief Engineer, and Jeremy WØJRL System Engineer for the ALLSTAR hub connections, and the Rocky Mountain Radio League, and to the Denver Water Amateur Radio Club, The Denver Radio League,  The N2KNK western slope repeater system, Randall AE7RJ, and all other systems and operators on the SkyHubLink.  Thanks also to Kathleen W0KPH for spotting and logging. IF you would like to be on our email list, be sure to go to SkyHubLink.com, and then click on the “Join/Connect” tab for instructions."
        f"So with that, this is {callsign}, {name} from {location} wrapping up tonights net and returning all systems to normal amateur use.  73’ and have a great night, we will look for you next week!"
        "\n(After net, please email check-in list to ke0vh@outlook.com , and thanks!)"
    ]

    for section in net_script:
        print_section(section)
        user_input = Prompt.ask("[bold yellow]Press Enter to continue to the next section or 'q' to quit:[/bold yellow]", default="")
        if user_input.lower() == 'q':
            console.print("[bold magenta]Exiting script.[/bold magenta]")
            break

if __name__ == "__main__":
    next_section()
