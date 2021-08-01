# form-filler
I was frustrated by the need to perform redundant tasks when completing job applications and considering the irony of applying to jobs with "automation" in the title while clicking through menus for the nth time when I realized that I should come up with a better solution.

An internet search led me to Selenium, which is a Python library for automating in-broswer actions. It simply requires one to establish a browser window, direct it to a URL, and then commands can find elements on the current page and send clicks and text strings. I run it in the Spyder IDE, which lets me run code blocks as desired while still allowing me to conventionally browse and navigate pages.

Now, the fine print.

It's not quite as easy as the above makes it sound. For one thing, each company's website will require a customized set of commands. Additionally, some company's forms have a lot of variation in their structure between job requisitions (prepare to learn a fair bit about the webpage design of job application forms across the industry).

Also, many jobs applications will have components that are simply specific to that application, such as confirmation of skills unique to that requisition. Although this is really no problem at all. It's the really repetative stuff that we're concerned with.

To find the X_PATH of a page element, just right click > inspect. Then right click on the relevant region in the inspection pane and click "copy X_PATH". 

Additionally, if the target is the page itself, one can send commands to the window as though typing without directing keystrokes to a page element. This turns out to be super useful, since (1) a lot of page elements are not active until interacted with, which means they cannot be targeted by X_PATH (at least easily. It appears possible, but it's complicated. If you know how, message me!) and (2) element names may vary between job requisitions. Using TAB to move between elements seriously helps break reliance on X_PATHs.

I'm pretty satisfied with the result. Did it save me time relative to doing the tasks manually though? That will depend on how many times I end up using it before it gets me my next job.
