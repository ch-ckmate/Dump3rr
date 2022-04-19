
<p align="center">
<img height="250" width="250" src="logo1.png"></img>
</p>
<H1 align="center">Dump3rr</H1>

<br><br>
With this tool you can dump an entire website.

<h4>Features</h4>

  - Replace page links in the html. (so you can browse it offline)
  - Download images and make sure that .js are loaded.
  - Download video: I only implemented download from Vimeo. (Since it is the most utilized)
  - Support Cookies.
  - You can stop and restart it ;). (Tip: Don't change the url)

<h4>Requirements</h4>

  - Python 3.8+
  - Pip
  - It will install the dependencies



<h4>How to use</h4>

  - Open the .py.
  - Change the url with a page of the website you want to dump.
  - Set to True if you want to download videos. (vimeo=True)
  - If you want to avoid some pages just inster it in the pagetoavoid variable. (if you want to avoid all the sub dirs, for example - https://1234test.test/lession/123/1.html just do pagetoavoid=['lession'])
