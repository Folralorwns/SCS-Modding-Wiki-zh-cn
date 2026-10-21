# MediaWiki:Mobile.css

```
/* CSS placed here will affect users of the mobile site */

.home_tile {
    display: inline-block;
    background: #eee;
    width: 340px;
    margin-top: 5px;
    border: 1px solid #989898;
    vertical-align: top;
}

.home_tile > .description {
    display: inline-block;
    vertical-align: top;
    padding: 10px;
    font-family: sans-serif;
    font-size: 12px;
}

.home_tile > .description a {
    font-size: 14pt;
}

.home_tile > .icon {
    display: inline-block;
    width: 50px;
    text-align: center;
    vertical-align: middle;
    padding: 15px 15px 10px 15px;
    border-right: 1px solid #989898;
}

.wip {
    background: #F3D95D;
    text-align: center;
    font-size: 13pt;
    padding: 3px;
}

.tutorial_navigation {
    padding: 10px;
    background: #f9f9f9;
    border: 1px solid #aaa;
    overflow: hidden;
}

.tutorial_navigation p {
    margin: 0;
}

.tutorials_container {
    border-spacing: 10px;
}

.tutorials_container img {
    width: 100%;
}

/*** File system tree visualization classes ***/

.FST-IconFolder {
   background: url(images/9/93/FST-Folder.png);
   width: 16px;
   height: 16px;
   display: inline-block;
   background-size: 16px 16px;
   vertical-align: text-bottom;
   margin-right: 5px;
}

.FST-IconRoot {
   background: url(images/6/6e/FST-Root.png);
   width: 16px;
   height: 16px;
   display: inline-block;
   background-size: 16px 16px;
   vertical-align: text-bottom;
   margin-right: 5px;
}

.FST-IconFileTxt {
   background: url(images/4/48/FST-File.png);
   width: 16px;
   height: 16px;
   display: inline-block;
   background-size: 16px 16px;
   vertical-align: text-bottom;
   margin-right: 5px;
}

.FST-IconFileSii {
   background: url(images/c/c4/FST-Sii.png);
   width: 16px;
   height: 16px;
   display: inline-block;
   background-size: 16px 16px;
   vertical-align: text-bottom;
   margin-right: 5px;
}

.FST-ReadOnly {
   font-width: bold;
   color: red;
}

.folder_structure > pre {
   min-width: 740px;
}
```

<!-- source: https://modding.scssoft.com/wiki/MediaWiki%3AMobile.css | revision: 2414 | captured: 2026-10-21 23:56:14 -->
