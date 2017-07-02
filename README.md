## xml to csv script
This is an xml scraper that injests an xml workbook file and generates a `csv` file for each `worksheet`.

It was written to process data downloads from Facebook pages, so it can probably be used for that purpose with minimal editing.

Python 3.5, beautifulsoup 4.5.3, and iso8601utils 0.1.2 were used for this project.


#### XML files

For the code to work on your xml file as-is, your xml will need a data hierarchy with tags as follows:

-- tag called `workbook` with an `ss:name` attribute, e.g.: `<Worksheet ss:Name="Sample Worksheet">`
  
  --- tag called `table` with an `ss:expandedcolumncount` attribute, e.g. `<Table ss:ExpandedColumnCount="19" ss:ExpandedRowCount="125" x:FullColumns="1">`
  
  ---- tag called `data` with an `ss:type=` attribute that can be equal to `string`, `datetime` or `number`, e.g. `<Data ss:Type="String">`
  
 If your tags don't match these, simply do a find and replace to update them. If the hierarchy doesn't match, you can work around it, but it will involve moving and modifying some lines of code.

The `iso8601utils` requirement is there to support dates in ISO format, like this (note the "T"): `2015-12-02T15:59:44.000` and converts it to a Python datetime object.  If you don't want this functionality, you can edit the code where `DateTime` types are handled in the file.


#### How to run the code
You should have Python 3+ installed on your computer.

From the command line/terminal:
- Create a Python3 virtualenv `python3 -m venv xml2csv` (but you can change ` xml2csv` to whatever you want 😉)
- Activate your virtualenv
- Install the requirements `pip install -r requirements.txt`
- Add the path to your file(s) in the `filenames` list on line 6 of `writecsv.py`
- Modify the code as needed based on the structure and contents of your file as outlined above
- Run the code `python writecsv.py`

### Enjoy your data!  📊 🤓

