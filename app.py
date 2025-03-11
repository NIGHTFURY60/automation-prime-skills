import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

# Configure logging
logging.basicConfig(
    filename='course_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CourseAutomation:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = None
        self.pathway_count = 0
        self.all_pathways = []  # Store all pathway elements
        self.last_completed_index = -1  # Store index of last completed pathway
        
    def setup_driver(self):
        """Initialize the Chrome WebDriver with appropriate settings"""
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            logging.info("WebDriver initialized successfully")
        except Exception as e:
            logging.error(f"Failed to initialize WebDriver: {e}")
            raise

    def wait_and_click(self, by, value, timeout=10):
        """Wait for element to be clickable and click it"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)
            element.click()
            return True
        except Exception as e:
            logging.error(f"Failed to click element {value}: {e}")
            return False

    def login(self):
        """Handle the login process"""
        try:
            self.driver.get("https://www.futureskillsprime.in/")
            time.sleep(3)
            
            # Click login button
            self.wait_and_click(By.XPATH, "//a[contains(text(),'Log in')]")
            time.sleep(2)
            
            # Enter credentials
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "userid_temp"))
            )
            email_field.send_keys(self.email)
            
            password_field = self.driver.find_element(By.ID, "confData")
            password_field.send_keys(self.password)
            
            # Click login
            self.wait_and_click(By.XPATH, "//a[contains(text(),'Login')]")
            time.sleep(5)
            logging.info("Login successful")
            
        except Exception as e:
            logging.error(f"Login failed: {e}")
            raise

    def navigate_to_course(self):
        """Navigate to the course page"""
        try:
            self.driver.get("https://www.futureskillsprime.in/iDH/fsp/Dashboard/Groups")
            time.sleep(3)
            
            # Click Visit button
            self.wait_and_click(By.XPATH, "//button[contains(text(),'Visit')]")
            time.sleep(5)
            
            # Click Get Started
            self.driver.execute_script("window.scrollBy(0, 530);")
            time.sleep(2)
            self.wait_and_click(By.CLASS_NAME, "enrol_btn_text.p-0.text-nowrap")
            time.sleep(5)
            
            logging.info("Successfully navigated to course page")
        except Exception as e:
            logging.error(f"Failed to navigate to course: {e}")
            raise

    def count_pathways(self):
        """Count total number of pathways and store them"""
        try:
            # First scroll to top
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            
            print("Starting pathway count...")  # Visual feedback
            logging.info("Starting pathway count...")
            
            scroll_attempts = 0
            max_attempts = 20  # Maximum number of scroll attempts
            
            while scroll_attempts < max_attempts:
                # Find pathways in current view
                current_pathways = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='allActiveProd']")
                
                # Process found elements
                for pathway in current_pathways:
                    if pathway not in self.all_pathways:  # Only add new pathways
                        self.all_pathways.append(pathway)
                
                # Get current scroll position
                prev_scroll = self.driver.execute_script("return window.pageYOffset;")
                
                # Scroll down by viewport height
                self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
                time.sleep(1.5)  # Increased wait time for better loading
                
                # Get new scroll position
                new_scroll = self.driver.execute_script("return window.pageYOffset;")
                
                # If we couldn't scroll further, we've reached the bottom
                if new_scroll == prev_scroll:
                    break
                
                scroll_attempts += 1
            
            self.pathway_count = len(self.all_pathways)
            print(f"\nTotal pathways found: {self.pathway_count}")  # Visual feedback
            logging.info(f"Total pathways found: {self.pathway_count}")
            
            # Log individual pathways for verification
            for idx, pathway in enumerate(self.all_pathways, 1):
                try:
                    print(f"Pathway {idx}: {pathway.text}")
                    logging.info(f"Pathway {idx}: {pathway.text}")
                except:
                    continue
            
            # Scroll back to top
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
            
            return self.pathway_count
        except Exception as e:
            error_msg = f"Failed to count pathways: {str(e)}"
            print(error_msg)  # Visual feedback
            logging.error(error_msg)
            return 0

    def find_ongoing_pathway(self):
        """Find the ongoing pathway by finding the last pathway with 'Completed' in its text"""
        try:
            if not self.all_pathways:
                logging.error("No pathways found. Run count_pathways first.")
                return None
            
            # Find the last completed pathway
            for i, pathway in enumerate(self.all_pathways):
                try:
                    pathway_text = pathway.text
                    if "Completed" in pathway_text:
                        self.last_completed_index = i
                        print(f"Found completed pathway at index {i}: {pathway_text}")
                except:
                    continue
            
            # Get the next pathway after the last completed one
            if self.last_completed_index >= 0 and self.last_completed_index + 1 < len(self.all_pathways):
                next_pathway = self.all_pathways[self.last_completed_index + 1]
                # Scroll the ongoing pathway into view
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_pathway)
                time.sleep(1)
                print(f"Found ongoing pathway: {next_pathway.text}")
                logging.info(f"Found ongoing pathway: {next_pathway.text}")
                return next_pathway
            
            logging.error("Could not find ongoing pathway")
            return None
        except Exception as e:
            logging.error(f"Failed to find ongoing pathway: {e}")
            return None

    def process_lesson(self):
        
        try:
            # Find all lesson containers
            lesson_containers = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='allActiveProd']")
            
            if not lesson_containers:
                print("No more lessons found - might be quiz time")
                return False
                
            # Process each lesson container
            for container in lesson_containers:
                try:
                    # Check if lesson is already completed
                    container_text = container.text
                    if "Completed" in container_text:
                        print("Skipping completed lesson")
                        continue
                    
                    # Find Get Started button in this container
                    get_started = container.find_elements(By.XPATH, ".//button[contains(text(),'Get Started')]")
                    if get_started:
                        print("Clicking Get Started")
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", get_started[0])
                        time.sleep(1)
                        get_started[0].click()
                        time.sleep(2)
                        
                        # After Get Started, find and click View Content
                        view_content = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'View Content')]"))
                        )
                        print("Clicking View Content")
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_content)
                        time.sleep(1)
                        view_content.click()
                        time.sleep(2)
                        
                        # Handle new tab
                        if len(self.driver.window_handles) > 1:
                            self.driver.switch_to.window(self.driver.window_handles[1])
                            self.driver.close()
                            self.driver.switch_to.window(self.driver.window_handles[0])
                        
                        # Find and click Mark as Complete
                        mark_complete = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, 
                                "//a[contains(text(),'Mark as Complete')] | //button[contains(text(),'Mark as Complete')]"))
                        )
                        print("Clicking Mark as Complete")
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", mark_complete)
                        time.sleep(1)
                        mark_complete.click()
                        time.sleep(2)
                        
                        print("Lesson completed successfully")
                        return True
                except Exception as e:
                    print(f"Failed to process lesson: {str(e)}")
                    continue
            
            # If we've processed all lessons and found none to complete, return False
            print("No more incomplete lessons found")
            return False
            
        except Exception as e:
            logging.error(f"Failed to process lesson: {e}")
            return False

    def handle_quiz(self):
        """Handle the quiz section"""
        try:
            # Launch quiz
            self.wait_and_click(By.CLASS_NAME, "btn.launchBtn")
            time.sleep(3)
