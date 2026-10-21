# User talk:Aveneger

Hi Avenger,

this page will be dedicated as communication channel for you about your contributions.

2024-04-16 - **suggestion/idea**: I was thinking about writing a script to generate kind of an "API Reference", as complete as both games combined (ATS/ETS2) uses in their def.scs files. That means, say:

```
def/vehicle/ai/bus_opalin.sii

traffic_spawn_condition: .traffic.bus_s.condition.time
{
 # spawn only in following game time intervals
 type: time

 # 06:00 - 9:00
 num_param[]: 360
 num_param[]: 540

 # 16:00 - 18:00
 num_param[]: 960
 num_param[]: 1080
}

traffic_spawn_condition: .traffic.bus_s.condition.city
{
 # spawn only inside cities
 type: city
 str_param[]: "?*"
}
```

Given the use above, I can infer that the `traffic_spawn_condition` type (shall I call it a "type"?) can take `type` as an `enum` and `num_param[]` as an `integer` and `str_param[]` as `string`.

Then by parsing all files, the script should be able to see other uses, like `type: area` and `type: weather` and "fill in" the enum for that case. It could also tell that `type` is mandatory and the `*_param` optional.

Then descriptions would be another problem. Either sync descriptions with the script to re-generate **API Reference** every release. It'd also be possible to get added/updated descriptions straight from the wiki and feed the script too.

And then for ease of maintenability, we could post it all in a single page and enable, for instance, expandable sections with the `details` and `summary` HTML, [The Details disclosure element - MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) to have all searchable in a single page, and not (initially) an endless scroll (hopefully).

```
<details>
 <summary>traffic_spawn_condition</summary>
 type => enum (area, city', time, weather)
</details>
```

Well, that may be a little big one, but that'd be something I like doing!

---

*> Hmm, how would this work when any unit gets an update/delete?*

**A: A full rerun, indeed, to regenerate the full "mega page". And, I suppose wiki would just be able to tell what exactly changed in a nice diff as much as any CVS probably does.**

*> Who would be maintaining the database of the units?*

**A: A volunteer, I'm afraid. Me at first.**

*> You would regenerate all the used units for each update and upload it?*

**A: That's one point I raised. It would be much easier if the page was a single one, right? Then topics "contracted" via a `<details>` HTML entity of sorts, something to enable units to be collapsed and expanded. At least for the first iterations of the doc. If it works well, then some kind of automation could be made to send to individual pages, not sure how much the wiki is "automatable", but form submission, etc. I think it's pretty possible, just not really viable for the first iterations of the generator.**

*> The point is not everything that is used in our data might still be valid, some attributes might be obsolete or just there and never even loaded by the game. Simply said, if sth like this should be present on official modding wiki, it should be created from the code itself, where units are declared as only code knows what is valid and what shall be there.*

**A: Agreed with the whole point. But what I have access to is the data; and better something close and concise than nothing, I thought when coming up with this idea. The right thing to do would be , yes, to extract from sources. But I don't think anyone in SCS has had the opportunity to work on something like that so far, right?**

So, the proposal really is full of caveats, there will be lots of assumptions and guesses, like the accepted input (float/int/str), acceptable ranges, mostly would come from "educated guesses" over values used throughout the data, or manual documentation input (descriptions, as the community finds out what does what). So, a `spawn_ratio` could report as accepted values an interval from 0.0 up to 1.0 while seems they could go at least as high as 6.0 with some meaning in the game. It would at least be a central reference for the game for modders and maybe even for the developer team, and could also be used to find mistakes in the data (single use popping up, range exceedingly high, unexpected change from previous version, etc).

(excuse my lack of experience to use this talk channel :})

--[50keda](https://modding.scssoft.com/index.php?title=User:50keda&action=edit&redlink=1) ([talk](https://modding.scssoft.com/index.php?title=User_talk:50keda&action=edit&redlink=1)) 16:24, 19 April 2024 (UTC)

<!-- source: https://modding.scssoft.com/wiki/User_talk%3AAveneger | revision: 5500 | captured: 2026-10-21 23:56:14 -->
