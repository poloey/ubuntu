import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
public class englishEngineFirstTest {
	public static void main(String[] args) {
              WebDriver driver = new FirefoxDriver();
              
              //working for login page

              String appUrl = "http://localhost:3000/english-engine";
              driver.get(appUrl);
              driver.manage().window().maximize();
              String expectedTitle = "English Engine";
              String actualTitle = driver.getTitle();
              if(expectedTitle.equals(actualTitle)) {
				System.out.println("correct title");  
              }else {
				System.out.println("incorrecttitle");
              }
              
              WebElement username = driver.findElement(By.id("name"));
              username.clear();
              username.sendKeys("9666851953");

              WebElement password = driver.findElement(By.id("pass"));
              password.clear();
              password.sendKeys("iiit123");

              WebElement sendBtn = driver.findElement(By.id("send"));
              sendBtn.click();
              
              System.out.println("this is the way of learn or quiz page");

              //@Learn or quiz page
              //making waiting browser for learnorquiz page
              WebDriverWait wait = new WebDriverWait(driver, 40);
              wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("browse0")));
              //making a locator variable
              By simpleASLoc = By.className("browse0");
              WebElement simpleASElement = driver.findElement(simpleASLoc);
              //ExpectedConditions.visibilityOfElementLocated(receive only locator not webelement)
              wait.until(ExpectedConditions.visibilityOfElementLocated(simpleASLoc));
              simpleASElement.click();
              System.out.println("this is the way of topic page");
              
              //@topic page
              wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("topic1")));
              WebElement topic1 = driver.findElement(By.className("topic1"));
              topic1.click();
              System.out.println("Now it is going to the learn page");

              //@learn page
              wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("learn0")));
              WebElement learn0 = driver.findElement(By.className("learn0"));
              learn0.click();
              System.out.println("Now its opening the modal");
              //change a modal
              String xpathNextBtn = "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div[3]/button";
              wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(xpathNextBtn)));
              WebElement NextModalBtn = driver.findElement(By.xpath(xpathNextBtn));
              NextModalBtn.click();
              System.out.println("Now it is in second Modal");
              //@now back to the learn page
              System.out.println("Now it is in learn page again");
              wait.until(ExpectedConditions.visibilityOfElementLocated(By.partialLinkText("arrow_back")));
              WebElement arrowBackBtn = driver.findElement(By.partialLinkText("arrow_back"));
              arrowBackBtn.click();
              System.out.println("Now its goes to back page");
              String xpathTestMenu = "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div/div[3]/h4";
              String xpathPollsMenu = "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div/div[4]/h4";
              String xpathSurveysMenu = "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div/div[5]/h4";
              //Test menu
              WebElement TestMenu = driver.findElement(By.xpath(xpathTestMenu));
              TestMenu.click();
              System.out.println("Now it is inside test ");
              wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("exam10")));
              WebElement exam10 = driver.findElement(By.className("exam10"));
              exam10.click();
              System.out.println("Test modal open");
              //click on a radio button and submit for another modal come up
              wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("div.radio-option:first-child input")));
              WebElement radioBtn = driver.findElement(By.cssSelector("div.radio-option:first-child input"));
              radioBtn.click();
              String xpathTestSubmitBtn = "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div/div/div[4]/div/div[2]/div/div[2]/div/div[1]/input";
              WebElement TestSubmitBtn = driver.findElement(By.xpath(xpathTestSubmitBtn));
              TestSubmitBtn.click();
              System.out.println("clicked on submit button and Now it is in the 2nd question");
              //Now back to the learn page
              arrowBackBtn.click();

			  //logout from the page
			  wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("log-out-button")));
			  WebElement logoutBtn = driver.findElement(By.className("log-out-button"));
			  logoutBtn.click();
			  System.out.println("Succefully logout");
              
              
	}


}

