Feature: Leanplum

  Scenario: Create campaign and finish it
    Given Open Leanplum URL and login
    Then Open campaign page
    And Click button Create Campaign to start creating new campaign
    And Verify that the page is opened 'Select Campaign Goal'
    And Change the title of the campaign name
    And Choose your goal
    And Click on 'Target Audience' to set your target
    And Click on 'Delivery Method' to set your target
    And Set your 'Scheduled'
    And Click on 'Actions' to set your target
    And Choose your notifications Push
    And Review and click on button 'Start Campaign'
    And Click on button 'Start campaign' from modal
    And Click on button 'End Campaign' to finish
    And Click on button 'End' to close window
    And State of the created campaign is 'FINISHED'


  Scenario: Verify created campaign list
    Given Open created campaign 'New Campaign Test'
    And Verify the name of the campaign 'New Campaign Test'
    And Close browser
