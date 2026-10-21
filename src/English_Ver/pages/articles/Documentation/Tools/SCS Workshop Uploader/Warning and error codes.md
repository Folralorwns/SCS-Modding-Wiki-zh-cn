# Documentation/Tools/SCS Workshop Uploader/Warning and error codes

In the validation results you can get errors and warnings. With most of them you also have descriptive information about what is the real reason of it. We present you the list of the error and warning codes with the explanation of what they mean.

**Errors:**

| Code | Name | Description |
| --- | --- | --- |
| 00001 | Generic error | Any error that does not fit error codes below. |
| 00002 | File not found | File is not found. |
| 00003 | Not allowed | Something that is not allowed for example placing ".." in paths or windows-like path separators. |
| 00004 | Malformed file | The file is malformed and will definitely crash the game - you should try to reexport it or resave it. |
| 00005 | Missing required attribute | Some of the required unit attribute is not set. |
| 00006 | Access denied | Tool failed to create file or read it. |
| 00007 | Not supported | Some file has not supported version or some feature is not supported. |
| 00008 | Unable to load | Unable to load some file - in most cases its similar to `00002` error. |
| 00009 | File is too big | File is too big. |
| 00010 | Unused field set | Field that must not be set was set. |

> **Useful link:** If you want to see all possible errors and solutions for them check this page - [Validation errors and solutions for them](Validation%20errors%20and%20solutions%20for%20them.md)

**Warnings:**

| Code | Name | Description |
| --- | --- | --- |
| 00001 | Generic warning | Any warning that does not fit warning codes below. |
| 00002 | Unused field set | Field that should be not set is set. Not critical but should be fixed. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Warning_and_error_codes | revision: 5187 | captured: 2026-10-21 23:56:14 -->
