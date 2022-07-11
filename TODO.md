# Programming Exercise using **Pandas**

## Background:
A very small company called **KommatiPara** that deals with bitcoin trading has two separate datasets dealing with clients that they want to collate to starting interfacing more with their clients. One dataset contains information about the clients and the other one contains information about their financial details.

The company now needs a dataset containing the emails of the clients from the United Kingdom and the Netherlands and some of their financial details to starting reaching out to them for a new marketing push.

Since all the data in the datasets is fake and this is just an exercise, one can forego the issue of having the data stored along with the code in a code repository.

You can use any library to finish the task, however, using Pandas is a plus.

## TODOs:
- [x] Use latest Python **3.x**
- [x] Only use clients from the United Kingdom or the Netherlands.
- [x] Remove personal identifiable information from the first dataset, **excluding emails**.
- [x] Remove credit card number from the second dataset.
- [x] Data should be joined using the **id** field.
- [x] Rename the columns for the easier readability to the business users:
    Old name|New name
    --|--
    id|client_identifier
    btc_a|bitcoin_address
    cc_t|credit_card_type
- [x] The project should be stored in GitHub.
- [x] Save the output in a client_data directory in the root directory of the project.
- [x] Add a README file explaining on a high level what the application does.
- [x] Application should receive three arguments, the paths to each of the dataset files and also the countries to filter as the client wants to reuse the code for other countries.
- [x] Use logging.
- [x] If possible, have different branches for different tasks that once completed are merged to the main branch. Follow the GitHub flow - https://guides.github.com/introduction/flow/.

### BONUS
- [x] Implement solution in one of the Python frameworks (REST API where the final file should be downloadable): Flask, Django or FastAPI
- [x] Add unit test to a project
- [x] Log to a file with a rotating policy.
- [ ] Code should be able to be packaged into a source distribution file.
- [x] Requirements file should exist.
- [x] Document the code with docstrings as much as possible
- [x] Dockerize the project
