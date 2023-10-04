# YTMATE

- Bhai dekh videos chahiye in the best possible quality isliye banaya hai

## Setup:
  1. Install Pytube 15.0.0 and moviepy 1.0.3 (Havent tested with newer versions if any)
  2. Replace the line "223" in the file "innertube.py" at "C:\Users\<USER>\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube" in windows and "/usr/local/python/3.10.8/lib/python3.10/site-packages/pytube" in linux, with the following bit.

```Python
221  class InnerTube:
222      """Object for interacting with the innertube API."""
223      def __init__(self, client='ANDROID', use_oauth=False, allow_cache=True):
224          """Initialize an InnerTube object.
225  
226          :param str client:
227              Client to use for the object.
228              Default to web because it returns the most playback types.
229          :param bool use_oauth:
```

  4. All set (IG, if you encounter a problem then raise an issue or a PR)
## Credits:
- Documentation of Pytube: https://pytube.io/en/latest/index.html

- Age-restricted issue: https://stackoverflow.com/questions/75791765/how-to-download-videos-that-require-age-verification-with-pytube
