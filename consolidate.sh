#!/bin/bash
location="output/$1_tiles"
ls "$location/Before" | xargs -I {} mv $location/Before/{}  $location/before_{}
ls "$location/After" | xargs -I {} mv $location/After/{}  $location/after_{}
