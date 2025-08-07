# Fusion 360 Face/Edge Automation Add-in

**Streamline your Fusion 360 workflow with automatic command detection!**

This add-in automatically triggers the appropriate command when you select faces or edges in Fusion 360:
- 🔶 **Click a face** → Extrude dialog opens instantly
- 📏 **Click an edge** → Fillet dialog opens instantly

No more manually pressing `E` for extrude or `F` for fillet - just click and go!

## ✨ Features

- **Zero Configuration**: Works immediately after installation
- **Smart Detection**: Automatically distinguishes between faces and edges
- **Non-Intrusive**: Only active during normal selection mode, won't interfere with dialogs
- **Auto-Start**: Runs automatically when Fusion 360 starts
- **Lightweight**: Minimal performance impact
- **Universal**: Works with any Fusion 360 model or design

## 🚀 Installation

### Method 1: Manual Installation (Recommended)

1. **Download the files:**
   - `FaceEdgeAutomation.py`
   - `FaceEdgeAutomation.manifest`

2. **Create the add-in folder:**
   ```
   Windows: %appdata%\Autodesk\Autodesk Fusion 360\API\AddIns\FaceEdgeAutomation\
   Mac: ~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/FaceEdgeAutomation/
   ```

3. **Copy both files into the folder**

4. **Enable in Fusion 360:**
   - Open Fusion 360
   - Press `Shift + S` to open Scripts and Add-Ins dialog
   - Go to **Add-Ins** tab
   - Find **FaceEdgeAutomation** in the list
   - Check **"Run on Startup"** (important!)
   - Click **Run**

### Method 2: Git Clone

```bash
cd "%appdata%\Autodesk\Autodesk Fusion 360\API\AddIns\"
git clone https://github.com/your-username/fusion360-face-edge-automation.git FaceEdgeAutomation
```

Then follow steps 4 from Method 1.

## 🎯 How It Works

The add-in runs a lightweight background process that:

1. **Monitors your selections** in real-time
2. **Detects the entity type** (face vs edge) when you click
3. **Simulates the appropriate hotkey** (E for faces, F for edges)
4. **Opens the relevant dialog** with your selection ready

### Smart Behavior

- **Respects active commands**: Won't trigger when you're already in a dialog
- **Prevents duplicates**: Won't repeatedly trigger on the same selection
- **Stays out of your way**: Only active during normal selection mode

## 📋 Requirements

- **Fusion 360** (any recent version)
- **Windows** (uses Windows API for key simulation)
- **Python 3.7+** (included with Fusion 360)

## 🔧 Usage

Once installed and running:

1. **For Extrude**: Simply click any face in your model
   - The Extrude dialog opens automatically
   - Your selected face is already highlighted
   - Enter your distance and press OK

2. **For Fillet**: Simply click any edge in your model
   - The Fillet dialog opens automatically  
   - Your selected edge is already highlighted
   - Enter your radius and press OK

## 🐛 Troubleshooting

### Add-in doesn't appear in the list
- Ensure both `.py` and `.manifest` files are in the correct folder
- Restart Fusion 360
- Check that folder names match exactly

### Commands not triggering
- Verify "Run on Startup" is checked
- Make sure the add-in is running (green light in Scripts & Add-Ins)
- Try clicking **Stop** then **Run** in the Add-Ins dialog

### Extrude/Fillet dialogs open but selection is lost
- This is a timing issue - try clicking slightly slower
- Make sure you're clicking directly on faces/edges, not in empty space

### Add-in stops working
- Check Fusion 360's Text Commands panel for error messages
- Restart the add-in from Scripts & Add-Ins dialog
- Restart Fusion 360 if issues persist

## 🤝 Contributing

Found a bug or have an improvement idea?

1. **Issues**: Report bugs or request features via GitHub Issues
2. **Pull Requests**: Contributions welcome! Please test thoroughly
3. **Discussions**: Share your experience and help other users

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Acknowledgments

- Built for the Fusion 360 community
- Inspired by the need for faster CAD workflows
- Thanks to all users who provided feedback and testing

## 🔄 Version History

### v1.0.0
- Initial release
- Face detection → Extrude automation
- Edge detection → Fillet automation
- Auto-startup functionality
- Windows support

---

**Made with ❤️ for the Fusion 360 community**

*If this add-in saves you time, consider giving it a ⭐ on GitHub!*
