// Week 4 lecture draft deck: neural networks, word embeddings, and getting data.
//
// Figures come from slides/week04_figs.py — the spiral is a real fit, the word vectors
// are trained on the two novels in the repo, the API panel is a live call. Run that
// first; this reads its PNGs and week04_figs.json out of $FIG_DIR (default /tmp/figs).
//
//   python3 slides/week04_figs.py && node slides/week04_deck_build.js
//
// Visual-heavy by design: eleven of the nineteen slides carry a figure.
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");

const F = (process.env.FIG_DIR || "/tmp/figs") + "/";
const facts = JSON.parse(fs.readFileSync(F + "week04_figs.json", "utf8"));
const pct = (x) => `${Math.round(x * 100)}%`;

const pres = new pptxgen();
pres.defineLayout({ name: "W", width: 13.333, height: 7.5 });
pres.layout = "W";
const TERRA="7A3B2E", TERRA_DK="4E261D", INK="1A1A1A", MUTED="6B6B63",
      GREEN="3F6F5F", GOLD="B9852F", BLUE="2E5F8A", TINT="F4EEE8", WHITE="FFFFFF", CREAM="E8DCD6";
const SERIF="Cambria", SANS="Calibri", MONO="Courier New";
const M=0.7;
function base(dark=false){ const s=pres.addSlide(); s.background={color:dark?TERRA_DK:WHITE}; return s; }
function kicker(s,t,c=GOLD){ s.addText(t,{x:M,y:0.55,w:11.5,h:0.35,fontFace:SANS,fontSize:13,bold:true,color:c,charSpacing:3}); }
function title(s,t,c=INK){ s.addText(t,{x:M,y:0.95,w:12,h:0.85,fontFace:SERIF,fontSize:34,bold:true,color:c,valign:"top"}); }
function bullets(s,items,opt={}){
  const o=Object.assign({x:M,y:2.2,w:5.4,h:4.4,fontFace:SANS,fontSize:15,color:INK,valign:"top",lineSpacingMultiple:1.15,paraSpaceAfter:10},opt);
  s.addText(items.map((t,i)=>({text:t,options:{bullet:{code:"2022",indent:12},breakLine:i<items.length-1}})),o);
}
function fig(s,file,x,y,w,h){ s.addImage({path:F+file,x,y,w,h,sizing:{type:"contain",w,h}}); }
function qcards(s,qs,y0=2.2,rh=1.5,fs=15){
  qs.forEach((q,i)=>{
    s.addShape("roundRect",{x:M,y:y0+i*rh,w:11.9,h:rh-0.2,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
    s.addShape("ellipse",{x:M+0.3,y:y0+0.3+i*rh,w:0.35,h:0.35,fill:{color:q[1]},line:{type:"none"}});
    s.addText(q[0],{x:M+0.9,y:y0+0.1+i*rh,w:10.7,h:rh-0.35,fontFace:SERIF,fontSize:fs,italic:true,color:INK,valign:"middle",margin:0});
  });
}
function caption(s,t){ s.addText(t,{x:M,y:6.85,w:11.9,h:0.4,fontFace:SANS,fontSize:11,italic:true,color:MUTED}); }

// 1 title
let s=base(true);
s.addText("CULTURE AS DATA · WEEK 4",{x:M,y:0.7,w:8,h:0.3,fontFace:SANS,fontSize:13,color:GOLD,bold:true,charSpacing:3});
s.addText("How Machines Learn to Read:",{x:M,y:2.0,w:11.5,h:1.0,fontFace:SERIF,fontSize:44,bold:true,color:WHITE});
s.addText("Neural Networks and Word Embeddings",{x:M,y:2.95,w:11.5,h:1.0,fontFace:SERIF,fontSize:44,bold:true,color:CREAM});
s.addText("Your Week 3 classifier is one neuron. Today it grows, learns a map of meaning,\nand then you go and fetch the data you will use it on",
 {x:M,y:4.5,w:10.5,h:1.1,fontFace:SANS,fontSize:17,italic:true,color:CREAM,lineSpacingMultiple:1.25});
[GOLD,GREEN,CREAM].forEach((c,i)=>s.addShape("ellipse",{x:11.3+i*0.42,y:0.62,w:0.22,h:0.22,fill:{color:c},line:{type:"none"}}));

// 2 the arc
s=base(); kicker(s,"TODAY",TERRA); title(s,"Two ideas, then the practical half hour");
[["1","A century, measured","Garg et al.: stereotype change read off an embedding space",TERRA],
 ["2","One neuron, then many","Your classifier, stacked - and what stacking buys and costs",GREEN],
 ["3","Rolling downhill","What training actually is, without the calculus",BLUE],
 ["4","Words as vectors","Where they come from, and what the geometry can do",GOLD],
 ["5","Where a corpus comes from","A file, an API, or a careful scrape",TERRA],
 ["6","Collect and commit","Your data in Drive, your repo born, your project pitched",GREEN]].forEach((st,i)=>{
  const col=i%2,row=Math.floor(i/2),x=M+col*6.2,y=2.15+row*1.55;
  s.addShape("roundRect",{x,y,w:5.9,h:1.3,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addShape("ellipse",{x:x+0.25,y:y+0.33,w:0.62,h:0.62,fill:{color:st[3]},line:{type:"none"}});
  s.addText(st[0],{x:x+0.25,y:y+0.33,w:0.62,h:0.62,fontFace:SERIF,fontSize:20,bold:true,color:WHITE,align:"center",valign:"middle"});
  s.addText(st[1],{x:x+1.05,y:y+0.16,w:4.7,h:0.45,fontFace:SANS,fontSize:16,bold:true,color:INK,margin:0});
  s.addText(st[2],{x:x+1.05,y:y+0.6,w:4.7,h:0.6,fontFace:SANS,fontSize:12.5,color:MUTED,margin:0,valign:"top"});
});

// 3 look at this
s=base(); kicker(s,"LOOK AT THIS",TERRA); title(s,"A century of stereotypes, measured as distance");
bullets(s,["Garg, Schiebinger, Jurafsky and Zou (PNAS 2018): train word vectors on each decade of American text from 1910 on.",
 "The measure: how far do occupation words sit from woman-words versus man-words, decade by decade?",
 "The curve tracks the century - and lines up with census and survey data, which is what makes it evidence rather than a demo.",
 "By the end of today you will know exactly what machinery produced that number."],{w:5.8});
s.addShape("roundRect",{x:6.8,y:2.2,w:5.8,h:3.9,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("the move, in one line",{x:7.1,y:2.45,w:5.2,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
s.addText("distance( occupation , she-words )\n      vs\ndistance( occupation , he-words )",
 {x:7.1,y:2.95,w:5.2,h:1.3,fontFace:MONO,fontSize:14,color:INK,margin:0,lineSpacingMultiple:1.2});
s.addText("Nobody labelled anything. The geometry was already there, in a century of printed text, waiting to be measured.",
 {x:7.1,y:4.4,w:5.2,h:1.5,fontFace:SANS,fontSize:13.5,color:INK,margin:0,valign:"top",lineSpacingMultiple:1.15});
caption(s,"Read before class: abstract, significance statement, figures. Methods skimmed.");

// 4 question it
s=base(); kicker(s,"QUESTION IT",GREEN); title(s,"Before you believe the curve");
qcards(s,[["Whose century is it? Google Books and COHA are what got printed and digitised. Is the shift in the country, or in publishing?",TERRA],
 ["Who chose the words? Someone decided which words count as female and which jobs count as occupations. Where in the paper is that list?",GOLD],
 ["The bias it detects is the bias in the text - the same geometry that makes king - man + woman work. Can you keep one and refuse the other?",GREEN],
 ["What would convince you? Name the check you would want run before repeating this finding out loud.",BLUE]],2.1,1.28,13.5);

// 5 the neuron
s=base(); kicker(s,"IDEA ONE",GREEN); title(s,"You already built a neuron");
fig(s,"w4_neuron.png",M,2.1,7.0,4.4);
bullets(s,["Counts in, one weight each, add them up, squash the total into a probability.",
 "That is Week 3's logistic regression, drawn as a picture.",
 "It is also, exactly, one artificial neuron. Nothing has been added.",
 "The thickness of each line is the size of the weight. You read those yourself last week."],{x:7.9,w:4.7,fontSize:14});

// 6 the network
s=base(); kicker(s,"IDEA ONE",GREEN); title(s,"Stack them and something changes");
fig(s,"w4_network.png",M,2.1,7.0,4.4);
bullets(s,["Put a layer of neurons between the words and the answer.",
 "Each hidden unit learns to fire on some combination of words. Nobody specifies which.",
 "That is the whole trick: features you did not hand-write.",
 "The cost arrives immediately: there is no longer one weight per word to read. Week 7 asks you to accept that knowingly."],{x:7.9,w:4.7,fontSize:14});

// 7 the spiral
s=base(); kicker(s,"WHY IT MATTERS",BLUE); title(s,"Some questions a straight line cannot answer");
fig(s,"w4_spiral.png",M,2.0,8.4,4.6);
bullets(s,[`One neuron: ${pct(facts.spiral_linear)} right. It can only draw a straight line.`,
 `A network with two hidden layers: ${pct(facts.spiral_net)}.`,
 "Same data, same training, more shape available.",
 "TensorFlow Playground, live: watch the hidden units carve the space while it trains."],{x:9.4,w:3.3,fontSize:13.5});
caption(s,"Both models fitted here, on the same points. Nothing drawn by hand.");

// 8 gradient descent
s=base(); kicker(s,"HOW IT LEARNS",GOLD); title(s,"Rolling downhill in fog");
fig(s,"w4_gradient.png",M,2.1,6.6,4.4);
bullets(s,["A loss is one number: how wrong the model is right now.",
 "Ask which direction lowers it, take a small step, repeat. That is gradient descent.",
 "Thousands of weights, all nudged at once, millions of times.",
 "No calculus today. The picture is the idea: you cannot see the whole landscape, only the slope under your feet.",
 "This is also why training is slow, and why it can settle somewhere that is not the bottom."],{x:7.6,w:5.0,fontSize:14});

// 9 the problem embeddings solve
s=base(); kicker(s,"IDEA TWO",TERRA); title(s,"What counting cannot do");
fig(s,"w4_onehot_vs_dense.png",M,2.2,8.4,3.9);
bullets(s,["In a bag of words, happy and joyful share nothing at all. Neither do Oakland and Berkeley.",
 "Every word is its own column, and every pair is equally unrelated.",
 "You have lived with this since Week 2. It is counting's honest floor.",
 "The fix: a few dozen numbers per word instead, chosen so that similar words land near each other."],{x:9.4,w:3.3,fontSize:13.5});

// 10 where vectors come from
s=base(); kicker(s,"IDEA TWO",TERRA); title(s,"Where the numbers come from");
fig(s,"w4_skipgram.png",M,2.2,7.2,3.7);
bullets(s,["A word is known by the company it keeps.",
 "So train a small network on a fake task: given a word, guess the words around it.",
 "Slide that window over a billion words of text.",
 "Throw the predictions away. Keep the hidden layer: one vector per word.",
 "That is word2vec, and it is the machinery behind this morning's paper."],{x:8.1,w:4.5,fontSize:14});

// 11 neighbours, from our own corpus
s=base(); kicker(s,"IT WORKS ON A SMALL CORPUS TOO",GREEN); title(s,"Trained on two novels, an hour ago");
fig(s,"w4_neighbours.png",M,2.1,7.4,4.3);
bullets(s,[`${facts.corpus_tokens.toLocaleString()} words of Frankenstein and Dracula, ${facts.corpus_vocab.toLocaleString()} word types.`,
 "No labels, no supervision, nobody told it what a door is.",
 "Nearest neighbours in the space it learned - and they are the words you would have listed.",
 "Small corpus, so the vectors are rough. The idea does not need a supercomputer to show itself."],{x:8.3,w:4.3,fontSize:13.5});

// 12 the map
s=base(); kicker(s,"THE MAP",BLUE); title(s,"Meaning becomes geometry");
fig(s,"w4_map.png",M,2.0,7.4,4.6);
bullets(s,["The same vectors, squashed to two dimensions so you can look at them.",
 "Times of day cluster. Family words cluster. Ship, sea and ice sit together.",
 "Nothing here was labelled. The clusters are what the text did.",
 "Embedding Projector, live: search a word, spin the space, read the neighbours."],{x:8.3,w:4.3,fontSize:14});
caption(s,"Two dimensions of eighty. The picture always loses something - Week 5 makes that its own lesson.");

// 13 the analogy, with caveats
s=base(); kicker(s,"THE FAMOUS TRICK",GOLD); title(s,"king − man + woman ≈ queen");
s.addShape("roundRect",{x:M,y:2.1,w:5.9,h:2.0,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("king − man + woman → queen\nparis − france + japan → tokyo",
 {x:M+0.35,y:2.4,w:5.3,h:1.4,fontFace:MONO,fontSize:16,color:TERRA,margin:0,lineSpacingMultiple:1.35});
bullets(s,["Directions in the space carry relationships nobody labelled.",
 "The arithmetic is nudged: the query words are excluded from the answer, or king comes back as its own nearest neighbour.",
 "Most analogies fail. The famous four are the ones that worked.",
 "The same geometry gives doctor − man + woman → nurse (Bolukbasi 2016), which is this morning's paper arriving from the other direction."],{y:4.3,w:5.9,h:2.5,fontSize:14});
s.addShape("roundRect",{x:6.9,y:2.1,w:5.7,h:4.3,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("three kinds of vector, in one breath",{x:7.2,y:2.35,w:5.1,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
[["static","one vector per word, forever. word2vec, GloVe.",TERRA],
 ["contextual","one vector per occurrence: bank in two sentences, two vectors. BERT and after.",BLUE],
 ["sentence","one vector per document, which is what Week 5 actually uses on your corpus.",GREEN]].forEach((r,i)=>{
  const y=2.85+i*1.15;
  s.addText(r[0],{x:7.2,y:y,w:5.1,h:0.35,fontFace:SERIF,fontSize:16,bold:true,color:r[2],margin:0});
  s.addText(r[1],{x:7.2,y:y+0.38,w:5.1,h:0.7,fontFace:SANS,fontSize:13,color:INK,margin:0,valign:"top"});
});

// 14 break
s=base(true); kicker(s,"BREAK",GOLD);
s.addText("Ten minutes",{x:M,y:2.6,w:11,h:1.0,fontFace:SERIF,fontSize:40,bold:true,color:WHITE});
s.addText("Then: where your corpus actually comes from.",{x:M,y:3.7,w:11,h:0.6,fontFace:SANS,fontSize:18,italic:true,color:CREAM});

// 15 three routes
s=base(); kicker(s,"GETTING THE DATA",TERRA); title(s,"Three routes, in the order you should try them");
[["1","A prepared file","pd.read_csv(url) · gdown · load_dataset() · unzip. Most corpora already exist. Most projects should stop here.",GREEN],
 ["2","An API","A documented URL that returns JSON. Endpoint, key, pagination, rate limit - four words you will meet in the next ten minutes.",BLUE],
 ["3","A careful scrape","Only when there is no file and no API. BeautifulSoup, slowly, and never republished.",TERRA]].forEach((r,i)=>{
  const y=2.2+i*1.45;
  s.addShape("roundRect",{x:M,y,w:11.9,h:1.25,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addShape("ellipse",{x:M+0.3,y:y+0.32,w:0.6,h:0.6,fill:{color:r[3]},line:{type:"none"}});
  s.addText(r[0],{x:M+0.3,y:y+0.32,w:0.6,h:0.6,fontFace:SERIF,fontSize:19,bold:true,color:WHITE,align:"center",valign:"middle"});
  s.addText(r[1],{x:M+1.1,y:y+0.18,w:3.1,h:0.5,fontFace:SERIF,fontSize:18,bold:true,color:INK,margin:0});
  s.addText(r[2],{x:M+4.3,y:y+0.2,w:7.3,h:0.9,fontFace:SANS,fontSize:13.5,color:INK,margin:0,valign:"top"});
});
caption(s,"The licensing line decides which routes are even open to you. That is the next slide.");

// 16 the API, live
s=base(); kicker(s,"ROUTE TWO, LIVE",BLUE); title(s,"A URL, some JSON, and then a table");
fig(s,"w4_api.png",M,2.1,8.6,4.0);
bullets(s,["An endpoint is just a URL that answers with data instead of a web page.",
 "A key is a name badge. Some APIs want one; the museums here do not.",
 "Pagination: it hands you a page at a time, and you ask for the next.",
 "A rate limit is the host saying how fast you may knock. Respect it and you keep the door open."],{x:9.6,w:3.1,fontSize:13});
caption(s,`The panel on the left is a real response, ${facts.api_source}. The AI writes the three lines that turn it into the table.`);

// 17 scraping, with the rules attached
s=base(); kicker(s,"ROUTE THREE",TERRA); title(s,"Scraping, and the four things that come with it");
[["Read robots.txt and the terms","before the first request, not after the complaint.",TERRA],
 ["Request slowly","one page every couple of seconds. You are a guest on someone's server.",GOLD],
 ["Take only what you need","the fields your question uses, not the whole site.",GREEN],
 ["Never republish the text","analyse it, quote it, count it. Do not hand it on.",BLUE]].forEach((r,i)=>{
  const y=2.2+i*1.15;
  s.addShape("roundRect",{x:M,y,w:11.9,h:1.0,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addText(r[0],{x:M+0.35,y:y+0.1,w:4.4,h:0.8,fontFace:SERIF,fontSize:17,bold:true,color:r[2],valign:"middle",margin:0});
  s.addText(r[1],{x:M+4.9,y:y+0.1,w:6.7,h:0.8,fontFace:SANS,fontSize:13.5,color:INK,valign:"middle",margin:0});
});
s.addText("CC0 and public domain: go anywhere.   Academic sets and community text: analyse, don't redistribute.   Shadow libraries: never.",
 {x:M,y:6.9,w:11.9,h:0.4,fontFace:SANS,fontSize:12.5,italic:true,color:MUTED});

// 18 the lab
s=base(); kicker(s,"YOUR TURN · 20 MINUTES",GREEN); title(s,"Collect it, save it, and start the repo");
bullets(s,["Point the cookbook notebook at your corpus. File, API or scrape, whichever your data needs.",
 "Reshape it with the AI until it is a table you would want to work with.",
 "Save it to your Drive project folder. Week 5 starts from that file, and Colab forgets everything else.",
 "Fork the publishing template and switch GitHub Pages on, so a live URL exists today rather than in Week 9 under deadline."],{w:6.4});
s.addShape("roundRect",{x:7.4,y:2.2,w:5.2,h:3.4,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("before you leave",{x:7.7,y:2.45,w:4.6,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
[["a file in Drive",GREEN],["a repo with Pages on",BLUE],["two minutes of pitch, to a partner",TERRA]].forEach((r,i)=>{
  s.addShape("ellipse",{x:7.7,y:3.05+i*0.75,w:0.22,h:0.22,fill:{color:r[1]},line:{type:"none"}});
  s.addText(r[0],{x:8.1,y:2.92+i*0.75,w:4.3,h:0.5,fontFace:SANS,fontSize:14.5,color:INK,margin:0});
});
s.addText("A null result, honestly shown, is a complete project. The pivot kit is insurance, not a demotion.",
 {x:7.7,y:5.2,w:4.6,h:0.9,fontFace:SANS,fontSize:12.5,italic:true,color:MUTED,valign:"top"});

// 19 homework
s=base(true); kicker(s,"BEFORE WEEK 5",GOLD);
s.addText("Homework",{x:M,y:1.0,w:11,h:0.8,fontFace:SERIF,fontSize:34,bold:true,color:WHITE});
[["Data Biography","~400 words on your corpus: where it came from, who made it, who is in it, who is missing, and what it cannot tell you however cleverly you count.",GOLD],
 ["Collect it for real","Use the cookbook notebook and leave the file in your Drive project folder. Week 5 begins there.",GREEN],
 ["Play with the map","Open the Embedding Projector, search a word from your own corpus, and bring back one neighbour that makes sense and one that does not.",CREAM]].forEach((r,i)=>{
  s.addShape("ellipse",{x:M,y:2.25+i*1.45,w:0.24,h:0.24,fill:{color:r[2]},line:{type:"none"}});
  s.addText(r[0],{x:M+0.45,y:2.1+i*1.45,w:11,h:0.4,fontFace:SANS,fontSize:15,bold:true,color:r[2],margin:0});
  s.addText(r[1],{x:M+0.45,y:2.5+i*1.45,w:10.8,h:0.95,fontFace:SANS,fontSize:14,color:CREAM,valign:"top",margin:0});
});
s.addText("Next week: embeddings on YOUR corpus, all session. Bring the file.",{x:M,y:6.6,w:11.9,h:0.5,fontFace:SANS,fontSize:13,italic:true,color:GOLD});

pres.writeFile({ fileName: path.join(__dirname, "week-04-lecture-draft.pptx") })
    .then(()=>console.log("written: slides/week-04-lecture-draft.pptx"));
