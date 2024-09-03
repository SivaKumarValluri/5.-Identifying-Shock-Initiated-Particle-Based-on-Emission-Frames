# Shock Initiated Particles Identification #

This work has been used to generate data for the publication: "Valluri, S.K., Salvati III, L., Dreizin, E.L., Dlott, D.D., Fast reactions of shocked energetic microporous metallic composites, Propellants, Explosives, Pyrotechnics 48 (10), 2023"
(https://onlinelibrary.wiley.com/doi/full/10.1002/prep.202300031)

![image](https://github.com/user-attachments/assets/061e69fd-ecd6-419f-b158-f604f5ce1b12)


## ImageJ File ##
This script processes a series of images from a directory, specifically for analyzing particles in PBX chips using cross-polarized images. Here's a concise summary of its functionality:

## 1.Initialization: ##

    Clears any previous results and sets directories for input and output.
    
## 2.Image Processing: ##

    - For each set of 16 images (8 stationary and 8 time-lapse):
    
        - Opens and processes images, applying scale, cropping, and thresholding.
        
        - Performs specific operations based on the type of particles (e.g., HMX chips or metallic particles in PDMS).
        
        - Analyzes particles using various techniques (e.g., Gaussian blur, watershed segmentation).
        
## 3.Measurement and Data Collection: ##

    - Measures and collects particle statistics from multiple trials.
    
    - Saves the measurement results into CSV files.
    
## 4. Final Steps: ##

    Closes all open windows and ROI Manager.

## 5. Output for Python Script: ##
### 1.CSV Files: ###

    - Particle Details: For each trial, the script saves a CSV file named Particle details in PBX chip for trial no. X.csv, where X is the trial number. This file contains details about the particles identified in the PBX chip from the stationary images.
    
    - Trial-Specific Particle Data: For each particle in a given trial, the script saves additional CSV files named Trial no. X Particle no. Y out of Z .csv, where X is the trial number, Y is the particle number, and Z is the total number of particles. These files contain measurements of the particle's characteristics at different time points.
    
### 2.Measurement Results: ###

    For each image processed, results are saved to a CSV file containing measurements such as mean, modal, and minimum values. These are generated from the Analyze Particles function.
    
### 3.Intermediate Image Files (if not closed properly): ###

    The script performs various image processing operations (e.g., Gaussian blur, thresholding) that generate intermediate images which may remain open if not properly closed by the script.
    
### 4.Logs and Results: ###

    The script handles various result windows and may close them if they are open to avoid clutter and ensure clean execution.
    
In summary, the primary output is a set of CSV files containing detailed measurements of particles from the images processed in each trial, along with any intermediate image files and results generated during the analysis.

## Python File ##
This script performs data analysis and visualization on image sequences from a camera. Here's a summarized breakdown of its functionality:

## 1.Setup and Libraries: ##

    - Imports necessary libraries (e.g., pandas, numpy, matplotlib).
    
    - Sets the working directory.
    
## 2.User Inputs: ##

    - Prompts the user to input the directory containing CSV files with image data and camera acquisition settings.
    
    - Asks for specifics such as the number of images, exposure settings, and delays between captures.
    
    - Requests confirmation for whether exposure and delays are consistent across images.
    
    - Offers an option to plot intensity values over time.
    
## 3.Processing User Inputs: ##

    - Collects and validates inputs regarding the number of images, exposure, and delays.
    
    - Creates time scale arrays based on these inputs.
    
## 4.Data Loading and Preparation: ##

    - Loads CSV files containing particle data and intensity measurements.
    
    - Computes average particle size and processes intensity data for various metrics (mean, mode, min, max).
    
## 5.Analysis and Visualization: ##

    - Computes statistical measures for each well's data.
    
    - Identifies particles that are shocked based on intensity changes before a specified duration.
    
    - Optionally plots intensity values for particles over time and saves these plots.
    
## 6.Output: ##

    - Writes the processed data and statistical analysis to an Excel file.
    
    - Saves plots and results in separate sheets within the Excel file.
    
In summary, the script processes image data to analyze particle sizes and intensity changes over time, identifies particles affected by shocks, and generates both data tables and visualizations to help interpret the results.
