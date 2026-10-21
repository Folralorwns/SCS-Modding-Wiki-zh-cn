# Tutorials/SCS Workshop Uploader/How to use mod versioning

> **TIP:** The game and tool is now in public beta. To use informational packages switch to public_beta branches on steam

With Steam Workshop mods you have better more flexible way to make your mod compatible with specified set of game versions. From ETS2 update 1.24, ATS update 1.3 and SCS Workshop Uploader 1.0.4 you can use new package option - informational package.

Informational package is a package that is used just for informational purpose - it means it does not affect gameplay in any way and is simply here to let mod user know what he has to do to use your mod - for example upgrade to the latest patch or downgrade to the currently supported patch (useful for map authors which needs some time to update mod to work with the latest patch).

Let's assume your **versions.sii** file looks like this:

```
SiiNunit
{

package_version_info : .content
{
    package_name: "content"
    compatible_versions[]: "1.25.*"
}

}
```

Which means your mod is only compatible with **1.25** update.

The incompatible package should contain **manifest.sii**, mod icon and mod description file. The manifest can be the same as for normal package - icon may indicate that this is just informational version without any functionality however mod user will see red "Incompatible" label next to the mod in mod manager so it can be the same as for different versions. The description *should* let mod user know how to adjust his game to make your mod working for example:

```
To make super mod 1000 work you must downgrade your game to patch 1.25. To do that go to your steam game library, select Euro Truck Simulator 2 click right mouse button on it select Preferences go to Beta tab and select temporary_1_25 - 1.25 for incompatible mods beta and close the dialog. Steam will downgrade your game version and on next launch of the game super mod 1000 will be useable again!
```

In **versions.sii** this version will look like this:

```
package_version_info : .info.any
{
    package_name: "informational"
    informational: true
}
```

This version will be used even for the older and for newer versions than **1.25**. At the moment there is no way to specify different informational package for older game version so for example if your mod will target **1.25** game patch you will be able to specify different informational version for 1.24 and older patches and different for 1.26 and newer. However you can specify version of informational package so it will be only used for specified version. Let's say you have two informational versions - one informing about downgrade (folder is called **downgrade_info_package**) and one informing about update of the game (folder is called **upgrade_info_package**).

You have nice description in both packages with advices how to do upgrade and downgrade all you need to do now is to just add the packages to **versions.sii**.

The version for older game versions will look like that: *(We use 1.24 and older versions only to demonstrate the functionality - this will start working starting from 1.24 patch of ETS2 and 1.3 of ATS)*

```
package_version_info : .info.upgrade.older.game.versions
{
    package_name: "upgrade_info_package"
    informational: true
    compatible_versions[]: "1.24.*"
    compatible_versions[]: "1.23.*"
    compatible_versions[]: "1.22.*"
}
```

The version for newer game versions will look like that.

```
package_version_info : .info.downgrade.newer.game.versions
{
    package_name: "downgrade_info_package"
    informational: true
}
```

You may notice in newer package there are no compatible versions specified. As your content package looks like that:

```
package_version_info : .content
{
    package_name: "content"
    compatible_versions[]: "1.25.*"
}
```

All the older game versions are listed in the upgrade package - downgrade package will be selected ONLY for the patches newer than 1.25.

<!-- source: https://modding.scssoft.com/wiki/Tutorials/SCS_Workshop_Uploader/How_to_use_mod_versioning | revision: 2702 | captured: 2026-10-21 23:56:14 -->
