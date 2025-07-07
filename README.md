# 🎙️ AI Podcast Generator

Transform AI articles into engaging podcast-style audio content with this complete generative AI pipeline!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/ai-podcast-generator/blob/main/AI_Podcast_Generator.ipynb)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

- ✅ **Free & Open Source**: Uses only free APIs and open-source tools
- ✅ **URL Extraction**: Automatically extracts text from article URLs
- ✅ **AI Summarization**: Powered by BART model for intelligent content summarization
- ✅ **Podcast Style Rewriting**: Converts formal text to conversational podcast tone
- ✅ **High-Quality TTS**: Uses Google Text-to-Speech for natural audio generation
- ✅ **Audio Enhancement**: Automatic intro/outro and background music support
- ✅ **Web Interface**: User-friendly Streamlit interface
- ✅ **Google Colab Ready**: One-click deployment to Google Colab
- ✅ **Download Support**: Export podcasts as MP3 files

## 🚀 Quick Start

### Option 1: Google Colab (Recommended)

1. Click the "Open in Colab" badge above
2. Run all cells in sequence
3. Use the generated public URL to access the web interface
4. Start creating podcasts!

### Option 2: Local Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ai-podcast-generator.git
cd ai-podcast-generator

# Install dependencies
pip install -r requirements.txt

# Download sample background music
wget -O music.mp3 "https://cdn.pixabay.com/download/audio/2024/12/09/audio_5c5be993bd.mp3?filename=vlog-music-beat-trailer-showreel-promo-background-intro-theme-274290.mp3"

# Run the Streamlit app
streamlit run streamlit_app.py
```

## 📋 Requirements

- Python 3.7+
- Internet connection (for model downloads and TTS)
- ~2GB RAM (for AI models)
- ~1GB storage (for model cache)

## 🛠️ How It Works

The AI Podcast Generator follows a simple 5-step pipeline:

1. **Text Extraction**: Extracts content from URLs or accepts raw text input
2. **AI Summarization**: Uses Facebook's BART model to create concise summaries
3. **Style Conversion**: Transforms formal text into conversational podcast style
4. **Text-to-Speech**: Converts text to natural-sounding audio using gTTS
5. **Audio Enhancement**: Adds intro/outro and optional background music

## 🎯 Use Cases

- **Content Creators**: Convert blog posts into podcast episodes
- **Researchers**: Transform research papers into accessible audio content
- **Educators**: Create audio summaries of educational materials
- **News Outlets**: Generate podcast versions of news articles
- **Personal Use**: Convert any text content into podcast format

## 📱 Web Interface

The Streamlit web interface provides:

- **Input Options**: URL extraction or direct text input
- **Configuration**: Toggle intro/outro and background music
- **Real-time Processing**: Live progress updates during generation
- **Audio Player**: Built-in player to preview generated podcasts
- **Download**: One-click MP3 download functionality

## 🔧 Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Text Input    │───▶│   AI Processing  │───▶│  Audio Output   │
│                 │    │                  │    │                 │
│ • URL Extract   │    │ • Summarization  │    │ • TTS Generation│
│ • Raw Text      │    │ • Style Rewrite  │    │ • Intro/Outro   │
│ • File Upload   │    │ • BART Model     │    │ • Background    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 📁 Project Structure

```
ai-podcast-generator/
├── AI_Podcast_Generator.ipynb    # Google Colab notebook
├── streamlit_app.py              # Web interface
├── text_processing.py            # Text extraction & summarization
├── audio_processing.py           # TTS & audio enhancement
├── requirements.txt              # Python dependencies
├── music.mp3                     # Sample background music
├── README.md                     # This file
├── src/                          # Source modules
│   ├── text_processing.py
│   └── audio_processing.py
├── docs/                         # Documentation
└── assets/                       # Media assets
```

## 🎨 Customization

### Text Processing
- Modify summarization models (try different BART variants)
- Adjust summary length parameters
- Customize podcast style rewriting patterns

### Audio Generation
- Change TTS language and voice settings
- Modify intro/outro templates
- Adjust background music volume and effects

### Web Interface
- Customize Streamlit theme and layout
- Add new configuration options
- Implement user authentication

## 📊 Example Output

**Input Text:**
```
Artificial intelligence (AI) is rapidly transforming various industries, 
from healthcare to finance. Its ability to process vast amounts of data 
and identify patterns has led to breakthroughs in drug discovery...
```

**Generated Summary:**
```
Artificial intelligence is transforming industries like healthcare and 
finance through data processing and pattern recognition, leading to 
breakthroughs in drug discovery and fraud detection.
```

**Podcast Script:**
```
Alright, so let's dive into this. What we're essentially looking at is... 
Artificial intelligence is transforming industries like healthcare and 
finance through data processing and pattern recognition. So, this has led 
to breakthroughs in drug discovery and fraud detection. And that's pretty 
fascinating, isn't it?
```

## 🔍 Troubleshooting

### Common Issues

1. **Model Download Fails**
   - Ensure stable internet connection
   - Models download automatically on first use
   - Check available disk space (~1GB needed)

2. **Audio Generation Errors**
   - Verify internet connection for gTTS
   - Check if text is not empty
   - Try shorter text if processing fails

3. **Memory Issues**
   - Use Google Colab for better resources
   - Process shorter texts
   - Restart notebook if needed

### Performance Tips

- Use Google Colab for faster processing
- Keep text under 1000 words for optimal performance
- Enable GPU in Colab for faster model inference
- Cache models locally to avoid re-downloading

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Contribution Ideas

- Better text extraction algorithms
- More sophisticated podcast style rewriting
- Advanced audio processing features
- Multi-language support
- Voice cloning capabilities
- Batch processing functionality

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face Transformers** for the BART summarization model
- **Google Text-to-Speech** for high-quality audio generation
- **Streamlit** for the amazing web framework
- **Pixabay** for royalty-free background music
- **PyDub** for audio processing capabilities

## 📞 Support

- 🐛 **Bug Reports**: [Open an issue](https://github.com/your-username/ai-podcast-generator/issues)
- 💡 **Feature Requests**: [Start a discussion](https://github.com/your-username/ai-podcast-generator/discussions)
- 📧 **Email**: your-email@example.com

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Built with ❤️ using Python, Transformers, gTTS, and Streamlit**

*Happy podcasting! 🎙️*

