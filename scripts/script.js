function addAllTheAttsToContainer(wordObj) {
    theword = wordObj["word"].replace(".", "").replace('”', "").replace(",", "").replace('“', "").replace("?", "")
        themorphology = wordObj["morphology"]
        thegloss = wordObj["gloss"]
        wordp = document.createElement('p')
        morphp = document.createElement('p')
        glossp = document.createElement('p')
        document.getElementById('attpanelcontainer').append(wordp)
        document.getElementById('attpanelcontainer').append(morphp)
        document.getElementById('attpanelcontainer').append(glossp)
        wordp.setAttribute("class", "att-item")
        morphp.setAttribute("class", "att-item")
        glossp.setAttribute("class", "att-item")
        wordp.append("Word: " + theword)
        morphp.append("Morphology: " + themorphology)
        glossp.append("Gloss: " + thegloss)
        for (var key in wordObj) {
            // check if the property/key is defined in the object itself, not in parent
            if (key !== "word" && key !== "morphology" && key !== "gloss") {
                console.log("extrakey found")
                attribute = key
                value = wordObj[key]
                randomp = document.createElement('p')
                document.getElementById('attpanelcontainer').append(randomp)
                randomp.setAttribute("class", "att-item")
                randomp.append(attribute + ": " + key)
            }
        }
}

function clickedWord(wordObj) {
    removeAllChildNodes(document.getElementById('attpanelcontainer'))
    w = document.getElementById('att-panel').clientWidth
    console.log(wordObj)
    if (w === 0) {
        //slide att-panel into view.
        document.getElementById('att-panel').style.animation = "animate .5s linear forwards";
        //for each attribute in wordObj, make a child of attpanelcontainer with the name of attribute: value of attribute
        addAllTheAttsToContainer(wordObj)
    }
    else {
        //don't expand, just fade in new word
        addAllTheAttsToContainer(wordObj)
    }
}

function populateMain(anobject, docName) {
    removeAllChildNodes(document.getElementById('main'))
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
            sentence=sentence + item.block + " "
        }
        translation = item.translation
        let t = document.createElement("p")
        tidname = "translation" + i
        document.getElementById("main").append(t)
        t.setAttribute("id", tidname)
        t.setAttribute("class", "translation")
        document.getElementById(tidname).append(translation)
    })
    document.addEventListener('click', function (event) {
        if (event.target.matches('.iword')) {
            console.log(event.target.id)
            idOfClicked = event.target.id
            sentenceNum = parseInt(idOfClicked.replace("sentence", "").replace(/word.*/, "")) - 1
            wordNum = parseInt(idOfClicked.replace(/sentence.*word/, "")) - 1
            console.log(sentenceNum)
            console.log(wordNum)
            wordObj = dictionary[event.target.id];
            clickedWord(wordObj)
        }
        if (event.target.matches('.documentitem')) {
            idofdoc = event.target.id
            idtopopulate = parseInt(idofdoc.replace("item", ""))
            console.log(idofdoc)
            console.log(idtopopulate)
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
        console.log('animating...')
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