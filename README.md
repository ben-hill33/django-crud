# Lab: Django CRUD and Forms
## Author: Ben Hill

## Overview
Add full CRUD functionality to your bag of tricks by building a Django project that allows Creating, Reading, Updating and Deleting.

## Feature Tasks and Requirements
- [x] Create snacks_crud_project Django project
- [x] Create snacks app
- [x] Create Snack model
  - [x] title field
  - [x] purchaser field
  - [x] description field
  - [x] Register model with admin
- [x] Create SnackListView that extends appropriate generic view
  - [x] associated url path is an empty string
- [x] Create SnackDetailView that extends appropriate generic view
  - [x] associated url path is <int:pk>/
- [x] Create SnackCreateView that extends appropriate generic view
  - [x] associated url path is create/
- [x] Create SnackUpdateView that extends appropriate generic view
  - [x] associated url path is <int:pk>/update/
- [x] Create SnackDeleteView that extends appropriate generic view
  - [x] associated url path is <int:pk>/delete/
- [x] Add urls to support all views, with appropriate names
- [x] Add templates to support all views
- [x] Add navigation links in appropriate locations to access all pages
- [x] Make all necessary changes to project level files for project to run
  - [x] In other words, make it work

## Implementation Notes
A lot of functionality is being added here. But it should still follow the “Django way.” So when in doubt refer back to demo.

## Stretch Goals
- add multiple models
- use an alternate test runner
- add more advanced fields to models, e.g. created time stamp
- [x] add styling
## User Acceptance Tests
- Test all Views
- Test Model
  - string representation
  - all fields
- When in doubt on what to test refer to demo
