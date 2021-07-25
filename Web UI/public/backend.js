let myData = {};

const history = document.getElementById('history-btn');
history.addEventListener('click', showHistory);

async function showHistory(){
  console.log("Call the History function !");
          
  await fetch("https://teamop.winoff.ml/history").then(function(response) {
    response.json().then( data => {
        console.log(data);
        let tableRef = document.getElementById('table-body');
        
        while(tableRef.rows.length > 0)
        {
            tableRef.deleteRow(0);
        }
        myData = data;
        printAllData();
    })
  });
}

async function getResponseFromAPI()
{
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://teamop.winoff.ml/users');
    // xhr.responseType = 'json';
    xhr.setRequestHeader('Access-Control-Allow-Origin', 'https://teamop.winoff.ml');
    xhr.setRequestHeader('Access-Control-Allow-Methods', 'GET, POST');
    xhr.send();
    xhr.onload = function() {
        if (xhr.status != 200) {
          alert(`Error ${xhr.status}: ${xhr.statusText}`);
        } 
      };
      
      xhr.onprogress = function(event) {
            myData = JSON.parse(this.response);
            console.log("Successfully Fetched Data !");
            console.log(myData);
            printAllData();
      };

      xhr.onerror = function() {
        console.log("Request Failed to load! Source Down");
      }
}

async function printAllData()
{
  let tableRef = document.getElementById('table-body');

  for(let row = 0; row < myData['data'].length; row++)
  {
    let newRow = tableRef.insertRow(-1);

    for(let cols = 0; cols < 7; cols++)
    {
        let newCell = newRow.insertCell(cols);
        let key = Object.keys(myData['data'][row])[cols]
        let newText = document.createTextNode(myData['data'][row][key]);
        newCell.appendChild(newText);
    }
  }
}

getResponseFromAPI();

document.getElementById("id_of_textbox")
    .addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
      let search = document.getElementById("id_of_textbox")
      if(search.value.length > 2)
      {
          console.log("Call the search function !");
          
          fetch(`/data?search=${search.value}`).then(function(response) {
            response.json().then( data => {
                console.log(data);
                let tableRef = document.getElementById('table-body');
                
                while(tableRef.rows.length > 0)
                {
                    tableRef.deleteRow(0);
                }
                
                myData = data;
                
                  let newRow = tableRef.insertRow(-1);
              
                  for(let row = 0; row < myData.length; row++)
                  {
                    let newRow = tableRef.insertRow(-1);

                    for(let cols = 0; cols < 7; cols++)
                    {
                        let newCell = newRow.insertCell(cols);
                        let key = Object.keys(myData[row])[cols];
                        let newText = document.createTextNode(myData[row][key]);
                        newCell.appendChild(newText);
                    }
                  }
            })
          });
      }
      else
      {
        console.log("Provide atleast 3 chars");
        let tableRef = document.getElementById('table-body');
        while(tableRef.rows.length > 0)
                  {
                      tableRef.deleteRow(0);
                  }
        getResponseFromAPI();
    }
    }
});