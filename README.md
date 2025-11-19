# Display Mode Switcher

A simple Windows GUI application to quickly switch between display modes using Windows' built-in `displayswitch.exe`.

## Features

- **Duplicate (Clone)** - Mirror your primary display to secondary displays (perfect for HDMI TV output)
- **Extend** - Extend your desktop across multiple displays
- **PC screen only** - Use only the primary display
- **Second screen only** - Use only the secondary display

## Requirements

- Windows 7 or later
- Python 3.x (if running from source)
- tkinter (included with Python on Windows)

## Installation

### Option 1: Run from Source

1. Ensure Python 3.x is installed
2. Run the script:
   ```powershell
   python display_clone_gui.py
   ```

### Option 2: Build Executable

The project includes a PyInstaller spec file for creating a standalone executable:

```powershell
pyinstaller display_clone_gui.spec
```

The executable will be created in the `dist` folder.

## Usage

1. Launch the application
2. Click the button corresponding to your desired display mode:
   - **Duplicate (Clone)** - For mirroring to TV/projector
   - **Extend** - For multi-monitor workspace
   - **PC screen only** - Disable external displays
   - **Second screen only** - Use only external display

3. A confirmation message will appear when the mode is successfully changed

## Use Case

This tool is particularly useful for:
- Quickly cloning your display to an HDMI TV
- Switching between laptop screen and external monitor
- Presentations requiring quick display mode changes
- Gaming or media viewing on TV

## Technical Details

The application uses Windows' native `displayswitch.exe` command-line utility with the following switches:
- `/clone` - Duplicate displays
- `/extend` - Extend desktop
- `/internal` - PC screen only
- `/external` - Second screen only

## License

Copyright (c) 2025 Kannan Industrials Ltd. All rights reserved.

## Author

KannanSA

## Support

For issues or questions, please open an issue on the GitHub repository.
