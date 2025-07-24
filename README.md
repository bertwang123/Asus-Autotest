---
title: Instruction for the program ASUS autotest

---

# Instructions for the programs

###### tags: `README`, `selenium`

This article is the instructions of the programs for the test of autotest position. The programs consist of three parts, and each represents the answer to the different questions. As to all the question descriptions, please refer to [the test](../TEST.pdf).

## Environment settings
The program is totally written and run in Python. The download link and install instructions can be referred to [Download Python](https://www.python.org/downloads/). If the further language and instructions of development environment are needed, please refer to the [Help Center](https://www.python.org/about/help/).

### Python

  - Version
      - Developed in version Python 3.13.5. The same or later version is recommended.

  - Required toolbox
      - Selenium (functional tests in web browser)
          - Developed in version 4.34.2. The same or later version is recommended.
          - The download link and install instructions can be referred to [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/).

  - Operating system
      - Developed in Windows 10 Professional version 22H2. Refer to the official webpage [Python Documentation](https://docs.python.org/3/using/windows.html).

### Google Chrome

  - Version
      - Developed in Google Chrome 138.0.7204.101. The same or later version is recommended.

      - The download link and install instructions can be referred to [Chrome](https://www.google.com/intl/zh-TW/chrome/).
    
  - Operating system
      - Developed in Windows 10 Professional version 22H2. Refer to the official webpage [Google Support](https://support.google.com/chrome/a/answer/7100626?hl=en#:~:text=Windows%2010%20or%20later%20or%20Windows%20Server,4%20processor%20or%20later%20that's%20SSE3%20capable.).

### Chrome Driver

  - Version
      - Developed in ChromeDriver 138.0.7204.92. The same or later version is recommended.

      - The download link and install instructions can be referred to [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/#stable).

  - Operating system
      - Developed in Windows 10 Professional version 22H2. Requirements are generally align with Chrome browser. Refer to the official webpage [Google Support](https://support.google.com/chrome/a/answer/7100626?hl=en#:~:text=Windows%2010%20or%20later%20or%20Windows%20Server,4%20processor%20or%20later%20that's%20SSE3%20capable.).

## Instructions

### Program 1(a) and 1(b)

The function parts of the program **1(a)** and **1(b)** are fixed. They show the sorting algorithm and backtracking algorithm respectively. You can modify the input array, i.e. `nums`; or you can change the sorting order, e.g. ascending order, by swithching the "less than" sign (<) to the "greater than" sign (>) in the inner `for` loop in program **1(a)**.

### Program 6

The purpose of program **6** is to fetch data on website. By web crawler, we can collect various elements on the page. The main purpose is to enumerate all combinations in order to figure out the disconnection problem.

The path of the `chromedriver.exe` can be set as your path. If this executable file is in the exact working directory, you can just modify the line to `service = Service("chromedriver.exe")`.

In order to fetch the data of "bandwidth" and "control channel" in different bands (2.4GHz and 5GHz), I set a timer to wait for the page loading. You can adjust the timer as you wish.

Then I list the desired elements, aiming to find out the dropdown menu of them. Prepare two arrays to save the `Select` objects and their texts. Generate all the combinations of texts and ready to print them out.

The question requires to save all the combinations into an excel file, so I open a workbook, name a worksheet as "Option Combinations" and name the headers. You can change the name as well.

In the `for` loop, I fill all the different combinations into the worksheet. Besides, I try to fetch the internet status in order to check whether it is connected or not in each combination. Therefore, I simulate the mouse hovering on the icon of internet status, trying to fetch the data and output in the worksheet.

Finally, Save the excel file on the same path as the python file. You can name it and change the path on your own.

#### Notice

After finishing ths program, there are several points I want to clarify. First, I don't add the line to actual "click" the "Apply" buttom because the webpage is intended for demonstration purposes only. Second, due to the same reason, I omit the waiting time in several places to make the program run faster. Third, the internet status are always "connected". I assume the reason is probably the same, though I'm not sure.

## Complexity
Let's analyze the time and space complexity of these programs.

### Program 1(a)
  - Time Complexity: O(n^2^)
      Compare to each other takes (n * (n-1) / 2) times.

  - Space Complexity: O(1)
      In-place.

### Program 1(b)
  - Time Complexity: O(n * n!)
      Permutations cost O(n!) and `for` loop costs O(n).

  - Space Complexity: O(n)
      Recusions call stacks.

### Program 6
  - Time Complexity: O(band0_bw * band0_channel * band1_bw * band1_channel)

  - Space Complexity: O(band0_bw * band0_channel * band1_bw * band1_channel)
