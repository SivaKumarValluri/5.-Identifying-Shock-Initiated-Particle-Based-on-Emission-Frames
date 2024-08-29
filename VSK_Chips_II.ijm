run("Clear Results"); // clear the results table of any previous measurements

//Data in the form of 8 raw stationary images before experiment and the 8 time snaps 
//at various instances of multiple trials in a single folder

//Reads the stationary image to give details of PBX chip(s) and the particles within the frame
//Applicable for cross-polarized images only


inputDirectory = getDirectory("Choose a Directory of Images");
fileList = getFileList(inputDirectory);
outputDirectory = getDirectory("Choose an output Directory");


//setBatchMode(true); 
//While-loop functions as 'Particles in PBX' Identifier within frame
//i=0; //Initializing 'no of trials' counter
i=0;
k=0;
while (i < fileList.length)
{
    //Need to update scalebar based on image acquired 
    open(inputDirectory+fileList[i]);
    run("Set Scale...", "distance=499.38 known=380 unit=Micron global");
    run("Set Measurements...", "area center bounding fit shape redirect=None decimal=3");
   	selectWindow(fileList[i]);	
    rename("original");
    
	//setTool("rectangle");
    makeRectangle(289, 152, 738, 732);
    run("Crop");
    run("Make Circular Selection...", "radius=353");
    run("Crop");
	
	//FOR HMX CHIPS- USE THIS SECTION
	//run("Normalize Local Contrast", "block_radius_x=40 block_radius_y=40 standard_deviations=3 center stretch");
	//run("Subtract Background...", "rolling=1 sliding");
	//run("Remove Outliers...", "radius=4 threshold=10 which=Dark");
	//run("Remove Outliers...", "radius=4 threshold=100 which=Bright");
	//run("Duplicate...", "title=duplicate");
	//run("Gaussian Blur...", "sigma=10");
	//imageCalculator("Subtract create", "original","duplicate");
	//selectWindow("Result of original");
	//rename("Processed");
	//close("duplicate");
	//close("original");
	//run("Invert");
	//run("Despeckle");	
	//Thresholding by user input
	//run("Threshold...");  // open Threshold tool
	//title = "Thresholding";
	//msg = "If necessary, use the \"Threshold\" tool to\nadjust the threshold, then click \"OK\".";
	//waitForUser(title, msg);
	//selectImage("Processed");  //make sure we still have the same image
	//getThreshold(lower, upper);
	//run("Particle Sizer");
	//setTool("rectangle");
	//setOption("ScaleConversions", true);
	//close();
	//selectWindow("Segmentierung");
			
	//FOR METALLIC PARTILCES IN PDMS-USE THIS SECTION
	rename("AAA");
	run("Duplicate...", " ");
	run("Gaussian Blur...", "sigma=10");
	imageCalculator("Divide create 32-bit", "AAA","AAA-1");
	selectWindow("Result of AAA");
	run("Convert to Mask");
	run("Remove Outliers...", "radius=2 threshold=50 which=Bright");
	selectWindow("Result of AAA");
	run("8-bit");
	run("Convert to Mask");
	run("Close-");
	run("Fill Holes");
	selectWindow("AAA");
	close();
	selectWindow("AAA-1");
	close();
	selectWindow("Result of AAA");	
	run("Watershed");
											
	//run("Irregular Watershed", "erosion=1000 convexity_threshsold=100");
    run("Analyze Particles...", "size=0-Infinity display exclude clear add in_situ");
    
    selectWindow("Results");
    saveAs("Results", outputDirectory+"Particle details in PBX chip for trial no. "+k+1+".csv");
	if (isOpen("Exception"))
	  {
	    selectWindow("Exception");
	    run("Close");
	  }
	if (isOpen("Console"))
	  {
	    selectWindow("Console");
	    run("Close");
	  }
	if (isOpen("Log"))
	  {
	    selectWindow("Log");
	    run("Close");
	  }
	if (isOpen("Results")) 
	  {
	    selectWindow("Results");
	    run("Close");
	  }
    close("*");
    
   	PN = roiManager("Count");
    for (j=0; j < PN; j++)
    {
    	//First
    	open(inputDirectory+fileList[i+8]);
	    makeRectangle(289, 152, 738, 732);
	    run("Crop");
	    run("Make Circular Selection...", "radius=353");
	    run("Crop");
		run("Set Measurements...", "mean modal min center redirect=None decimal=3"); 
		roiManager("Select",j);
		run("Measure");
		selectWindow(fileList[i+8]);
		close();
		//Second
		open(inputDirectory+fileList[i+9]);
	    makeRectangle(289, 152, 738, 732);
	    run("Crop");
	    run("Make Circular Selection...", "radius=353");
	    run("Crop");
		run("Set Measurements...", "mean modal min center redirect=None decimal=3"); 
		roiManager("Select",j);
		run("Measure");
		selectWindow(fileList[i+9]);
		close();
		//Third
		open(inputDirectory+fileList[i+10]);
	    makeRectangle(289, 152, 738, 732);
	    run("Crop");
	    run("Make Circular Selection...", "radius=353");
	    run("Crop");
		run("Set Measurements...", "mean modal min center redirect=None decimal=3"); 
		roiManager("Select",j);
		run("Measure");
		selectWindow(fileList[i+10]);
		close();
		//Fourth
		open(inputDirectory+fileList[i+11]);
	    makeRectangle(289, 152, 738, 732);
	    run("Crop");
	    run("Make Circular Selection...", "radius=353");
	    run("Crop");
		run("Set Measurements...", "mean modal min center redirect=None decimal=3"); 
		roiManager("Select",j);
		run("Measure");
		selectWindow(fileList[i+11]);
		close();
		//Fifth
		open(inputDirectory+fileList[i+12]);
	    makeRectangle(289, 152, 738, 732);
	    run("Crop");
	    run("Make Circular Selection...", "radius=353");
	    run("Crop");
		run("Set Measurements...", "mean modal min center redirect=None decimal=3"); 
		roiManager("Select",j);
		run("Measure");
		selectWindow(fileList[i+12]);
		close();
		//Sixth
		open(inputDirectory+fileList[i+13]);
	    makeRectangle(289, 152, 738, 732);
	    run("Crop");
	    run("Make Circular Selection...", "radius=353");
	    run("Crop");
		run("Set Measurements...", "mean modal min center redirect=None decimal=3"); 
		roiManager("Select",j);
		run("Measure");
		selectWindow(fileList[i+13]);
		close();
		//Seventh
		open(inputDirectory+fileList[i+14]);
	    makeRectangle(289, 152, 738, 732);
	    run("Crop");
	    run("Make Circular Selection...", "radius=353");
	    run("Crop");
		run("Set Measurements...", "mean modal min center redirect=None decimal=3"); 
		roiManager("Select",j);
		run("Measure");
		selectWindow(fileList[i+14]);
		close();
		//Eighth
		open(inputDirectory+fileList[i+15]);
	    makeRectangle(289, 152, 738, 732);
	    run("Crop");
	    run("Make Circular Selection...", "radius=353");
	    run("Crop");
		run("Set Measurements...", "mean modal min center redirect=None decimal=3"); 
		roiManager("Select",j);
		run("Measure");
		selectWindow(fileList[i+15]);
		close();
		
		//Saving data
		selectWindow("Results");
		saveAs("Results", outputDirectory+"Trial no. "+(k+1)+" Particle no. "+(j+1)+" out of "+ PN +" .csv");
		if (isOpen("Results")) 
		  {
		    selectWindow("Results");
		    run("Close");
		  }
    }

	 	        
    //Closing ROI manager at the end of processing the last trial                  
	i=i+16; // 8 stationary and 8 instances jumped
	k=k+1; //Title
	if(isOpen("ROI Manager"))
	{
		selectWindow("ROI Manager");
		run("Close");
	} 

}

//setBatchMode(false); 




close("*");

if (isOpen("Results")) 
  {
    selectWindow("Results");
    run("Close");
  }