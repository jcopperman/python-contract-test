# features\contract_test.feature
Feature: Contract Testing for API

  Scenario: Verify the API contract
    Given the API is available
    When a request is made to the API
    Then the response should adhere to the contract