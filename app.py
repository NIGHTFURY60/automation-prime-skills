



# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time

# # def wait_for_manual_login(driver):
# #     # This function pauses execution until you hit Enter in the console
#         # print("Please log in manually. Waiting 60 seconds before continuing...")
#         # time.sleep(60)


# # def navigate_to_group(driver, group_name):
# #     groups_link = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.LINK_TEXT, "Groups"))
# #     )
# #     groups_link.click()
# #     time.sleep(2)
# #     group_link = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.LINK_TEXT, group_name))
# #     )
# #     group_link.click()
# #     print(f"Navigated to group: {group_name}")

# # def complete_pathway_chapter(driver):
# #     # Click "Get Started" three times for chapter steps
# #     for i in range(3):
# #         get_started = WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
# #         )
# #         get_started.click()
# #         print(f"Chapter step {i+1}: Clicked Get Started.")
# #         time.sleep(2)
# #     # Click "Get Started" on course material
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
# #     ).click()
# #     print("Clicked Get Started on course material.")
# #     time.sleep(2)
# #     # Click "View Content" then "Mark as Complete"
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
# #     ).click()
# #     print("Clicked View Content.")
# #     time.sleep(2)
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.LINK_TEXT, "Mark as Complete"))
# #     ).click()
# #     print("Clicked Mark as Complete.")
# #     time.sleep(2)

# # def take_quiz(driver):
# #     # Launch the quiz
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Launch')]"))
# #     ).click()
# #     print("Clicked Launch to start the quiz.")
# #     time.sleep(2)
# #     # Start Quiz
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Quiz')]"))
# #     ).click()
# #     print("Clicked Start Quiz.")
# #     time.sleep(2)
# #     # Answer quiz questions (assuming 5 questions)
# #     for q in range(1, 6):
# #         print(f"Answering Question {q}")
# #         radio_option = WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]"))
# #         )
# #         radio_option.click()
# #         time.sleep(1)
# #         WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
# #         ).click()
# #         time.sleep(1)
# #         if q < 5:
# #             WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next Question')]"))
# #             ).click()
# #             print("Moved to the next question.")
# #             time.sleep(2)
# #         else:
# #             WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.LINK_TEXT, "View Result"))
# #             ).click()
# #             print("Clicked View Result.")
# #             time.sleep(2)
# #             WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
# #             ).click()
# #             print("Clicked Continue.")
# #             time.sleep(2)
# #             WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Process My Result & Close')]"))
# #             ).click()
# #             print("Processed quiz result and closed quiz.")
# #             time.sleep(2)

# # def return_to_pathway(driver):
# #     driver.back()
# #     print("Returned to the pathway page.")
# #     time.sleep(2)

# # def main():
# #     # Setup WebDriver using Service (update the path as needed)
# #     service_obj = Service(r"C:\Users\jeswi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# #     driver = webdriver.Chrome(service=service_obj)
# #     driver.maximize_window()

# #     try:
# #         # Open the website and wait for manual login
# #         driver.get("https://www.futureskillsprime.in/")
# #         wait_for_manual_login(driver)
# #         time.sleep(7)
# #         # Navigate to the desired group (replace with your actual group name)
# #         navigate_to_group(driver, "KTU-SCMS SCHOOL OF ENGINEE")
        
        
# #         # Click initial "Get Started" to enter the pathway
# #         WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
# #         ).click()
# #         print("Entered the pathway by clicking initial Get Started.")
# #         time.sleep(2)
        
# #         # Loop through pathway chapters (adjust number as needed)
# #         num_chapters = 3  # Example: repeat for 3 chapters
# #         for chapter in range(1, num_chapters + 1):
# #             print(f"\n--- Processing Chapter {chapter} ---")
# #             complete_pathway_chapter(driver)
# #             take_quiz(driver)
# #             return_to_pathway(driver)
# #             time.sleep(2)
        
# #         print("\nCourse automation completed successfully.")
# #     except Exception as e:
# #         print("An error occurred during automation:", e)
# #     finally:
# #         driver.quit()

# # if __name__ == "__main__":
# #     main()





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def complete_pathway_chapter(driver):
#     # Click "Get Started" three times for chapter steps
#     for i in range(3):
#         get_started = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
#         )
#         get_started.click()
#         print(f"Chapter step {i+1}: Clicked Get Started.")
#         time.sleep(2)
    
#     # Click "Get Started" on course material
#     material_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
#     )
#     material_button.click()
#     print("Clicked Get Started on course material.")
#     time.sleep(2)
    
#     # Click "View Content" then "Mark as Complete"
#     view_content = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
#     )
#     # Click the "View Content" hyperlink (assumes it opens a new tab)
#     view_content = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
#     )
#     view_content.click()
#     time.sleep(2)

