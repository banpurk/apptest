import webapp2

html = """
<html>
        <head>
                This is a form to pick workload and compliance

        </head>
                <body>
                       <p>Select a compliance from the below options:</p>

        <form id="test" action="datastore" method="post">
                <fieldset id="group1">
                        <input type="radio" name="compliance" onclick="myFunction1(this.value)" id="group1" value="GDPR">GDPR<br>
                        <input type="radio" name="compliance" onclick="myFunction1(this.value)" id="group1" value="PCI">PCI<br>
                        <input type="radio" name="compliance" onclick="myFunction1(this.value)" id="group1" value="HIPAA">HIPAA<br>
                </fieldset>

                        <p>Select a workload from the below options:</p>
                <fieldset id="group2">
                        <input type="radio" name="workload" onclick="myFunction2(this.value)" id="group2" value="DataWarehouse">DataWarehouse<br>
                        <input type="radio" name="workload" onclick="myFunction2(this.value)" id="group2" value="DLP">DLP<br>
                </fieldset>
        </form>
        
        <script>
        function myFunction1(compliance) {
          document.getElementById("result").value = compliance;
        }
        
        function myFunction2(workload) {
          document.getElementById("result").value = workload;
        }
        </script>
                </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.right('html')
    
  def post(self):
    self.response.out.right("Compliance selected: " + compliance 
                           + "Workload selected: " + workload)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
  
