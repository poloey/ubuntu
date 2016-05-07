/**
 * this file created by Ranjith bro. this will be great cheat-sheet for selenium along with selenium.java
 */
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.interactions.Actions;

public class selenium2 {
	
	// Selenium Constants
	public static final String APPURL = "http://localhost:3000/";
	public static final String CHROMEDRIVERPATH = "/home/user/Downloads/chromedriver(path of ChromeDriver)";
	public static final int WAITTIME = 40;
	
	// App constants
	public static final String USERNAME = "username";
	public static final String PASSWORD = "password";
	
	public static void main(String[] args) {
	  System.setProperty("webdriver.chrome.driver", CHROMEDRIVERPATH);
      WebDriver driver = new ChromeDriver();
      
      //Open the app
      driver.get(APPURL);
      driver.manage().window().maximize();
      
      // Login page
      WebElement username = driver.findElement(By.id("name"));
      username.clear();
      username.sendKeys(USERNAME);

      WebElement password = driver.findElement(By.id("pass"));
      password.clear();
      password.sendKeys(PASSWORD);

      WebElement sendBtn = driver.findElement(By.id("send"));
      sendBtn.click();
      
      System.out.println("Going to list of learn or quiz view");

      //Learn or quiz page
      WebDriverWait wait = new WebDriverWait(driver, WAITTIME);
      wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("browse11")));
      By simpleASLoc = By.className("browse11");
    		  ;
      WebElement simpleASElement = driver.findElement(simpleASLoc);
      wait.until(ExpectedConditions.visibilityOfElementLocated(simpleASLoc));
      simpleASElement.click();
      System.out.println("Going to list of learn or quiz view");
      
      //Topic page
      wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("topic1")));
      WebElement topic1 = driver.findElement(By.className("topic1"));
      topic1.click();
      System.out.println("Now it is going to the learn page");

      //Sets Page
      wait.until(ExpectedConditions.visibilityOfAllElementsLocatedBy(By.className("set")));
      List<WebElement> allSets = (List<WebElement>) driver.findElements(By.className("set"));

      
      // Looping through the sets
      for (int i = 0; i < allSets.size(); i++) {
    	  wait.until(ExpectedConditions.visibilityOfAllElementsLocatedBy(By.className("set")));
    	  List<WebElement> sets = (List<WebElement>) driver.findElements(By.className("set"));
    	  
    	  // Going into a set
    	  sets.get(i).click();
    	  
    	  // Getting the no.of cards in a set
    	  wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("progress-bar")));
          WebElement progressBar = driver.findElement(By.className("progress-bar"));
          String progressBarSpan[] = progressBar.findElement(By.tagName("span")).getText().split("/");
          
          wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("right-button")));              
          WebElement nextButtonDiv = driver.findElement(By.className("right-button"));
          WebElement nextButton = nextButtonDiv.findElement(By.tagName("button"));

          // Going next card by card 
          for (int j = 0; j < Integer.parseInt(progressBarSpan[1]); j++) {    
        	  nextButton.click();				
          }                 
      }
      
	  //logout from the app
	  wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("log-out-button")));
	  WebElement logoutBtn = driver.findElement(By.className("log-out-button"));
	  logoutBtn.click();
	  System.out.println("Successfully logged out");
	  
	  //to close the web browser
  	  driver.close();
	  System.out.println("Successfully Tested!");        
              
	}

}