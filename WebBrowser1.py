# Import python package
import sys # Build-in python module
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# Creating class
class MainWindow(QMainWindow):
    # Creating a constructor or function
    def __init__(self):
        # Calling 'super()' connection
        super(MainWindow, self).__init__()
        # Creating a browser
        self.browser = QWebEngineView()
        # set url
        self.browser.setUrl(QUrl('https://google.co.in/'))
        # Set Central
        self.setCentralWidget(self.browser)
        # Browser open in full screen mode
        self.showMaximized()

        # Creating a navbar
        navbar = QToolBar()
        # Add toolbar
        self.addToolBar(navbar)

        # Creating back button
        back_btn = QAction('Back', self) # where, 'self' is the reference of the current class
        back_btn.triggered.connect(self.browser.back)
        # Add back button
        navbar.addAction(back_btn)

        # Creating forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        # Add forward button
        navbar.addAction(forward_btn)

        # Creating reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        # Add reload button
        navbar.addAction(reload_btn)

        #Creating home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navi_home)
        navbar.addAction(home_btn)

        #Creating youtube button
        you_btn = QAction('YouTube', self)
        home_btn.triggered.connect(self.you_ap)
        navbar.addAction(you_btn)

        #Creating my blogger button
        my_blogger_btn = QAction('My Blogger', self)
        my_blogger_btn.triggered.connect(self.blog_btn_ap)
        navbar.addAction(my_blogger_btn)

        # Creating a search bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navi_url)
        # Add widget
        navbar.addWidget(self.url_bar)

        # Fix search bar not changed
        self.browser.urlChanged.connect(self.update_url)

    def navi_home(self):
        self.browser.setUrl(QUrl('https://google.co.in/'))
    
    def you_ap(self):
        self.browser.setUrl(QUrl('https://youtube.com/'))
    
    def blog_btn_ap(self):
        self.browser.setUrl(QUrl('https://saxena88ankur.blogspot.com/'))
    
    def navi_url(self):
        abc = self.url_bar.text()
        self.browser.setUrl(QUrl(abc))
    
    def update_url(self, sc):
        self.url_bar.setText(sc.toString())
    
        
# Create a application
app = QApplication(sys.argv)
# Call 'QApplication()' # Set the browser name
QApplication.setApplicationName('MyWebEx')
# Create a new variable named 'window'
window = MainWindow()
# Call the app and execute
app.exec_()
