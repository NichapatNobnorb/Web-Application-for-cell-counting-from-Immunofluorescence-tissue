# Web-Application-for-cell-counting-from-Immunofluorescence-tissue
**Summary**
> The web application for automatic nucleus counting for immunofluorescence tissue (DAPI) is a user-friendly tool that uses advanced computer vision and machine learning algorithms to accurately count the number of nuclei in DAPI-stained tissue biopsy images. It provides multiple output formats, including an image with identified nuclei highlighted, a numerical value indicating the total number of nuclei, and a table containing additional metrics.

**How to use?**
>****Step 1: Upload your image****
>To upload a DAPI immunofluorescence tissue biopsy image, navigate to the left panel and go to the **Browse files** button. The image should be in `.png`, `.jpg`, or `.tif` format, and the file size should not exceed 10 MB.  
When you upload already, click the **Start Analysis** button in the left panel.

>****Step 2: Check the Results****
>On the results page, you will see an image with the identified nuclei highlighted, as well as a count of the number of nuclei in the image. There also be a table with additional data, such as the position of each nucleus.  
_Additional:_ to save the table and image result by clicking the **Save table** and **Save image** buttons. Table will be saved as `.csv` file and image will be saved as `.png` file.

The table will contain the following columns:
-   _**xmin**_: x-coordinate of the top-left corner of the nucleus
-   _**ymin**_: y-coordinate of the top-left corner of the nucleus
-   _**xmax**_: x-coordinate of the bottom-right corner of the nucleus
-   _**ymax**_: y-coordinate of the bottom-right corner of the nucleus
-   _**x (px)**_: x-coordinate of the nucleus center
-   _**y (px)**_: y-coordinate of the nucleus center
-   _**Mean Intensity**_: mean intensity of the nucleus
-   _**Horizontal radius (px)**_: horizontal radius of the nucleus
-   _**Vertical radius (px)**_: vertical radius of the nucleus
-   _**Area (px^2)**_: area of the nucleus
