function addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj) {  
    attpanelcontainer = document.createElement("div")
    document.getElementById('attpanelcontainer').replaceWith(attpanelcontainer)
    attpanelcontainer.setAttribute("id", "attpanelcontainer")
    dc = {}
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
            valueSpan.contentEditable='true'
            dc[key] = wordObj[key] 
    }



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
                      'Document': docName
                    },
                    body: JSON.stringify(send)
                  }
                  
                  url = "http://localhost:5001/numu-know/us-central1/app/api/update/1"
                  fetch(url, postInfo).then(populateMain(anobject, docName))
                
                }                
            }
      });


}

function clickedWord(anobject, docName, sentenceNum, wordNum, wordObj) {
    removeAllChildNodes(document.getElementById('attpanelcontainer'))
    w = document.getElementById('att-panel').clientWidth
    if (w === 0) {
        //slide att-panel into view.
        document.getElementById('att-panel').style.animation = "animate .5s linear forwards";
        //for each attribute in wordObj, make a child of attpanelcontainer with the name of attribute: value of attribute
        addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj)
    }
    else {
        //don't expand, just fade in new word
        addAllTheAttsToContainer(anobject, docName, sentenceNum, wordNum, wordObj)
    }
}

function populateMain(anobject, docName) {
    maindiv = document.createElement("div")
    document.getElementById('main').replaceWith(maindiv)
    maindiv.setAttribute("id", "main")
    i=0
    dictionary = {}
    doctitle = document.createElement("h2")
    document.getElementById("main").append(doctitle)
    doctitle.append(docName)
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
            clickedWord(anobject, docName, sentenceNum, wordNum, wordObj)
        }
    })
    document.getElementById('doc-container').addEventListener('click', function (event) {
        if (event.target.matches('.documentitem')) {
            idofdoc = event.target.id
            idtopopulate = parseInt(idofdoc.replace("item", ""))
            fetch('https://us-central1-numu-know.cloudfunctions.net/app/api/read')
            .then(response => response.json())
            .then(data => populateMain(data[idtopopulate]['item']['item']['data'], data[idtopopulate]['id']));
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

function toogleSideBar() {
    w = document.getElementById('doc-panel').clientWidth
    if (w === 0) {
        document.getElementById('doc-panel').style.animation = "animate .5s linear forwards";
        removeAllChildNodes(document.getElementById('doc-container'))
        fetch('https://us-central1-numu-know.cloudfunctions.net/app/api/read')
        .then(response => response.json())
        .then(data => data.forEach(function(item, index) {populateSideBar(item, index)}));
    }
    else if (w===250) {
        document.getElementById('doc-panel').style.animation = "deanimate .5s linear backwards";
    }
}

function startUp() {
    fetch('https://us-central1-numu-know.cloudfunctions.net/app/api/read')
  .then(response => response.json())
  .then(data => populateMain(data[0]['item']['item']['data'], data[0]['id']));
}

startUp()

document.getElementById('doc-toggler').addEventListener('click', function() {toogleSideBar()}, false)
document.getElementById('exit-panel').addEventListener('click', function() {document.getElementById('att-panel').style.animation = "deanimate .5s linear backwards";}, false)

// add a loader to documents list and main document holder