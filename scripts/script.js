let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`)

window.addEventListener('resize', () => {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`)
})


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
    for (var key in wordObj) {
        if (!key.startsWith('variant-')) {
        // check if the property/key is defined in the object itself, not in parent
            attribute = key
            value = wordObj[key]
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
    }
    addattdiv = document.createElement("div")
    attpanelcontainer.append(addattdiv)
    addattdiv.setAttribute("id", "addattbtndiv")

    if (currentUser !== "" && userstatus == "owner") {
    addattbtn = document.createElement("button")
    addattdiv.append(addattbtn)
    addattbtn.setAttribute("id", "add-att")
    addattbtn.append("Add Attribute")

    document.getElementById('add-att').addEventListener('click', function(event) {

        attCapture = document.createElement("div")
        addattbtn.replaceWith(attCapture)
        acName = document.createElement("div")
        attCapture.append(acName)
        attCapture.setAttribute("id", "newattbuilder")
        acName.setAttribute("id", "acName")
        document.getElementById("acName").style.animation = "grow-font .5s linear forwards"
        labelDiv = document.createElement("div")
        attCapture.append(labelDiv)
        labelDiv.setAttribute("id", "acNameLabel")
        document.getElementById("acNameLabel").style.animation = "grow .5s linear forwards"
        acNameInput = document.createElement("input")
        acName.append(acNameInput)
        acNameInput.setAttribute("id", "acNameInput")
        acNameInput.select()
        document.getElementById("acNameInput").style.animation = "grow .5s linear forwards"
        labelDiv.append("Name this attribute")

        canceladdatt = document.createElement("div")
        acName.append(canceladdatt)
        canceladdatt.setAttribute("id", "canceladdatt")
        canceladdatt.append("×")

        confirmaddatt = document.createElement("div")
        acName.append(confirmaddatt)
        confirmaddatt.setAttribute("id", "confirmaddatt")
        confirmaddatt.append("✓")

        document.getElementById('canceladdatt').addEventListener('click', function(event) {
            document.getElementById("acName").style.animation = "degrow-font .5s linear forwards"
            document.getElementById("acNameLabel").style.animation = "degrow .5s linear forwards"
            try{
                document.getElementById("acNameInput").style.animation = "degrow .5s linear forwards"
            }
            catch {
                document.getElementById("acAttInput").style.animation = "degrow .5s linear forwards"
            }
            setTimeout(function(){ 
                attCapture.replaceWith(addattbtn)
            }, 500)
        })
        document.getElementById('confirmaddatt').addEventListener('click', function(event) {
            handleAddAtt(anobject, sentenceNum, wordNum, docName, currentUser, userstatus, wordObj)
        })
        document.getElementById('acNameInput').addEventListener('keydown', function(e) {
            if (e.key === "Enter") {
                e.preventDefault();
                handleAddAtt(anobject, sentenceNum, wordNum, docName, currentUser, userstatus, wordObj)
            }
        }, false)



    })
}

    // document.getElementById('add-att').addEventListener('click', function(event){


    // })
    document.getElementById('attpanelcontainer').addEventListener('keydown', function(e) {
        if (e.target.matches('.wordatt-value')) {
        if (e.key === "Enter") {
            e.preventDefault();
        }
    }
    }, false)

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

function handleAddAtt(anobject, sentenceNum, wordNum, docName, currentUser, userstatus, wordObj) {
    attname = document.getElementById('acNameInput').value
    if (attname == "") {
        return
    }
    else {
        document.getElementById("acNameLabel").innerHTML = "Give " + attname + " a value"
        acAttInput = document.createElement("input")
        document.getElementById('acNameInput').replaceWith(acAttInput)
        acAttInput.setAttribute("id", "acAttInput")
        acAttInput.select()

        confirmaddattvalue = document.createElement("div")
        document.getElementById("confirmaddatt").replaceWith(confirmaddattvalue)
        confirmaddattvalue.setAttribute("id", "confirmaddattvalue")
        confirmaddattvalue.append("✓")

        document.getElementById("confirmaddattvalue").addEventListener("click", function(e) {
            attributevalue = document.getElementById('acAttInput').value

            anobject[sentenceNum]['words'][wordNum][attname] = document.getElementById('acAttInput').value
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
                  wordObj[attname] = attributevalue
                  addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus)
                  attitems = document.querySelectorAll('.att-item')
                      attitems.forEach(item => {
                          item.style.whiteSpace = "normal"
                      })

        })

        document.getElementById("acAttInput").addEventListener('keydown', function(enterevent) {
            if (enterevent.key === "Enter") {
                enterevent.preventDefault();
                attributevalue = document.getElementById('acAttInput').value

                anobject[sentenceNum]['words'][wordNum][attname] = document.getElementById('acAttInput').value
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
                  wordObj[attname] = attributevalue
                  addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj, currentUser, userstatus)
                  attitems = document.querySelectorAll('.att-item')
                      attitems.forEach(item => {
                          item.style.whiteSpace = "normal"
                      })

            }
        }, false)
    }
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


