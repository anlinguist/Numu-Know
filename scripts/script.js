var el = document.querySelector('#nav-icon4');

el.onclick = function() {
  el.classList.toggle('open');
}
            
const firebaseUI = new firebaseui.auth.AuthUI(firebase.auth());


/**
 * Firebase Authentication configuration
 */
const firebaseUiConfig = {
  callbacks: {
    signInSuccessWithAuthResult: function (authResult, redirectUrl) {
      // User successfully signed in.
      // Return type determines whether we continue the redirect automatically
      // or whether we leave that to developer to handle.
                return false;
    },
    uiShown: () => {
    },
  },
  signInFlow: 'popup',
  signInSuccessUrl: '/',
  signInOptions: [
    firebase.auth.GoogleAuthProvider.PROVIDER_ID
  ],
  credentialHelper: firebaseui.auth.CredentialHelper.NONE,
};



firebase.auth().onAuthStateChanged((firebaseUser) => {
  if (firebaseUser) {
    currentUser = firebaseUser.uid;
    currentUserName = firebaseUser.displayName
    currentUserEmail = firebaseUser.email
    signoutbtn = document.createElement("button")
    document.querySelector('#firebaseui-auth-container').append(signoutbtn)
    signoutbtn.append("Sign Out")
    signoutbtn.setAttribute("id", "signout")
    document.getElementById("signout").addEventListener('click', function() {
        signoutbtn.remove();
        firebase.auth().signOut();
    })
    startUp(currentUser)
  } else {
      currentUser = ""
      startUp(currentUser)
    firebaseUI.start('#firebaseui-auth-container', firebaseUiConfig);
  }
});


function addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus) {  
    attpanelcontainer = document.createElement("div")
    document.getElementById('attpanelcontainer').replaceWith(attpanelcontainer)
    attpanelcontainer.setAttribute("id", "attpanelcontainer")
    dc = {}
    console.log(userstatus)
    for (var key in wordObj) {
        // check if the property/key is defined in the object itself, not in parent
            attribute = key
            value = wordObj[key].replace(".", "").replace('”', "").replace(",", "").replace('“', "").replace("?", "")
            randomp = document.createElement('p')
            valueSpan = document.createElement('span')
            document.getElementById('attpanelcontainer').append(randomp)
            randomp.setAttribute("class", "att-item")
            randomp.setAttribute("id", "att-" + attribute)
            randomp.append(attribute + ": ")
            randomp.append(valueSpan)
            valueSpan.setAttribute("class", "wordatt-value")
            valueSpan.append(value)
            if (currentUser !== "" && userstatus == "owner") {
                valueSpan.contentEditable='true'
            }
            dc[key] = wordObj[key] 
    }
    addattdiv = document.createElement("div")
    attpanelcontainer.append(addattdiv)
    addattdiv.setAttribute("id", "addattbtndiv")

    addattbtn = document.createElement("button")
    addattdiv.append(addattbtn)
    addattbtn.setAttribute("id", "add-att")
    addattbtn.append("Add Attribute")

    // document.getElementById('add-att').addEventListener('click', function(event){


    // })


    document.getElementById('attpanelcontainer').addEventListener('focusout', async function(event) {
        if (event.target.matches('.wordatt-value')) {
            attChanged = event.target.parentElement.id.replace("att-", "")
            if (event.target.innerHTML != dc[attChanged].replace(".", "").replace('”', "").replace(",", "").replace('“', "").replace("?", "")) {
                anobject[sentenceNum]['words'][wordNum][attChanged] = event.target.innerHTML
                send = {
                        'data': anobject
                    }
                let postInfo = {
                    method: 'PUT',
                    headers: {
                      'Content-Type': 'application/json',
                      'Document': docName,
                      'uid': currentUser
                    },
                    body: JSON.stringify(send)
                  }
                  
                  url = "https://us-central1-numu-know.cloudfunctions.net/app/api/update/1"
                  fetch(url, postInfo).then(populateMain(anobject, docName, currentUser))
                
                }                
            }
      });


}

function clickedWord(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus) {
    removeAllChildNodes(document.getElementById('attpanelcontainer'))
    w = document.getElementById('att-panel').clientWidth
    h = document.getElementById('att-panel').clientHeight
    mw = document.body.clientWidth
    if (mw > 690) {
        if (w === 0) {
            //slide att-panel into view.
            setTimeout(function(){ 
                attitems = document.querySelectorAll('.att-item')
                attitems.forEach(item => {
                    item.style.whiteSpace = "normal"
                })}, 500);
            document.getElementById('att-panel').style.animation = "animate .5s linear forwards";
            //for each attribute in wordObj, make a child of attpanelcontainer with the name of attribute: value of attribute
            addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus)
            
        }
        else {
            //don't expand, just fade in new word
            addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus)
            attitems = document.querySelectorAll('.att-item')
                attitems.forEach(item => {
                    item.style.whiteSpace = "normal"
                })
        }
    }
    else {
        if (h === 0) {
            //slide att-panel into view.
            setTimeout(function(){ 
                attitems = document.querySelectorAll('.att-item')
                attitems.forEach(item => {
                    item.style.whiteSpace = "normal"
                    document.getElementById('att-panel').style.display = "block";
                })}, 500);
            document.getElementById('att-panel').style.animation = "showatts .5s linear forwards";
            //for each attribute in wordObj, make a child of attpanelcontainer with the name of attribute: value of attribute
            addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus)
            
        }
        else {
            //don't expand, just fade in new word
            addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus)
            attitems = document.querySelectorAll('.att-item')
                attitems.forEach(item => {
                    item.style.whiteSpace = "normal"
                })
        }
    }

}

