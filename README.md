<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!--
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->

  <h3 align="center">Cars Used in Finland, 1995-2022</h3>

  <p align="center">
    An Interactive Dataset Visualization
    <br />
    <br />
    <!--<a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·-->
    <a href="https://github.com/jerkkov/cars-used-in-finland-1995-2022/issues">Report Bug</a>
    ·
    <a href="https://github.com/jerkkov/cars-used-in-finland-1995-2022/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br />


<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->



This project utilizes publicly available data from Traficom (Finnish Transport and Communications Agency) in the creation of an interactive visualizations. This visualization may be used to view and compare trends in car power source usage in Finland from 1995 to 2022. Interactive options include the selection of:
* Different power sources, including electric, gasoline, gas, diesel, and hydrogen
* Specific cities/areas in Finland
* Zooming in/out
* Dragging graph around

<br/>

<img src="images/cars-used-in-finland-1995-2022.PNG" alt="Graph">

<br/>


### Built With

<!--This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.-->

* [Python 3](https://www.python.org/)
* [Traficom dataset](https://trafi2.stat.fi/PXWeb/pxweb/en/TraFi/TraFi__Liikennekaytossa_olevat_ajoneuvot/010_kanta_tau_101.px/)



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To set up this visualization locally, follow these steps.

<br />

### Prerequisites

This project requires the installation of Python 3, along with the Bokeh package. If not already installed, download and install Python 3 and Bokeh.

* [Python 3](https://www.python.org/downloads/windows/)
* [Bokeh](https://docs.bokeh.org/en/latest/docs/first_steps/installation.html)
  
<br />

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/jerkkov/cars-used-in-finland-1995-2022
   ```
2. Navivate to local directory location
   ```sh
   cd C:~/cars-used-in-finland-1995-2022
   ```
3. Run the following command in the command line
   ```
   python cars-in-finland.py
   ```
Running the program creates an HTML file of the visualization in the local repository, which may be freely viewed again.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

If unsure where to start, check out the following usage demonstrations.

<br/>

<!--Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.-->

### Power Source Selection

All power source types are selected by default. Compare specific power types of interest by modifying the checkboxes in the upper right-hand corner of the visualization.

<img src="images/check-box.PNG" alt="Check">


<br/>


### Area Selection

The visualization shows data from the whole country of Finland by default. To view data from different areas of the country, select the text box in the upper left-hand corner, and type in a city name.
<img src="images/text-box.PNG" alt="Text">

The graph then pulls according data about car power types from that city. Use this function to compare the trends from different areas across Finland.

<!--Requires new image after graph reversal bug fix-->
<!--<img src="images/city.PNG" alt="City">-->

<br/>


<!--### Zooming-->


<br/>


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
<!--
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>
-->


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jerkko Viisteensaari - vjerkko@gmail.com

Project Link: [https://github.com/jerkkov/cars-used-in-finland-1995-2022](https://github.com/jerkkov/cars-used-in-finland-1995-2022)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Other resources used in this project.

* [Bokeh](https://bokeh.org/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jerkkov/cars-used-in-finland-1995-2022.svg?style=for-the-badge
[contributors-url]: https://github.com/jerkkov/cars-used-in-finland-1995-2022/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jerkkov/cars-used-in-finland-1995-2022.svg?style=for-the-badge
[forks-url]: https://github.com/jerkkov/cars-used-in-finland-1995-2022/network/members
[stars-shield]: https://img.shields.io/github/stars/jerkkov/cars-used-in-finland-1995-2022.svg?style=for-the-badge
[stars-url]: https://github.com/jerkkov/cars-used-in-finland-1995-2022/stargazers
[issues-shield]: https://img.shields.io/github/issues/jerkkov/cars-used-in-finland-1995-2022.svg?style=for-the-badge
[issues-url]: https://github.com/jerkkov/cars-used-in-finland-1995-2022/issues
[license-shield]: https://img.shields.io/github/license/jerkkov/cars-used-in-finland-1995-2022.svg?style=for-the-badge
[license-url]: https://github.com/jerkkov/cars-used-in-finland-1995-2022/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jerkko-viisteensaari/
[product-screenshot]: images/screenshot.png