#     # Switch to the last opened tab and close it
#     driver.switch_to.window(driver.window_handles[-1])
#     driver.close()

#     # Optionally, switch back to the original tab (assumed to be the first)
#     driver.switch_to.window(driver.window_handles[0])
#     time.sleep(2)


#     mark_complete = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "Mark as Complete"))
#     )
#     mark_complete.click()
#     print("Clicked Mark as Complete.")
#     time.sleep(2)

# def take_quiz(driver):
#     # Click the "Launch" button to open the quiz
#     launch_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Launch')]"))
#     )
#     launch_button.click()
#     print("Clicked Launch to start the quiz.")
#     time.sleep(2)
    
#     # Click the "Start Quiz" button
#     start_quiz = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Quiz')]"))
#     )
#     start_quiz.click()
#     print("Clicked Start Quiz.")
#     time.sleep(2)
    
#     # Answer quiz questions (assuming 5 questions)
#     for q in range(1, 6):
#         print(f"Answering Question {q}...")
#         # Wait for a radio button to be clickable and select the first option
#         radio_option = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]"))
#         )
#         radio_option.click()
#         time.sleep(1)
#         submit_button = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
#         )
#         submit_button.click()
#         time.sleep(1)
        
#         if q < 5:
#             next_question = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next Question')]"))
#             )
#             next_question.click()
#             print("Moved to the next question.")
#             time.sleep(2)
#         else:
#             view_result = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.LINK_TEXT, "View Result"))
#             )
#             view_result.click()
#             print("Clicked View Result for the quiz.")
#             time.sleep(2)
#             continue_button = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
#             )
#             continue_button.click()
#             print("Clicked Continue.")
#             time.sleep(2)
#             process_close = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Process My Result & Close')]"))
#             )
#             process_close.click()
#             print("Processed quiz result and closed quiz.")
#             time.sleep(2)

# def return_to_pathway(driver):
#     driver.back()
#     print("Returned to the pathway page.")
#     time.sleep(2)

# def main():
#     # Setup WebDriver using the Service class (update the path as needed)
#     service_obj = Service(r"C:\Users\jeswi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.maximize_window()

#     try:
#         # Open the homepage
#         driver.get("https://www.futureskillsprime.in/")
#         print("Please manually log in and navigate to your course pathway page (where 'Get Started' is visible).")
#         print("Please log in manually. Waiting 60 seconds before continuing...")
#         time.sleep(60)

#         # Now the script will automate the rest of the course.
#         print("Starting course automation...")
        
#         # For each chapter in the pathway, complete the chapter and take the quiz.
#         num_chapters = 3  # Adjust as needed
#         for chapter in range(1, num_chapters + 1):
#             print(f"\n--- Processing Chapter {chapter} ---")
#             complete_pathway_chapter(driver)
#             take_quiz(driver)
#             return_to_pathway(driver)
#             time.sleep(2)
        
#         print("\nCourse automation completed successfully.")
#     except Exception as e:
#         print("An error occurred during automation:", e)
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     main()




# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def complete_pathway_chapter(driver, repeat_get_started=True):
#     if repeat_get_started:
#         # Click "Get Started" three times for lesson steps
#         for i in range(3):
#             get_started = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
#             )
#             driver.execute_script("arguments[0].scrollIntoView(true);", get_started)
#             time.sleep(1)
#             driver.execute_script("arguments[0].click();", get_started)
#             print(f"Lesson step {i+1}: Clicked Get Started.")
#             time.sleep(2)
#     else:
#         print("Skipping initial 'Get Started' clicks for the first lesson.")

#     # Click "Get Started" on the course material
#     get_started = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", get_started)
#     time.sleep(1)
#     driver.execute_script("arguments[0].click();", get_started)
#     print("Clicked Get Started on course material.")
#     time.sleep(2)
    
#     # Store the original window handle before clicking "View Content"
#     original_window = driver.current_window_handle
    
#     # Click the "View Content" hyperlink (assumed to open a new tab)
#     view_content = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
#     )
#     view_content.click()
#     print("Clicked View Content; new tab should open.")
#     time.sleep(2)
    
#     # Wait for new tab(s) to open
#     WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    
#     # Close all extra tabs (any handle not equal to the original_window)
#     all_handles = driver.window_handles
#     for handle in all_handles:
#         if handle != original_window:
#             try:
#                 driver.switch_to.window(handle)
#                 driver.close()
#                 print(f"Closed extra tab: {handle}")
#             except Exception as e:
#                 print("Error closing tab:", e)
    
#     # Switch back to the original window
#     try:
#         driver.switch_to.window(original_window)
#     except Exception as e:
#         print("Error switching back to the original window:", e)
#     time.sleep(2)
    
