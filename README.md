# Simple Webtoon Creation Tool

My kids and I have been exploring [Webtoons](https://en.wikipedia.org/wiki/Webtoon), using pen, pencil, Photoshop, and Painter. We wanted to be able to share our creations with each other in a typical webtoon format, in our case following [https://tapas.io](https://tapas.io) format, and so we wrote a very simple Python script to fit our workflow.

The workflow is draw any why you like, pen, paper, Photoshop, Corel Painter, but the final output must be a set of web ready JEGs in **700 x 1000 px**. We used Photoshop to produce the final sliced JPEGS, see the tutorial [Creating and slicing verital comics](https://www.webtoons.com/en/challenge/ikous-tutorials/creating-and-slicing-vertical-comics/viewer?title_no=9019&episode_no=1) if you want to know more about this process.

Photoshop will produce a HTML file with the images stiched together, but we wanted something that was a little closer to the webtoon format, in our case this simply meant aligned in a centered table and support for pressing the 'f' key to fullscreen the page when reading on a laptop. It also meant that I could show the kids how to customize their own toons with CSS.

## Setup

Clone or download the repo.

You will will need Python 2. (We use Python 2.7 on MacOS.)

## Building a Toon

In the directory **site**, you will notice a directory called **images**, which is where your JPEGs need to be placed. (Remove the ones there otherwise things might get strange :-).)

To build the toon, simply ```cd site``` and run the command:

```
python tools/make_webtoon.py > index.html
```

This creates ```index.html```.

You can now simply open it in your favorite browser. As the kids wanted to share there toons with each other and we already have Python setup they use the built in web server to share there creations, which is as simple as running the following command in the directory with ```index.html```:

```
python -m SimpleHTTPServer
```

You can open http://localhost:8000 to access your toon on your local machine. For others to access your toon, they will need your machine's IP address, if you don't know how to get this, then there is a script in the tools directory to generate the HTTP address for you, simply run:

```
python site\tools\ipaddress.py
```

and type the outputted HTTP address into a browser on your local network. 

Try opening it on a phone to get the full webtoon experience :-)

Finally, you can, of course, modify the HTML, change the title is a good place to start, and custom CSS is waiting 
to be added in the file ```css/toon.css```.
