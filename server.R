#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#
library(reticulate)
library(dplyr)
library(shiny)
library(knitr)
library(tools)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
  
  
  # Filter data based on selections
  
  
  output$plot1 <- renderPlot({
    source_python("player_search.py")
    a = player_search(input$text1,input$text2)
    b = player_search(input$text3,input$text4)
    data <- data
    data1 <- data %>% filter(batter == b & pitcher ==  a)
    c= unlist(data1$pitch_type, use.names = F)
    barplot(table(c))
  })
  
  output$plot2 <- renderPlot({
    source_python("player_search.py")
    a = player_search(input$text1,input$text2)
    b = player_search(input$text3,input$text4)
    data <- data
    data1 <- data %>% filter(batter == b & pitcher ==  a)
    d= data1$description
    barplot(table(d), las = 2, cex.names = 0.5 )
  })
  
  output$Pitcher1 <- renderPrint({
    
    if (input$text6 == "angels") {
      park = "Angel Stadium"
    } else if (input$text6 == "giants") {
      park = "AT&T Park"
      park1 = "Oracle Park"
    } else if (input$text6 == "cardinals") {
      park = "Busch Stadium"
    } else if (input$text6 == "giants") {
      park = "AT&T Park"
    } else if (input$text6 == "d-backs") {
      park = "Chase Field"
    } else if (input$text6 == "mets") {
      park = "Citi Field"
    } else if (input$text6 == "phillies") {
      park = "Citizen Bank Park"
    } else if (input$text6 == "tigers") {
      park = "Coamerica Park"
    } else if (input$text6 == "red sox") {
      park = "Fenway Park"
    } else if (input$text6 == "rockies") {
      park = "Coors Field"
    } else if (input$text6 == "dodgers") {
      park = "Dodger Stadium"
    } else if (input$text6 == "rangers") {
      park = "Globe Life Park in Arlington"
    } else if (input$text6 == "reds") {
      park = "Great American Ballpark"
    } else if (input$text6 == "royals") {
      park = "Kauffman Stadium"
    } else if (input$text6 == "marlins") {
      park = "Marlins Park"
    } else if (input$text6 == "giants") {
      park = "AT&T Park"
    } else if (input$text6 == "brewers") {
      park = "Miller Park"
    } else if (input$text6 == "astros") {
      park = "Minute Maid park "
    } else if (input$text6 == "nationals") {
      park = "Nationals Park"
    } else if (input$text6 == "athletics") {
      park = "Oco Coliseum"
    } else if (input$text6 == "orioles") {
      park = "Oriole Park"
    } else if (input$text6 == "padres") {
      park = "Petco Park"
    } else if (input$text6 == "pirates") {
      park = "PNC Park"
    } else if (input$text6 == "indians") {
      park = "Progressive Field"
    } else if (input$text6 == "blue jays") {
      park = "Rodgers Centre"
    } else if (input$text6 == "mariners") {
      park = "Safeco Field"
      park1 = "T-Mobile Park"
    } else if (input$text6 == "twins") {
      park = "Target Field"
    } else if (input$text6 == "rays") {
      park = "Tropicana Field"
    } else if (input$text6 == "braves") {
      park = "Turner Field"
      park1 = "Truist Park"
    } else if (input$text6 == "white sox") {
      park = "US Cellular Field"
      park1 = "Guaranteed Rate Field"
    } else if (input$text6 == "cubs") {
      park = "Wrigley Field"
    } else if (input$text6 == "yankees") {
      park = "Yankee Stadium"
    }
    
    library(dplyr)
    
    aa = data_1 %>% filter(grepl('2016', V1) ) %>% filter(grepl(park, V6)) %>% summarise(ave_temp = mean(as.integer(V7)))
    
    if (input$text6 == "giants"|input$text6 == "braves"|input$text6 == "mariners"|input$text6 == "white sox") {
      bb = data_2 %>% filter(grepl('2016', V1) ) %>% filter(grepl(park1, V2)) %>% summarise(Name = V2, HR_Per_Game = V3, Hits_Per_Game = V4, Runs_Per_Game = V5)
    } else {
      bb = data_2 %>% filter(grepl('2016', V1) ) %>% filter(grepl(park, V2)) %>% summarise(Name = V2, HR_Per_Game = V3, Hits_Per_Game = V4, Runs_Per_Game = V5)
    }
    
    
    ad= t(cbind(bb,aa))
    print(ad)
    
    
  })
  
  output$Batter1 <- renderPrint({
    
    if (input$text5 == "angels") {
      park = "Angel Stadium"
    } else if (input$text5 == "giants") {
      park = "AT&T Park"
      park1 = "Oracle Park"
    } else if (input$text5 == "cardinals") {
      park = "Busch Stadium"
    } else if (input$text5 == "giants") {
      park = "AT&T Park"
    } else if (input$text5 == "d-backs") {
      park = "Chase Field"
    } else if (input$text5 == "mets") {
      park = "Citi Field"
    } else if (input$text5 == "phillies") {
      park = "Citizen Bank Park"
    } else if (input$text5 == "tigers") {
      park = "Coamerica Park"
    } else if (input$text5 == "red sox") {
      park = "Fenway Park"
    } else if (input$text5 == "rockies") {
      park = "Coors Field"
    } else if (input$text5 == "dodgers") {
      park = "Dodger Stadium"
    } else if (input$text5 == "rangers") {
      park = "Globe Life Park"
    } else if (input$text5 == "reds") {
      park = "Great American Ballpark"
    } else if (input$text5 == "royals") {
      park = "Kauffman Stadium"
    } else if (input$text5 == "marlins") {
      park = "Marlins Park"
    } else if (input$text5 == "giants") {
      park = "AT&T Park"
    } else if (input$text5 == "brewers") {
      park = "Miller Park"
    } else if (input$text5 == "astros") {
      park = "Minute Maid Park"
    } else if (input$text5 == "nationals") {
      park = "Nationals Park"
    } else if (input$text5 == "athletics") {
      park = "Oco Coliseum"
    } else if (input$text5 == "orioles") {
      park = "Oriole Park"
    } else if (input$text5 == "padres") {
      park = "Petco Park"
    } else if (input$text5 == "pirates") {
      park = "PNC Park"
    } else if (input$text5 == "indians") {
      park = "Progressive Field"
    } else if (input$text5 == "blue jays") {
      park = "Rodgers Centre"
    } else if (input$text5 == "mariners") {
      park = "Safeco Field"
      park1 = "T-Mobile Park"
    } else if (input$text5 == "twins") {
      park = "Target Field"
    } else if (input$text5 == "rays") {
      park = "Tropicana Field"
    } else if (input$text5 == "braves") {
      park = "Turner Field"
      park1 = "Truist Park"
    } else if (input$text5 == "white sox") {
      park = "US Cellular Field"
      park1 = "Guaranteed Rate Field"
    } else if (input$text5 == "cubs") {
      park = "Wrigley Field"
    } else if (input$text5 == "yankees") {
      park = "Yankee Stadium"
    }
    
    library(dplyr)
    
    aa = data_1 %>% filter(grepl('2016', V1) ) %>% filter(grepl(park, V6)) %>% summarise(ave_temp = mean(as.integer(V7)))
    
    if (input$text5 == "giants"|input$text5 == "braves"|input$text5 == "mariners"|input$text5 == "white sox") {
      bb = data_2 %>% filter(grepl('2016', V1) ) %>% filter(grepl(park1, V2)) %>% summarise(Name = V2, HR_Per_Game = V3, Hits_Per_Game = V4, Runs_Per_Game = V5)
    } else {
      bb = data_2 %>% filter(grepl('2016', V1) ) %>% filter(grepl(park, V2)) %>% summarise(Name = V2, HR_Per_Game = V3, Hits_Per_Game = V4, Runs_Per_Game = V5)
    }
    
    
    ae = t(cbind(bb,aa))
    print(ae)
    
  })
  
  output$Agg1 <- renderPrint({
    
    hh = tail(data_3 %>% filter(grepl(paste(toTitleCase(input$text3), toTitleCase(input$text4)), V2)) %>%  select(V3,V5,V6,V7,V9))
    names = c('Dates','Opponent', 'Plate Appearances','At Bats','Hits')
    names(hh) = names
    print(hh)
    
  })
  
  output$plot3 <- renderPlot({
    source_python("player_search.py")
    a = player_search(input$text1,input$text2)
    b = player_search(input$text3,input$text4)
    data <- data
    data1 <- data %>% filter(batter == b & pitcher ==  a)
    d= data1$description
    barplot(table(d), las = 2 )
  })
  
  output$table <- DT::renderDataTable(DT::datatable({
    
    source_python("player_search.py")
    a = player_search(input$text1,input$text2)
    b = player_search(input$text3,input$text4)
    data <- data
    data1 <- data %>% filter(batter == b & pitcher ==  a)
    data1
  
  }
  ,options = list(searching = F)
  ))
    
    
  
})