varSelected = ""
async function populateMain(anobject, docName, currentUser) {
    maindiv = document.createElement("div")
    document.getElementById('main').replaceWith(maindiv)
    maindiv.setAttribute("id", "main")

    titleDiv = document.createElement("div")
    document.getElementById("main").append(titleDiv)
    titleDiv.setAttribute("id", "titleDiv")
    i=0
    dictionary = {}
    doctitle = document.createElement("h2")
    doctitle.setAttribute("id", "doctitle")
    document.getElementById("titleDiv").append(doctitle)
    doctitle.append(docName)
    // if () {

    // }
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

    varArr = []
    anobject.forEach(function(item) {
        i+=1
        sentence = document.createElement("p");
        document.getElementById("main").append(sentence)
        idname = "sentence" + i
        sentence.setAttribute("id", idname)

        if (item.words != undefined) {
            words = item.words
            ws = 0
            words.forEach(function(iword, index) {
                for (key in iword) {
                    if (key.startsWith('variant-')) {
                        multipleVars = true
                        if (!varArr.includes(key)) {
                            varArr.push(key)
                        }
                    }
                }
                if ("punctuation" in iword) {
                    ws +=1
                    theword = iword.punctuation
                    wordspan = document.createElement("span");
                    document.getElementById(idname).append(wordspan)
                    wid = idname + "word" + ws
                    wordspan.setAttribute("id", wid)
                    wordspan.className += " iword";
                    wordspan.className += " punctuation";
                    //need to test for front punctuation
                    //if the the item contains "left-quote", do not add space
                    //else, add space
                    if (words[index+1] !== undefined) {
                        if (words[index+1]["punctuation"] === "." ||
                            words[index+1]["punctuation"] === "?" ||
                            words[index+1]["punctuation"] === "!" ||
                            words[index+1]["punctuation"] === "," ||
                            words[index+1]["punctuation"] === "”"
                        ) {
                            document.getElementById(wid).append(theword)
                        }
                        else {
                            if (theword === "“") {
                                document.getElementById(wid).append(theword)
                            }
                            else {
                                document.getElementById(wid).append(theword + " ")
                            }
                        }
                    }
                    else {
                    document.getElementById(wid).append(theword + " ")

                }}
                else {
                    ws +=1
                    if (varSelected == "") {
                        theword = iword.word
                    }
                    else {
                        if (varSelected in iword) {
                            theword = iword[varSelected]
                        }
                        else {
                            theword = iword.word
                        }
                    }
                    morphology = iword.morphemes
                    gloss = iword.gloss
                    wordspan = document.createElement("span");
                    document.getElementById(idname).append(wordspan)
                    wid = idname + "word" + ws
                    wordatts = {}
                    dictionary[wid] = wordatts
                    wordatts["word"] = iword.word
                    wordatts["morphology"] = morphology
                    wordatts["gloss"] = gloss
                    for (key in iword) {
                        if (key !== "word" && key !== "morphemes" && key !== "gloss") {
                            wordatts[key] = iword[key]
                        }
                    }
                    wordspan.setAttribute("id", wid)
                    wordspan.setAttribute("class", "iword")

                    if (words[index+1] !== undefined) {
                    if (words[index+1]["punctuation"] === "." ||
                        words[index+1]["punctuation"] === "?" ||
                        words[index+1]["punctuation"] === "!" ||
                        words[index+1]["punctuation"] === "," ||
                        words[index+1]["punctuation"] === "”"
                    ) {
                        document.getElementById(wid).append(theword)
                    }
                    else {
                        document.getElementById(wid).append(theword + " ")
                    }
                }
                else {
                    document.getElementById(wid).append(theword)
                }
                }
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
    if (varArr.length>0) {
        customSelectWrapper = document.createElement('div')
        doctitle.after(customSelectWrapper)
        customSelectWrapper.setAttribute("class", "custom-select-wrapper")

        customSelect = document.createElement('div')
        customSelectWrapper.append(customSelect)
        customSelect.setAttribute("class", "custom-select")

        customSelectTrigger = document.createElement('div')
        customSelect.append(customSelectTrigger)
        customSelectTrigger.setAttribute("class", "custom-select__trigger")

        defaultSpan = document.createElement("span")
        customSelectTrigger.append(defaultSpan)
        defaultSpan.append("default")

        arrowDiv = document.createElement("div")
        customSelectTrigger.append(arrowDiv)
        arrowDiv.setAttribute("class", "arrow")

        customOptions = document.createElement("div")
        customSelect.append(customOptions)
        customOptions.setAttribute("class", "custom-options")

        defaultVariant = document.createElement('span')
        customOptions.append(defaultVariant)
        defaultVariant.setAttribute("data-value", "default")
        if (varSelected == "") {
            defaultVariant.setAttribute("class", "custom-option selected")
            document.querySelector('.custom-select__trigger span').textContent = "default";
        }
        else {
            defaultVariant.setAttribute("class", "custom-option")
        }
        defaultVariant.append("default")

        for (variant in varArr) {
            varOption = document.createElement('span')
            customOptions.append(varOption)
            varOption.setAttribute("data-value", varArr[variant])
            varOption.setAttribute("class", "custom-option")
            varOption.append(varArr[variant])
            if (varSelected != "") {
                if (varArr[variant] == varSelected) {
                    varOption.setAttribute("class", "custom-option selected")
                    document.querySelector('.custom-select__trigger span').textContent = varSelected;
                }
                else {
                    varOption.setAttribute("class", "custom-option")
                }
            }
            else {
                varOption.setAttribute("class", "custom-option")
            }
        }




        document.querySelector('.custom-select-wrapper').addEventListener('click', function() {
            this.querySelector('.custom-select').classList.toggle('ddopen');
        })
        for (const option of document.querySelectorAll(".custom-option")) {
            option.addEventListener('click', function() {
                if (!this.classList.contains('selected')) {
                    this.parentNode.querySelector('.custom-option.selected').classList.remove('selected');
                    this.classList.add('selected');
                    this.closest('.custom-select').querySelector('.custom-select__trigger span').textContent = this.textContent;
                    selected_option = this.textContent
                    if (selected_option == "default") {
                        varSelected = ""
                    }
                    else {
                        varSelected = selected_option
                    }
                    populateMain(anobject, docName, currentUser)
                }
            })
        }
        
        window.addEventListener('click', function(e) {
            const select = document.querySelector('.custom-select')
            try{
            if (!select.contains(e.target)) {
                select.classList.remove('ddopen');
            }
        }
        catch {

        }
        });

    }
    
    document.getElementById('main').addEventListener('click', function (event) {
        if (event.target.matches('.iword') && !event.target.matches('.punctuation')) {
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
            idofdoc = event.target.id
            idtopopulate = parseInt(idofdoc.replace("item", ""))
            varSelected = ""
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

