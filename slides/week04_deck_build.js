// Week 4 lecture draft deck: neural networks, word embeddings, and getting data.
//
// Figures come from slides/week04_figs.py — the spiral is a real fit, the word vectors
// are trained on the two novels in the repo, the API panel is a live call. Run that
// first; this reads its PNGs and week04_figs.json out of $FIG_DIR (default /tmp/figs).
//
//   python3 slides/week04_figs.py && node slides/week04_deck_build.js
//
// Figure-led by design: most slides are a picture and one line. Four figures come
// from the week's reading itself, cropped from the arXiv preprint at build time.
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
function credit(s,t){ s.addText(t,{x:M,y:6.95,w:11.9,h:0.35,fontFace:SANS,fontSize:10,color:MUTED}); }
const PAPER = "Garg, Schiebinger, Jurafsky & Zou, PNAS 2018 (arXiv:1711.08412)";
const hasFig = (f) => fs.existsSync(F + f);
// a slide that is mostly picture: one line of setup, one line underneath
function figSlide(s,file,{x=1.5,y=1.95,w=10.3,h=4.4,note=null,cred=null}={}){
  if (hasFig(file)) fig(s,file,x,y,w,h);
  if (note) s.addText(note,{x:M,y:6.45,w:11.9,h:0.45,fontFace:SERIF,fontSize:16,italic:true,color:INK});
  if (cred) credit(s,cred);
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

// 3 look at this: the figure, almost nothing else
s=base(); kicker(s,"LOOK AT THIS · THIS WEEK'S READING",TERRA);
title(s,"A century, measured as distance");
figSlide(s,"w4_paper_time.png",{x:1.9,y:1.9,w:9.6,h:4.4,
  note:"Blue: how far occupation words sit from she-words versus he-words, decade by decade. Green: the share of women actually in those jobs.",
  cred:"Fig. 1b, " + PAPER + " · shown for teaching"});

// 3b the validation
s=base(); kicker(s,"WHY IT IS EVIDENCE AND NOT A DEMO",GREEN);
title(s,"The vectors agree with the census");
figSlide(s,"w4_paper_validation.png",{x:2.1,y:1.9,w:9.2,h:4.4,
  note:"One dot per occupation. Right on the x-axis: the word sits closer to she-words. Up on the y-axis: more women in the job.",
  cred:"Fig. 1a, " + PAPER + " · shown for teaching"});

// 3c the adjectives
s=base(); kicker(s,"THE SAME METHOD, POINTED AT ADJECTIVES",GOLD);
title(s,"Top words associated with women, by decade");
figSlide(s,"w4_paper_adjectives.png",{x:3.6,y:1.85,w:6.1,h:4.5,
  note:"1910 to 1990, from the same embeddings. Read the columns down, then argue about the last one.",
  cred:"Fig. 2a, " + PAPER + " · shown for teaching"});

// 4 question it
s=base(); kicker(s,"QUESTION IT",GREEN); title(s,"Before you believe the curve");
qcards(s,[["Whose century is it? Google Books and COHA are what got printed and digitised. Is the shift in the country, or in publishing?",TERRA],
 ["Who chose the words? Someone decided which words count as female and which jobs count as occupations. Where in the paper is that list?",GOLD],
 ["The bias it detects is the bias in the text - the same geometry that makes king - man + woman work. Can you keep one and refuse the other?",GREEN],
 ["What would convince you? Name the check you would want run before repeating this finding out loud.",BLUE]],2.1,1.28,13.5);

// 5 the neuron
s=base(); kicker(s,"IDEA ONE",GREEN); title(s,"You already built a neuron");
figSlide(s,"w4_neuron.png",{x:1.6,y:1.9,w:10.1,h:4.5,
  note:"Counts in, one weight each, add them up, squash. Week 3's classifier is one neuron."});

// 6 the network
s=base(); kicker(s,"IDEA ONE",GREEN); title(s,"Stack them and something changes");
figSlide(s,"w4_network.png",{x:1.6,y:1.9,w:10.1,h:4.5,
  note:"Four neurons in between, each adding up every word in its own way. Nobody chose those combinations."});

// 6b what the layer costs
s=base(); kicker(s,"WHAT IT COSTS",TERRA); title(s,"You stop being able to read it");
figSlide(s,"w4_readability.png",{x:1.4,y:1.95,w:10.5,h:4.3,
  note:`Same passages, same job: ${pct(facts.novel_lr_acc)} against ${pct(facts.novel_net_acc)}. You can read the left panel and say why. You cannot do that with the right one.`,
  cred:`Both fitted for this slide on ${facts.novel_chunks} passages of Frankenstein and Dracula.`});

// 7 the spiral
s=base(); kicker(s,"WHY IT MATTERS",BLUE); title(s,"Some questions a straight line cannot answer");
figSlide(s,"w4_spiral.png",{x:1.2,y:1.9,w:10.9,h:4.5,
  note:`Same points, same training. One neuron: ${pct(facts.spiral_linear)}. Two hidden layers: ${pct(facts.spiral_net)}.`,
  cred:"Both models fitted for this slide. Next: the same thing live in TensorFlow Playground."});

// 8 gradient descent
s=base(); kicker(s,"HOW IT LEARNS",GOLD); title(s,"Rolling downhill in fog");
figSlide(s,"w4_gradient.png",{x:2.4,y:1.9,w:8.5,h:4.5,
  note:"A loss says how wrong you are. Step downhill, repeat, thousands of weights at once. No calculus today."});

// 9 the problem embeddings solve
s=base(); kicker(s,"IDEA TWO",TERRA); title(s,"What counting cannot do");
figSlide(s,"w4_onehot_vs_dense.png",{x:1.2,y:2.1,w:10.9,h:4.0,
  note:"Week 2 gave every word its own column, so night and morning have nothing in common. Nor do night and ship.",
  cred:`And Week 3 puts one weight on each column, so what it learns about one word tells it nothing about the next. Trained vectors: night and morning ${facts.sim_night_morning}, night and ship ${facts.sim_night_ship}.`});

// 10 where the numbers come from: the contrastive move
s=base(); kicker(s,"IDEA TWO",TERRA); title(s,"Same context, pull together. Different, push apart");
figSlide(s,"w4_contrastive_idea.png",{x:1.9,y:1.9,w:9.6,h:4.4,
  note:"For a word, a context is a few words of text. That is the whole rule. It is called contrastive learning, and most modern embeddings are trained this way.",
  cred:`Underneath it, Week 3's four moves: multiply, add, squash, nudge. The difference is that the prediction is thrown away and the weights are what you keep. ${facts.contrastive_pairs.toLocaleString()} pairs in one pass.`});

// 10b what falls out of it
s=base(); kicker(s,"THE SAME VECTORS, BEFORE AND AFTER",GOLD); title(s,"Nobody labelled the blocks");
figSlide(s,"w4_contrastive_result.png",{x:1.5,y:1.9,w:10.3,h:4.4,
  note:"Twelve words, every pair compared. On the left they start as noise. On the right, times of day, family and rooms have found each other."});

// 11 neighbours, from our own corpus
s=base(); kicker(s,"IT WORKS ON A SMALL CORPUS TOO",GREEN); title(s,"Trained on two novels, an hour ago");
figSlide(s,"w4_neighbours.png",{x:1.7,y:2.0,w:9.9,h:4.3,
  note:`${facts.corpus_tokens.toLocaleString()} words of Frankenstein and Dracula, and no labels anywhere. Nobody told it what a door is.`});

// 12 the map
s=base(); kicker(s,"THE MAP",BLUE); title(s,"Meaning becomes geometry");
figSlide(s,"w4_map.png",{x:2.2,y:1.9,w:8.9,h:4.5,
  note:"Family words on one side. Door, room and window on the other. Night and morning at the bottom. Nothing was labelled.",
  cred:"Two dimensions of sixty; the picture always loses something. Next: the Embedding Projector, live."});

// what the vectors also learned
s=base(); kicker(s,"THE SAME GEOMETRY, THE OTHER RESULT",TERRA);
title(s,"Occupations closest to each group's words");
figSlide(s,"w4_paper_ethnic.png",{x:3.9,y:1.85,w:5.6,h:4.5,
  note:"Nobody labelled any of this. It is what a century of printed English put near what.",
  cred:"Fig. 1c, " + PAPER + " · shown for teaching"});

// 13 the analogy, with caveats
s=base(); kicker(s,"THE FAMOUS TRICK",GOLD); title(s,"king − man + woman ≈ queen");
s.addShape("roundRect",{x:M,y:2.1,w:11.9,h:1.6,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("king − man + woman → queen        paris − france + japan → tokyo",
 {x:M+0.4,y:2.35,w:11.1,h:1.1,fontFace:MONO,fontSize:19,color:TERRA,margin:0,valign:"middle"});
bullets(s,["Directions carry relationships nobody labelled.",
 "The arithmetic is nudged, and most analogies fail. The famous four are the ones that worked.",
 "Same geometry, other result: doctor − man + woman → nurse."],{y:4.0,w:6.1,h:2.4,fontSize:16});
s.addShape("roundRect",{x:7.1,y:4.0,w:5.5,h:2.4,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
[["static","one vector per word",TERRA],["contextual","one per occurrence",BLUE],
 ["sentence","one per document — Week 5",GREEN]].forEach((r,i)=>{
  s.addText(r[0],{x:7.4,y:4.2+i*0.72,w:2.2,h:0.5,fontFace:SERIF,fontSize:16,bold:true,color:r[2],margin:0,valign:"middle"});
  s.addText(r[1],{x:9.5,y:4.2+i*0.72,w:2.9,h:0.5,fontFace:SANS,fontSize:13.5,color:INK,margin:0,valign:"middle"});
});

// --- the same two ideas, on pixels
// 13b what a convolution is, with nothing left out
s=base(); kicker(s,"THE SAME TRICK, ON PIXELS",BLUE); title(s,"A convolution, all of it");
figSlide(s,"w4_conv_arith.png",{x:0.6,y:2.15,w:12.1,h:3.6,
  note:`A picture is a grid of numbers. Take nine of them, multiply by nine other numbers, add them up: ${facts.conv_one_output}. Move one pixel across and repeat.`,
  cred:"Numbers read off a Met painting from the Week 1 data. Nothing else happens in a convolution."});

// 13c a filter is a question about the picture
s=base(); kicker(s,"WHAT THE NINE NUMBERS DO",BLUE); title(s,"Change the filter, ask a different question");
figSlide(s,"w4_convolution.png",{x:0.9,y:2.2,w:11.5,h:3.5,
  note:"Each panel is the same painting under a different 3x3 grid. One finds vertical edges, one horizontal, one blurs.",
  cred:"A CNN is not given these. It starts with random grids and learns which ones are worth having, by the same downhill roll as before."});

// 13d depth
s=base(); kicker(s,"WHY A CNN IS DEEP",BLUE); title(s,"Filters on top of filters");
figSlide(s,"w4_conv_stack.png",{x:0.9,y:2.2,w:11.5,h:3.5,
  note:"Run a filter over the output of the last filter, then shrink. Edges turn into corners, and corners into regions.",
  cred:"Every panel is real arithmetic on the painting to its left. Stacking them is all a CNN is."});

// 13e where the two halves meet
s=base(); kicker(s,"BOTH IDEAS AT ONCE",GOLD); title(s,"The same rule, where a context is a picture");
figSlide(s,"w4_clip.png",{x:1.2,y:1.95,w:10.9,h:4.2,
  note:"Same context: a painting and its own caption, pulled together. Different context: anyone else's caption, pushed away. Two kinds of thing in one space.",
  cred:"Which is why \"a painting of a woman in a red hat\" can search a museum with no tags in it at all. The notebook trains a small one on 18 paintings."});

// 14 break
s=base(true); kicker(s,"BREAK",GOLD);
s.addText("Ten minutes",{x:M,y:2.6,w:11,h:1.0,fontFace:SERIF,fontSize:40,bold:true,color:WHITE});
s.addText("Then: where your corpus actually comes from.",{x:M,y:3.7,w:11,h:0.6,fontFace:SANS,fontSize:18,italic:true,color:CREAM});

// 15 three routes
s=base(); kicker(s,"GETTING THE DATA",TERRA); title(s,"Three routes, in the order you should try them");
[["1","A prepared file","pd.read_csv(url) · gdown · load_dataset(). Most projects should stop here.",GREEN],
 ["2","An API","A documented URL that returns JSON. Four words: endpoint, key, pagination, rate limit.",BLUE],
 ["3","A careful scrape","Only when there is no file and no API. Slowly, and never republished.",TERRA]].forEach((r,i)=>{
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
figSlide(s,"w4_api.png",{x:1.2,y:2.1,w:10.9,h:4.1,
  note:"An endpoint is a URL that answers with data. A key is a name badge. Pagination hands you a page at a time.",
  cred:`Left panel: a real response, ${facts.api_source}. The AI writes the three lines that make the table.`});

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
s=base(); kicker(s,"YOUR TURN · 20 MINUTES",GREEN); title(s,"Collect it, save it, start the repo");
[["a file in your Drive folder","Week 5 starts from it. Colab forgets everything else.",GREEN],
 ["a repo with Pages switched on","so a live URL exists today, not in Week 9 under deadline.",BLUE],
 ["two minutes of pitch, to a partner","corpus, two methods, what would count as a finding.",TERRA]].forEach((r,i)=>{
  const y=2.3+i*1.4;
  s.addShape("roundRect",{x:M,y,w:11.9,h:1.2,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addText(r[0],{x:M+0.4,y:y+0.15,w:4.6,h:0.9,fontFace:SERIF,fontSize:19,bold:true,color:r[2],valign:"middle",margin:0});
  s.addText(r[1],{x:M+5.2,y:y+0.15,w:6.3,h:0.9,fontFace:SANS,fontSize:14,color:INK,valign:"middle",margin:0});
});
caption(s,"A null result, honestly shown, is a complete project. The pivot kit is insurance, not a demotion.");

// 19 homework
s=base(true); kicker(s,"BEFORE WEEK 5",GOLD);
s.addText("Homework",{x:M,y:1.0,w:11,h:0.8,fontFace:SERIF,fontSize:34,bold:true,color:WHITE});
[["Data Biography","~400 words: where it came from, who is in it, who is missing, what it cannot tell you.",GOLD],
 ["Collect it for real","The cookbook notebook, and leave the file in Drive. Week 5 begins there.",GREEN],
 ["Play with the map","Embedding Projector: a word from your corpus, one neighbour that makes sense and one that does not.",CREAM]].forEach((r,i)=>{
  s.addShape("ellipse",{x:M,y:2.25+i*1.45,w:0.24,h:0.24,fill:{color:r[2]},line:{type:"none"}});
  s.addText(r[0],{x:M+0.45,y:2.1+i*1.45,w:11,h:0.4,fontFace:SANS,fontSize:15,bold:true,color:r[2],margin:0});
  s.addText(r[1],{x:M+0.45,y:2.5+i*1.45,w:10.8,h:0.95,fontFace:SANS,fontSize:14,color:CREAM,valign:"top",margin:0});
});
s.addText("Next week: embeddings on YOUR corpus, all session. Bring the file.",{x:M,y:6.6,w:11.9,h:0.5,fontFace:SANS,fontSize:13,italic:true,color:GOLD});

pres.writeFile({ fileName: path.join(__dirname, "week-04-lecture-draft.pptx") })
    .then(()=>console.log("written: slides/week-04-lecture-draft.pptx"));
