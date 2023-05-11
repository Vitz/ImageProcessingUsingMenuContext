# ImageProcessingUsingMenuContext

Adds some image processing feautures to Windows Context Menu  (mouse right-click on file).

# Add custom function
To add new function (e.g resize) in Windows Context Menu just add new method to ImageEditor class and run Install.py like:
```
    def quick_xxx(self, item):
      img = Image.open(item)
      ...
      ...
```
Name of new method must starts with 'quick_'.


- .bat files will be generated autmaticly in ImageRunnes dir,
- Windows registry will be filled automatically with each .bat runner,
- Tab name in Windows Context Menu is based on method name and build as below  

```
self.name_safe.replace("-", " ").replace("_", " ").replace("P", "%").capitalize()

# effect:
# quick_reduce_10 --> Quick reduce 10
```



![img](https://github.com/Vitz/ImageProcessingUsingMenuContext/blob/master/process.png?raw=true)

