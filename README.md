# Adoption Agency Project

## Initialize Project
    $ pip install
    
## Start DB
    $ psql pet-database
## Stop DB
    $ \q

## Seed Database
    $ psql -d pet_database -a -f pets.sql   

## Installing Flask SQL Alchemy
    $ pip install psycopg2-binary
    $ pip install flask-sqlalchemy

## Start Server
    $ flask run

## To Do
1. Make Homepage Listing Pets
   - name
   - show photo, if present
   - display “Available” in bold if the pet is
   - available for adoption
2. Add a link to the homepage (/add)
3. Create Handler for Add Pet Form
    - This should validate the form:
    - on invalide, re-render the form
    - valide, create the new pet, redirect to '/'
    - should be POST request to path '/add'
4. Add Validation
   - WTForms gives us lots of useful validators; we want to use these for validating our fields more carefully:
   - species should be [“cat”, “dog”, “porcupine”]
   - Photo URL must be a URL (But still optional)
   - age between 0 and 30, if provided
5. Add Display/Edit Form
    - Make a page that shows some information about the pet:
      - Name
      - Species
      - Photo, if present
      - Age, if present
    - Show a form that allows us to edit this pet:
         - Photo URL
         - Notes
         - Available
         - Should be a GET to /[pet-id-number]. Make the pet card on homepage link to this.
6. Handle Edit Form
    - This should validate the form:
    - invalide, re-render the form
    - valide,edit the pet
    - Should be a POST request to the URL path /[pet-id-number].




