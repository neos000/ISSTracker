# ISSTracker
Tracking the ISS with the "wheretheiss.at" api. This is an experiment, and hasn't been refined. I made this script a while ago. 
I will possibly modify this script in the future.


# Usage
Navigate to the directory that is storing the IssTracker.py file using cmd or powershell.
Once that has been achieved simply start python.

1. Import the package.
``` import IssTracker ```

2. Create a new instance of the class (takes the sid argument, but ignore that for now by inputting a random integer.)
``` x = IssTracker.Tracker(sid) ```

3. Test the methods/functions.
   ``` x.track_satellite() ```
   ```
        {ISS TRACKER V.01}
        {CREATED BY NEOS}

         NAME: <iss>
         LATITUDE <-9.391537>
         LONGITUDE <-44.916797> 
   ```
