# Good Bad Weird

Good Bad Weird is an app that uses Markov chains to generate random dad jokes, and allows users to adjust the weirdness of generated jokes by adjusting the length of the Markov chains.

## Contents
* [Tech Stack](#technologies)
* [Features](#features)
* [Installation](#install)
* [About Me](#aboutme)

## <a name="technologies"></a>Technologies
Backend: Python, Flask<br/>
Frontend: JavaScript, jQuery, AJAX, HTML, CSS<br/>
API: icanhazdadjoke<br/>

## <a name="features"></a>Features

Users can generate random dad jokes:
![](/static/screen_shots/2_44_30.png)

By default jokes are generated based on 2-word Markov chains, but users can adjust the length of the chains to 1, 2, or 3 words at any time. 1-word chains tend to be more bizarre, and 3-word chains tend to be closer to real jokes.
![](/static/screen_shots/2_47_21.png)
![](/static/screen_shots/2_48_12.png)

Users can click on any word in jokes to generate a new dad joke built off of then word. In python the new joke is built first in reverse off of the selected word and then forward. The selected word in marked in bold red, and that word is noted in red in the new joke as the starting point for building the new joke.
![](/static/screen_shots/2_45_51.png)

Users' jokes are stored in localStorage and can be retrieved at any time:
![](/static/screen_shots/2_46_17.png)

## <a name="install"></a>Installation

To run Good Bad Weird:

Clone or fork this repo:

```
https://github.com/agstaples/good-bad-weird.git
```

Run the app:

```
python3 server.py
```

You can now navigate to 'localhost:5000/' to access Good Bad Weird.

## <a name="aboutme"></a>About Me
Anne Staples is a Software Engineer in the Bay Area.
Visit her on [LinkedIn](http://www.linkedin.com/in/anne-staples).