### Selenium to enroll in college classes
At my college, if I want to take all the classes, I need to open the website and then enroll in all of them. But often the site is down, so it takes hours to do something very simple. After a few semesters I gave up trying to do it manually and decided to try to create this automation. The idea is simple, I need to go to the University website and sign up for classes without actually having to do so.
#### Libraries
The project is based on the [Selenium Library](https://www.selenium.dev/pt-br/documentation/) which is used for automation.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
```
#### Objectives
At Universitty website there is three options of enrollment:
1. Regular 
2. Summer Classes
3. Extraordinary

Basically, It will enroll me in the classes I want in the semester after I choose one of the options. I want to make this program useful for me first then I want to make it avaible for other students at my college.
### Progress
I divided the progress in some tasks:
- [ ] Cookies problems
- [ ] Regular Enrollment
    - [x] Finding Regular
    - [ ] Selecting my Classes
    - [ ] Solve the Password Problem
    - [ ] Return the Result
- [ ] Summer Classes
- [ ] Extraordinary
    - [ ] Finding Extraordinary
    - [ ] Selecting my Classes
    - [ ] Password Problem
    - [ ] Return the Result
