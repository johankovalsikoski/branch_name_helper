# Branch Name Helper
![](https://i.ibb.co/p0LQ897/Screen-Shot-2020-10-23-at-9-43-25-AM.png)

## What is it?

This is a Python script to help on branch creation.

## How to use (macOS)

1. Download *__main.py__* file
1. Rename the file extension to *__.app__*
1. On terminal run *__chmod +x main.app__*
1. Run the application

## What each field means?

* _Replace spaces_ will replace all the blank space by whatever set on the field
* _Task prefix_ will be set to upper case
* _Task name_ will be set to lower case and clear special characters

## Exempli gratia:

Label | Field
------------ | -------------
Replace space | -
Task prefix | moon-2020
Task name | fly TO the moon!

And this is the result: **git checkout -b MOON-2020/fly-to-the-moon**
```diff
- Once you hit the button the result will be on your clipboard. There is no feedback!
```
