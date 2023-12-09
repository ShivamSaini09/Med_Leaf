# Med Leaf

Med Leaf is a project aimed at automating the identification of medicinal plants using image processing and machine learning. The system employs Azure Custom Vision to predict the species of medicinal plants based on images of their leaves.

## Getting Started

To use the Med Leaf project, follow these steps:

### Prerequisites

- Python 3.x
- [Install Azure Custom Vision SDK](https://pypi.org/project/azure-cognitiveservices-vision-customvision/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/med-leaf.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Azure Custom Vision:

   - Obtain Azure Custom Vision prediction URL.
   - Obtain Azure Custom Vision prediction key.

### Usage

1. Capture images of medicinal plant leaves using a camera.
2. Run the Med Leaf application:

   ```bash
   python med_leaf.py
   ```

3. Upload the captured images through the user interface.
4. The application will utilize Azure Custom Vision to predict the plant species.

### Configuration

Create a file named `.env` in the project root and add the following:

```dotenv
AZURE_CUSTOM_VISION_URL=your_custom_vision_url
AZURE_CUSTOM_VISION_KEY=your_custom_vision_key
```

