# BDIX Tester

A comprehensive BDIX (Bangladesh Internet Exchange) server testing application built with Python and Tkinter. This tool helps users test the connectivity and status of various BDIX servers including FTP, movie, TV, and famous servers.

## Features

- **Multi-Category Server Testing**: Test different types of BDIX servers (FTP, Movie, TV, Famous servers)
- **Real-time Progress Tracking**: Animated progress indicator with percentage completion
- **Custom Timeout Settings**: Configurable timeout values (1-5 seconds)
- **Interactive Results Display**: Treeview interface to browse active servers
- **Direct Server Access**: Double-click to open servers in browser
- **Copy to Clipboard**: Easy copying of server URLs
- **Custom UI**: Modern dark-themed interface with custom buttons and animations
- **Threaded Operations**: Non-blocking server testing with threading support

## Demo Video

🎥 **[Watch BDIX Tester in Action](https://youtu.be/-XDYmtXMOeA)**

See the complete functionality of BDIX Tester including real-time server testing, interactive UI, results categorization, and server connectivity demonstrations.

## Screenshots

The application features a sleek dark interface with:
- Animated GIF loader during testing
- Progress percentage display
- Custom styled buttons and controls
- Categorized server listing with interactive treeview

## Prerequisites

- Python 3.6 or higher
- Windows OS (uses `windll` for window management)
- Active internet connection for server testing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bdix-tester.git
cd bdix-tester
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure you have the required resource files in the `resource/` directory:
   - Images: `background_1.png`, `background_2.png`, `b1.png` through `b6.png`, etc.
   - Icon: `title_icon.ico`
   - Animation: `a5.gif`
   - Server lists: `famous_ftp.txt`, `ftp_server.txt`, `movie_server.txt`, `tv_server.txt`

## Usage

1. Run the application:
```bash
python bdix_tester.py
```

2. **Testing Servers**:
   - Click the "Start" button to begin testing all servers
   - Set timeout value (1-5 seconds) using the dropdown
   - Monitor progress with the animated loader and percentage display

3. **Viewing Results**:
   - Click "View Results" to see categorized active servers
   - Use category buttons (All, Movie, FTP, TV, Famous) to filter results
   - Double-click any server entry to open in browser
   - Click on a server and use the copy button to copy URL to clipboard

4. **Controls**:
   - **Start**: Begin server testing process
   - **Stop**: Halt the testing process
   - **View Results**: Open results window
   - **Back**: Return to main window
   - **Minimize**: Minimize application
   - **Close**: Exit application

## File Structure

```
bdix-tester/
├── bdix_tester.py          # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── resource/              # Resource directory
    ├── title_icon.ico     # Application icon
    ├── a5.gif            # Loading animation
    ├── background_1.png   # Main window background
    ├── background_2.png   # Results window background
    ├── b1.png - b6.png   # Button images
    ├── back.png          # Back button
    ├── all.png           # All servers button
    ├── movie.png         # Movie servers button
    ├── ftp.png           # FTP servers button
    ├── tv.png            # TV servers button
    ├── famous.png        # Famous servers button
    ├── copy.png          # Copy button
    ├── yes.png           # Yes button
    ├── no.png            # No button
    ├── famous_ftp.txt    # Famous FTP servers list
    ├── ftp_server.txt    # FTP servers list
    ├── movie_server.txt  # Movie servers list
    └── tv_server.txt     # TV servers list
```

## Server List Format

The server list files (`*.txt`) should contain one server URL per line:
```
http://example1.com
http://example2.com
ftp://example3.com
```

## Technical Details

- **GUI Framework**: Tkinter with custom styling
- **HTTP Requests**: Uses `requests` library for server connectivity testing
- **Threading**: Multi-threaded operation to prevent UI freezing
- **Window Management**: Custom title bar with Windows API integration
- **Animation**: GIF frame animation for loading indicator

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Known Issues

- Application is designed specifically for Windows (uses `windll`)
- Requires all resource files to be present in the `resource/` directory
- Internet connection required for server testing functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Boranno Golder**

## Acknowledgments

- Thanks to the BDIX community for server information
- Built for testing Bangladesh Internet Exchange servers
- Special thanks to contributors and testers

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/boranno/bdix-tester/issues) page
2. Create a new issue with detailed information
3. Include error messages and system information

---

**Note**: This tool is for educational and testing purposes. Please respect server policies and usage guidelines when testing connectivity.