async function populateMain(anobject, docName, currentUser) {
    maindiv = document.createElement("div")
    document.getElementById('main').replaceWith(maindiv)
    maindiv.setAttribute("id", "main")
    i=0
    dictionary = {}
    doctitle = document.createElement("h2")
    document.getElementById("main").append(doctitle)
    doctitle.append(docName)
    // doccontainer = document.createElement("div")
    // document.getElementById('doc-container').replaceWith(doccontainer)
    // doccontainer.setAttribute("id", "doc-container")

    let postInfo = {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Document': docName,
          'uid': currentUser
        }
      }
    userstatus = await fetch('https://us-central1-numu-know.cloudfunctions.net/app/api/userstatus', postInfo).then(response => response.text())
    .then(function(data){ return data})

    anobject.forEach(function(item) {
        i+=1
        sentence = document.createElement("p");
        document.getElementById("main").append(sentence)
        idname = "sentence" + i
        sentence.setAttribute("id", idname)

        if (item.words != undefined) {
            words = item.words
            ws = 0
            words.forEach(function(iword) {
                ws +=1
                theword = iword.word
                morphology = iword.morphemes
                gloss = iword.gloss
                wordspan = document.createElement("span");
                document.getElementById(idname).append(wordspan)
                wid = idname + "word" + ws
                wordatts = {}
                dictionary[wid] = wordatts
                wordatts["word"] = theword
                wordatts["morphology"] = morphology
                wordatts["gloss"] = gloss
                for (key in iword) {
                    if (key !== "word" && key !== "morphemes" && key !== "gloss") {
                        wordatts[key] = iword[key]
                    }
                }
                wordspan.setAttribute("id", wid)
                wordspan.setAttribute("class", "iword")
                document.getElementById(wid).append(theword + " ")
            })
        }
        else if (item.block) {
            block = document.createElement("p")
            document.getElementById(idname).append(block)
            block.append(item.block)
            block.setAttribute("class", "blockedsentence")
        }
        translation = item.translation
        let t = document.createElement("p")
        tidname = "translation" + i
        document.getElementById("main").append(t)
        t.setAttribute("id", tidname)
        t.setAttribute("class", "translation")
        document.getElementById(tidname).append(translation)
    })
    document.getElementById('main').addEventListener('click', function (event) {
        if (event.target.matches('.iword')) {
            idOfClicked = event.target.id
            sentenceNum = parseInt(idOfClicked.replace("sentence", "").replace(/word.*/, "")) - 1
            wordNum = parseInt(idOfClicked.replace(/sentence.*word/, "")) - 1
            wordObj = dictionary[event.target.id];
            clickedWord(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus)
        }
    })
    var old_element = document.getElementById("doc-container");
    var new_element = old_element.cloneNode(true);
    old_element.parentNode.replaceChild(new_element, old_element);
    document.getElementById('doc-container').addEventListener('click', function (event) {
        if (event.target.matches('.documentitem')) {
            console.log('populating')
            idofdoc = event.target.id
            idtopopulate = parseInt(idofdoc.replace("item", ""))
            fetch('https://us-central1-numu-know.cloudfunctions.net/app/api/read')
            .then(response => response.json())
            .then(data => populateMain(data[idtopopulate]['item']['item']['data'], data[idtopopulate]['id'], currentUser));
        }
    })
}

function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

function populateSideBar(item, index) {
        i = index
        itemName = item['id']
        itemID = "item" + i
        item = document.createElement("div");
        document.getElementById("doc-container").append(item)
        item.setAttribute("id", itemID)
        item.setAttribute("class", "documentitem")
        document.getElementById(itemID).append(itemName)
}

function toggleSideBar() {
    console.log('toggled')
    w = document.getElementById('doc-panel').clientWidth
    if (w === 0) {
        document.getElementById('doc-panel').style.animation = "animate .5s linear forwards";
        removeAllChildNodes(document.getElementById('doc-container'))
        fetch('https://us-central1-numu-know.cloudfunctions.net/app/api/read')
        .then(response => response.json())
        .then(function(data) {
            data.forEach(function(item, index) {
            populateSideBar(item, index);
            })              
        })
    }
    else {
        document.getElementById('doc-panel').style.animation = "deanimate .5s linear backwards";
    }
}

function startUp(currentUser) {
    fetch('https://us-central1-numu-know.cloudfunctions.net/app/api/read')
  .then(response => response.json())
  .then(function(data) {populateMain(data[0]['item']['item']['data'], data[0]['id'], currentUser)});
}


document.getElementById('nav-icon4').addEventListener('click', function() {toggleSideBar()}, false)
document.getElementById('exit-panel').addEventListener('click', function() {
    attitems = document.querySelectorAll('.att-item')
            attitems.forEach(item => {
                item.style.whiteSpace = "nowrap"
            })
            mw = document.body.clientWidth
    if (mw > 690) {
        document.getElementById('att-panel').style.animation = "deanimate .5s linear backwards";
    }
    else {
        document.getElementById('att-panel').style.animation = "removeatts .5s linear backwards";
    }
        }, false)

// add a loader to documents list and main document holder

