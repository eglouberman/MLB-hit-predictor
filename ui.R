#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  titlePanel("Baseball Data App"),
  fluidRow(
    column(3, wellPanel(
      textInput("text1", "Pitcher First  Name :", "clayton"),
      textInput("text2", "Pitcher Last Name :", "kershaw"),
      textInput("text3", "Batter First Name :", "bryce"),
      textInput("text4", "Batter Last Name :", "harper"),
      textInput("text5", "Batter Team:", "nationals"),
      textInput("text6", "Pitcher Team:", "dodgers"),
      submitButton("Submit")
    )),
    
    column(4, 
           plotOutput("plot1", height = 350)
    ),
    
    column(4, 
           plotOutput("plot2", height = 350)
    ),
   
    
    
    column(4, 
           
           verbatimTextOutput("Pitcher1")
    ),
    
    column(4, 
           
           verbatimTextOutput("Batter1")
    ),
    
    column(12, 
           h4("Batter Last 5 Games"),
           verbatimTextOutput("Agg1")
    )
  ),
  
  
  # Create a new row for the table.
  DT::dataTableOutput("table")
))
