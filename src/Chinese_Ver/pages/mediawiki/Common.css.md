# MediaWiki:Common.css

```
/* CSS placed here will be applied to all skins */

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

/** Notifications. */

.notification {
   padding: 5px;
   font-size: 10pt
}

.note {
   background-color: #c9edf7;
   border: 1px solid #6596a4;
   border-left: 10px solid #6596a4;
}

.tip {
   background-color: #f7f4c9;
   border: 1px solid #968e5b;
   border-left: 10px solid #968e5b;
}

.useful_link {
   background-color: #cef7c9;
   border: 1px solid #61965b;
   border-left: 10px solid #61965b;
}

/** Tutorial related styles. */

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
    display: table;
    width: 852px;
    border-spacing: 10px;
}

.tutorials_container > .tutorial_entry {
    display: table-cell;
    height: 0px;
}

.tutorial_entry > table {
    background-color: #aaa;
    overflow: hidden;
    height: 100%
}

.tutorial_entry h2 {
    margin: 0;
    padding: 0;
    border: none;
}

.tutorial_entry td {
    background-color: #a6c796;
    width: 400px;
    text-align: center;
    padding: 10px;
}

.tutorial_entry .steps {
    background-color: #ffffff;
    text-align: left;
    padding: 10px;
    height: 100%;
    vertical-align: top;
}

.tutorial_infobox td {
    background-color: #94c085;
    text-align: center;
    padding: 5px;
}

.tutorial_infobox tr {
    vertical-align: top;
}

.tutorial_infobox .info > td {
    text-align: left;
    vertical-align: top;
}

.tutorial_infobox .info > td:nth-of-type(2) {
    background-color: #fff;
}

.tutorial_infobox .row_name {
    background-color: #dcdcdc;
}

body.page-Main_Page.action-view h1.firstHeading, body.page-Main_Page.action-submit h1.firstHeading {
    display: none;
}
```

<!-- source: https://modding.scssoft.com/wiki/MediaWiki%3ACommon.css | revision: 3556 | captured: 2026-10-21 23:56:14 -->
