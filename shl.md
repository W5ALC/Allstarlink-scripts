# SkyHubLink Monday Night Net Script

## Overview
This script is designed to facilitate the SkyHubLink Monday Night Net.
It guides the net control operator through the various sections of the net script,
including announcements, topics, and check-ins.
The script is written in Python and utilizes the `rich` library for
enhanced console output.

## Features
- Display net topics from a file or use default topics.
- Display SkyHubLink announcements from a file or use default announcements.
- Guide the net control operator through the net script with user-friendly prompts.
- Provide detailed instructions and reminders for effective net control.

## Requirements
- Python 3.x
- `rich` library

You can install the `rich` library using pip:
```sh
pip install rich
```
## Usage
Clone the repository:
```sh
git clone https://github.com/yourusername/skyhublink-net-script.git
cd skyhublink-net-script
```
Run the script with optional arguments for topic and SkyHubLink announcements files:
```sh
python3 net_script.py -t topics.txt -s shl_announcements.txt
```

## Command Line Arguments
-t, --topic: File containing net topics.
	     If not provided, default topics will be used.

-s, --shl: File containing SkyHubLink announcements.
	   If not provided, default announcements will be used.

## Example
```sh
python3 net_script.py -t my_topics.txt -s my_announcements.txt
```

## Script Details

Default Topics
If no topic file is provided, the script uses the following default topics:

Could you tell us about your favorite antenna configuration and why you prefer it?
Have you made any interesting DX contacts recently? Please share your experience.
How have the propagation conditions been in your area?
Have you encountered any challenges or successes lately?
(Additional default topics listed in the script...)

Default Announcements
If no SkyHubLink announcements file is provided,
the script uses the following default announcement:

No new Announcements at this time.

## Contributing
Contributions are welcome!
Please feel free to submit a pull request or open an issue
if you have any suggestions or find any bugs.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, please contact Jon at W5ALC@SKYHUBLINK.COM

Thank you for using the SkyHubLink Monday Night Net Script.
We hope it helps you run effective and engaging nets!

Feel free to customize and edit this README to better fit your needs!
