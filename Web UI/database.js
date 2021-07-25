const { MongoClient } = require("mongodb");

// Replace the uri string with your MongoDB deployment's connection string.
const uri ="mongodb+srv://admin:admin@cluster0.ga47f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

const client = new MongoClient(uri);

async function _run() {
  try {
    await client.connect();

    const database = client.db("sample_analytics");
    const movies = database.collection("scans");
    const options = { projection: { _id: 0, "Connection Type":1, "Hostname":1, "MAC-Address":1, 
      "IP":1, "Operating System":1, "Last Seen":1, "Workgroup/Domain":1 }};

    let keyArray =  ["Connection Type", "Hostname", "MAC-Address", "IP", "Operating System", "Last Seen", "Workgroup/Domain"]; 

    for(let i = 0; i < keyArray.length; i++) {
      let key = keyArray[i];
      let str = "arsenal";

      var query = { key : str };                  //Need a variable key here
      // var query = { Hostname : "arsenal" };  //Sample wwhich works fine without variable key
      
      const cursor = movies.find(query, options);
      if ((await cursor.count()) === 0) {
        // console.log("No documents found!");
      }
      else {
          await cursor.forEach(console.dir);
          return;
      }
    }
   
  } finally {
    await client.close();
  }
}

async function run(str) {
  try {
    await client.connect();

    const database = client.db("sample_analytics");
    const movies = database.collection("scans");
    const options = { projection: { _id: 0, "Connection Type":1, "Hostname":1, "MAC-Address":1, 
      "IP":1, "Operating System":1, "Last Seen":1, "Workgroup/Domain":1 }};

    // let str = "10.0.0.5";
    let keyArray =  [{ "Connection Type" : str } ,{ "Hostname" : str }, { "MAC-Address" : str }, { "IP" : str } , { "Operating System" : str }, { "Last Seen" : str }, { "Workgroup/Domain" : str }]; 

    for(let i = 0; i < keyArray.length; i++) {
      let query = keyArray[i];

      const cursor = movies.find(query, options);
      if ((await cursor.count()) === 0) {
        // console.log("No documents found!");
      }
      else {
          var array = [];
          await cursor.forEach(function(doc) {
            array.push(doc)
            }).then(() => {
              // console.dir(array)
              });
          return array;
      }
    }
   
  } finally {
    await client.close();
  }
}

// run();

module.exports = { run };