#     # Click "Mark as Complete" hyperlink
#     mark_complete = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "Mark as Complete"))
#     )
#     mark_complete.click()
#     print("Clicked Mark as Complete.")
#     time.sleep(2)


# def take_quiz(driver):
#     # Launch the quiz
#     launch_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Launch')]"))
#     )
#     launch_button.click()
#     print("Clicked Launch to start the quiz.")
#     time.sleep(2)
    
#     # Click the "Start Quiz" button
#     start_quiz = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Quiz')]"))
#     )
#     start_quiz.click()
#     print("Clicked Start Quiz.")
#     time.sleep(2)
    
#     # Answer quiz questions (assuming 5 questions)
#     for q in range(1, 6):
#         print(f"Answering Question {q}...")
#         radio_option = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]"))
#         )
#         radio_option.click()
#         time.sleep(1)
#         submit_button = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
#         )
#         submit_button.click()
#         time.sleep(1)
#         if q < 5:
#             next_question = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next Question')]"))
#             )
#             next_question.click()
#             print("Moved to the next question.")
#             time.sleep(2)
#         else:
#             view_result = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'View Result')]"))
#             )
#             view_result.click()
#             print("Clicked View Result for the quiz.")
#             time.sleep(2)
#             continue_button = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
#             )
#             continue_button.click()
#             print("Clicked Continue.")
#             time.sleep(2)
#             process_close = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Process My Result & Close')]"))
#             )
#             process_close.click()
#             print("Processed quiz result and closed quiz.")
#             time.sleep(2)

# def process_pathway(driver, num_lessons):
#     """
#     Loops through the lessons in the pathway.
#     For the first lesson, it skips the repeated "Get Started" clicks.
#     For subsequent lessons, it performs the full cycle.
#     After processing all lessons, the quiz is taken.
#     """
#     for lesson in range(1, num_lessons + 1):
#         print(f"\n--- Processing Lesson {lesson} of the pathway ---")
#         if lesson == 1:
#             complete_pathway_chapter(driver, repeat_get_started=False)
#         else:
#             complete_pathway_chapter(driver, repeat_get_started=True)
#         time.sleep(2)
    
#     print("\nAll lessons processed. Proceeding to quiz...")
#     take_quiz(driver)

# def main():
#     # Setup WebDriver using Service (update the path as needed)
#     service_obj = Service(r"C:\Users\jeswi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.maximize_window()

#     try:
#         # Open the website and allow manual login and pathway selection.
#         driver.get("https://www.futureskillsprime.in/")
#         print("Please manually log in and select the pathway from which you want to start.")
#         input("After you've clicked your desired pathway and the page is loaded, press Enter to continue automation...")

#         # Ask for the number of lessons in the pathway.
#         num_lessons = int(input("Enter the number of lessons in this pathway: "))
        
#         # Process the pathway lessons and then take the quiz.
#         process_pathway(driver, num_lessons)
        
#         print("\nCourse automation completed successfully.")
#     except Exception as e:
#         print("An error occurred during automation:", e)
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     main()



import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure logging to capture errors
logging.basicConfig(
    filename='automation.log', 
    level=logging.ERROR, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Credentials
EMAIL = "jeswinchristie1234@gmail.com"
PASSWORD = "Jeswin@2006"

try:
    # Initialize WebDriver and open the main website
    driver = webdriver.Chrome()
    driver.get("https://www.futureskillsprime.in/")
    driver.maximize_window()
    time.sleep(5)

    # Click on the header's Login button to open the login popup modal
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Log in')]"))
    ).click()
    time.sleep(3)
    # Wait for the login modal to appear; locate fields using placeholder attributes
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID,"userid_temp"))
    )
    time.sleep(3)
    # Enter login details into the text boxes identified by their placeholders
    driver.find_element(By.ID,"userid_temp").send_keys(EMAIL)
    driver.find_element(By.ID,"confData").send_keys(PASSWORD)

    time.sleep(3)
    # Click on the login button using its given ID (adjust 'loginBtn' as needed)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))
    ).click()

    # Wait for the page to load after logging in
    time.sleep(5)

    # Navigate to the Groups page (if not automatically redirected)
    driver.get("https://www.futureskillsprime.in/iDH/fsp/Dashboard/Groups")
    time.sleep(5)

    # Click on the "Visit" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Visit')]")
    )).click()
    time.sleep(8)
    
    

    # Click "Get Started" on the Course Journey page
    driver.execute_script("window.scrollBy(0, 530);")
    time.sleep(2)
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "enrol_btn_text.p-0.text-nowrap")
    )).click()
    time.sleep(5)
    
    # works untill this point
