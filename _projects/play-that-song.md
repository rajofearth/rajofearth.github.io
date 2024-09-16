---
layout: projects
title: "Play-that-song"
description: "A Python-powered, terminal-based MP3 player designed for simplicity and customization. Enjoy a lightweight music experience with easy-to-use controls, all within the command line."
tags: [cli-music-player, music-player, python, terminal-app]
permalink: /projects/play-that-song/
---
  <h1><a href="javascript:history.back()" class="back-btn"><--</a
  >Projects</h1>
  <nav style="justify-content: center; padding-top: 20px;">
    <a href="/">Home</a>
    <a href="/blog/">Blog</a>
    <a href="/projects/">Projects</a>
    <a href="/about.html">About</a>
    <!-- Add other navigation links as needed -->
  </nav>
  

# Play That Song

**Play That Song** is a terminal-based MP3 player built with Python, utilizing `pygame`, `curses`, and `mutagen`. It features keyboard controls for playback, volume adjustment, seeking within tracks, shuffle, repeat modes, and a customizable text-based interface. The player can display song metadata and switch between music directories during runtime. Installation instructions are provided for Linux, macOS, and Windows.

## Features

- **Play, Pause, Stop** your tracks with easy keyboard shortcuts.
- **Repeat Modes:** Repeat a single track, repeat the entire playlist, or turn off repeat.
- **Shuffle Mode:** Shuffle your playlist to play songs randomly.
- **Seek Functionality:** Move forward or backward within the track using arrow keys.
- **Volume Control:** Adjust the volume using up and down arrows.
- **Change Music Folder:** Quickly switch between different music directories from within the player.
- **Displays Song Metadata:** See the currently playing song’s title, artist, and album.
- **Customizable Playlist View:** Browse through your playlist with the current track highlighted.
- **Curses Interface:** A retro text-based interface that runs right in your terminal.

## Screenshots
*Home Page*
![image](https://github.com/user-attachments/assets/053576e7-b887-430c-b0f5-482883f01bcf)
*Folder Change*
![image](https://github.com/user-attachments/assets/a5051130-2969-462a-ad76-064f2af49a57)




## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/rajofearth/play-that-song.git
    cd play-that-song
    ```

2. **Install the required dependencies:**

    - **For Linux/macOS:**
      ```bash
      pip install -r requirements.txt
      pip install curses
      ```

    - **For Windows:**
      ```bash
      pip install -r requirements.txt
      pip install windows-curses
      ```

3. **Run the player:**
    ```bash
    python play_that_song.py
    ```

## Usage

### Controls

| Key         | Action                            |
|-------------|-----------------------------------|
| **P**       | Play/Pause the current track      |
| **S**       | Stop the track                    |
| **R**       | Toggle repeat mode (Off/One/All)  |
| **H**       | Toggle shuffle mode               |
| **N**       | Play the next track               |
| **B**       | Play the previous track           |
| **← / →**   | Seek backward/forward in track    |
| **↑ / ↓**   | Increase/Decrease volume          |
| **F**       | Change music folder               |
| **ESC**     | Cancel folder change              |
| **Q**       | Quit the player                   |

### Changing the Music Folder

1. Press **F** to change the music folder.
2. Type the path to your music folder (e.g., `~/Music/`).
3. Press **Enter** to load the new folder or **ESC** to cancel.

### Default Music Folder

- The player starts with a default music folder. You can set this path in the code or change it during runtime using the **F** key.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to improve this project.

## Acknowledgments

- Built using [pygame](https://www.pygame.org/) for audio handling.
- [curses](https://docs.python.org/3/library/curses.html) for the text-based terminal interface.
- [mutagen](https://mutagen.readthedocs.io/en/latest/) for reading MP3 metadata.
- Special thanks to the Python and open-source community for making such projects possible.

## Contact

For any questions, suggestions, or feedback, please reach out via [GitHub Issues](https://github.com/rajofearth/play-that-song/issues).
