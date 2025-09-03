<!--
README

This markdown file serves as an example on how to format a checklist,
so that it can be successfully converted into html with the included py script.

Drag and drop the md file onto the md_to_html script, and a new html
will be created in the ../checklists directory.
Don't forget to add your new checklist to the index. See index.md for more info
-->

<!--Aircraft name and sources (up to 10 links - AdaptedFrom is optional)-->

AircraftName:Jolly Good Plane
AdaptedFrom: https://example.com https://another.com

<!--A category contains multiple checklists and can be collapsed-->

# Category

<!--A checklist can be "ticked off" by clicking on its header-->

## Checklist

<!--Everything after a colon is right-aligned -->

- Ground Crew: ADVICE
- APU: VERIFY ON
- EXT POWER: OFF
<!--An item can also have an image, revealed on hover or click -->
- This item has an [image](../assets/img/example/example.png): HOVER

<!--A divider helps with spacing out longer checklists-->

### Divider

<!--Info boxes are formatted differently-->

- (ATC) Request Push and Engine Start
- (Altitude) FL100
- (MCDU) DEP/ARR → Set RWY → Set SID/TRANS → EXEC
- (Tablet) Import Simbrief route & weather
<!--We can add images here, too! -->
- (Note) Start Boarding & [Refueling](../assets/img/example/example.png)
