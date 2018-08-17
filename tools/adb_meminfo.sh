#!/bin/sh

while [[ true ]]; do
	#statements
	adb shell dumpsys meminfo com.starmakerinteractive.starmaker | grep Java
	sleep 1
done

