#include <gtest/gtest.h>
#include <gtest/gtest.h>
#include <QApplication>
#include <QMainWindow>
#include <QPushButton>
#include <QTextEdit>
#include "MyTest.py"

class MyTestApp : public QMainWindow {
public:
    MyTestApp() : QMainWindow() {
      
        customWidget = new YourCustomWidget(this);

     
        setCentralWidget(customWidget);
    }

    void testGetIPv4Info() {
        customWidget->get_ipv4_info();
    }

 

private:
    YourCustomWidget* customWidget;
};

class TestMyTestApp : public ::testing::Test {
protected:
    void SetUp() override {
      
        int argc = 0;
        app = new QApplication(argc, nullptr);
        window = new MyTestApp();
    }

    void TearDown() override {
       
        delete window;
        delete app;
    }

    QApplication* app;
    MyTestApp* window;
};

TEST_F(TestMyTestApp, TestIPv4Info) {
 
    window->testGetIPv4Info();

   
    QString textOutput = window->customWidget->text_output->toPlainText();
    ASSERT_TRUE(textOutput.contains("IP:"));
    ASSERT_TRUE(textOutput.contains("Statyczne"));
    ASSERT_TRUE(textOutput.contains("Interfejs:"));
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}