// Week 2 lecture draft deck. Figures in /tmp/figs (see notebooks/week02 for the code
// that generates each from live data). Run: node week02_deck_build.js
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.defineLayout({ name: "W", width: 13.333, height: 7.5 });
pres.layout = "W";
const TERRA="7A3B2E", TERRA_DK="4E261D", INK="1A1A1A", MUTED="6B6B63",
      GREEN="3F6F5F", GOLD="B9852F", BLUE="2E5F8A", TINT="F4EEE8", WHITE="FFFFFF", CREAM="E8DCD6";
const SERIF="Cambria", SANS="Calibri";
const M=0.7, F="/tmp/figs/";
function base(dark=false){ const s=pres.addSlide(); s.background={color:dark?TERRA_DK:WHITE}; return s; }
function kicker(s,t,c=GOLD){ s.addText(t,{x:M,y:0.55,w:11.5,h:0.35,fontFace:SANS,fontSize:13,bold:true,color:c,charSpacing:3}); }
function title(s,t,c=INK){ s.addText(t,{x:M,y:0.95,w:12,h:0.85,fontFace:SERIF,fontSize:34,bold:true,color:c,valign:"top"}); }
function bullets(s,items,opt={}){
  const o=Object.assign({x:M,y:2.2,w:5.4,h:4.6,fontFace:SANS,fontSize:15,color:INK,valign:"top",lineSpacingMultiple:1.15,paraSpaceAfter:10},opt);
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

// 1 title
let s=base(true);
s.addText("CULTURE AS DATA · WEEK 2",{x:M,y:0.7,w:8,h:0.3,fontFace:SANS,fontSize:13,color:GOLD,bold:true,charSpacing:3});
s.addText("Counting, Compared:",{x:M,y:2.0,w:11.5,h:1.0,fontFace:SERIF,fontSize:48,bold:true,color:WHITE});
s.addText("Is the Difference Real?",{x:M,y:2.95,w:11.5,h:1.0,fontFace:SERIF,fontSize:48,bold:true,color:CREAM});
s.addText("One session, one case: Bollen v. Schmidt, tried live on Google Books,\nthen replicated by this room on Reddit",{x:M,y:4.5,w:10.5,h:1.1,fontFace:SANS,fontSize:17,italic:true,color:CREAM,lineSpacingMultiple:1.25});
[GOLD,GREEN,CREAM].forEach((c,i)=>s.addShape("ellipse",{x:11.3+i*0.42,y:0.62,w:0.22,h:0.22,fill:{color:c},line:{type:"none"}}));

// 2 arc
s=base(); kicker(s,"TODAY",TERRA); title(s,"One case, six steps");
[["1","What counts as a word","Tokenize, and a stop list's three rounds",TERRA],
 ["2","tf-idf","Twelve communities, sight-read from their words",GREEN],
 ["3","Elevated words","Keyness: topic, and register underneath",GOLD],
 ["4","The statistics","z-scores, the shuffle test, the bootstrap: hands on",BLUE],
 ["5","The trial","Bollen's evidence, pulled live",TERRA],
 ["6","The replication","Yours: one community, fifteen years",GREEN]].forEach((st,i)=>{
  const col=i%2,row=Math.floor(i/2),x=M+col*6.2,y=2.15+row*1.55;
  s.addShape("roundRect",{x,y,w:5.9,h:1.3,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addShape("ellipse",{x:x+0.25,y:y+0.33,w:0.62,h:0.62,fill:{color:st[3]},line:{type:"none"}});
  s.addText(st[0],{x:x+0.25,y:y+0.33,w:0.62,h:0.62,fontFace:SERIF,fontSize:20,bold:true,color:WHITE,align:"center",valign:"middle"});
  s.addText(st[1],{x:x+1.05,y:y+0.16,w:4.7,h:0.45,fontFace:SANS,fontSize:16,bold:true,color:INK,margin:0});
  s.addText(st[2],{x:x+1.05,y:y+0.6,w:4.7,h:0.6,fontFace:SANS,fontSize:12.5,color:MUTED,margin:0,valign:"top"});
});

// 3 discussion opener
s=base(); kicker(s,"DISCUSSION · BEFORE ANY CODE",GREEN); title(s,"What does it mean to count a feeling?");
qcards(s,[["“I am a failure” appears in a book. List the possible reasons it was written. How many of them are distress?",TERRA],
 ["If a phrase's frequency doubles, what claims does that support: about authors? readers? publishers? the age?",GOLD],
 ["What would you accept as evidence that a society got sadder? Write it down; today tests your standard.",GREEN]]);

// 4-6 trial
s=base(); kicker(s,"THE TRIAL · EXHIBIT A",TERRA); title(s,"The claim: a hockey stick of distress");
bullets(s,["Bollen et al. (PNAS 2021): cognitive-distortion phrases surge in Google Books after 2000.",
 "An n-gram count over ~500 billion words: the biggest counting study you will meet.",
 "This chart is not from the paper. The notebook pulled it minutes ago from the Ngram Viewer's JSON endpoint."]);
fig(s,"bollen_claim.png",6.4,2.1,6.2,4.3);

s=base(); kicker(s,"THE TRIAL · EXHIBIT B",GREEN); title(s,"The objection: the corpus changed under the count");
bullets(s,["Schmidt et al.: Google scanned more fiction over time. Maybe the surge is novels, not despair.",
 "The test: phrases that mark fiction and nothing else. “She whispered.” “He grinned.”",
 "They hockey-stick identically. Composition can manufacture a trend by itself."]);
fig(s,"bollen_fiction.png",6.4,2.1,6.2,4.3);

s=base(); kicker(s,"THE TRIAL · CROSS-EXAMINATION",GOLD); title(s,"The same phrase, fiction-only vs. all books");
bullets(s,["Inside fiction, “I am a failure” is roughly level for a century. The rise lives in the mixed corpus.",
 "But the authors deleted fiction entirely, re-ran, and reported the pattern held. The trial is not over.",
 "Hold that thought: what design would SETTLE it? You run one today."]);
fig(s,"bollen_check.png",6.4,2.1,6.2,4.3);

// 7 tools I
s=base(); kicker(s,"THE TOOLS · 1",TERRA); title(s,"What counts as a word");
bullets(s,["Our tokenizer strips apostrophes: don't becomes don + t. One tool's choice is the next tool's cleanup job.",
 "A stop list takes three rounds: obvious function words, then the shrapnel and fillers, then a judgment call.",
 "The judgment: in r/relationship_advice, are her and him function words, or the cast of the stories?"],{w:5.7});
s.addShape("roundRect",{x:6.7,y:2.2,w:5.9,h:4.0,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("three rounds on live comments",{x:7.0,y:2.45,w:5.3,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
[["round 1","s · t · not · her · if · him",TERRA],["round 2","her · him · know · husband · need · want",GREEN],
 ["round 3","know · husband · need · feel · yourself · life",GOLD]].forEach((r,i)=>{
  s.addText(r[0],{x:7.0,y:3.0+i*1.0,w:1.6,h:0.4,fontFace:SANS,fontSize:13,bold:true,color:r[2],margin:0});
  s.addText(r[1],{x:8.5,y:3.0+i*1.0,w:4.0,h:0.8,fontFace:SERIF,fontSize:14,italic:true,color:INK,margin:0});
});

// 8 tools II tfidf
s=base(); kicker(s,"THE TOOLS · 2",BLUE); title(s,"tf-idf: twelve communities, sight-read");
[[["r/Cooking","salt, veggies, protein"],["r/personalfinance","roth, account, rate"],["r/buildapc","cpu, fans, cooler"],
 ["r/gardening","plant, sun, leaves"],["r/cats","cat, kitten, feed"],["r/travel","flights, hotel, minute"]],
 [["r/wallstreetbets","puts, bulls, premium"],["r/movies","movie, trailer, films"],["r/Parenting","kids, naps, teach"],
 ["r/nba","player, shots, games"],["r/relationship_advice","adult, deserve, ex"],["r/askscience","math, animals, wildlife"]]].forEach((col,ci)=>col.forEach((r,i)=>{
  s.addText(r[0],{x:M+ci*6.2,y:2.05+i*0.78,w:2.7,h:0.7,fontFace:SANS,fontSize:13,bold:true,color:TERRA,valign:"middle",margin:0});
  s.addText(r[1],{x:M+2.7+ci*6.2,y:2.05+i*0.78,w:3.3,h:0.7,fontFace:SERIF,fontSize:13.5,italic:true,color:INK,valign:"middle",margin:0});
}));
s.addText("One document per community. “Common here, rare overall” becomes “what this community talks about that the others don't.”",{x:M,y:6.85,w:11.9,h:0.4,fontFace:SANS,fontSize:11,italic:true,color:MUTED});

// 9 tools III keyness
s=base(); kicker(s,"THE TOOLS · 3",TERRA); title(s,"Elevated words: keyness, then standardized keyness");
s.addShape("roundRect",{x:M,y:2.2,w:6.0,h:2.2,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("raw log-odds → topic",{x:M+0.3,y:2.4,w:5.4,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
s.addText("garden, plant, soil, seeds, water",{x:M+0.3,y:2.85,w:5.4,h:0.5,fontFace:SERIF,fontSize:16,italic:true,color:GREEN,margin:0});
s.addText("cpu, gpu, ram, motherboard, build",{x:M+0.3,y:3.45,w:5.4,h:0.5,fontFace:SERIF,fontSize:16,italic:true,color:BLUE,margin:0});
s.addShape("roundRect",{x:6.9,y:2.2,w:6.0,h:2.2,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("standardized by variance → register",{x:7.2,y:2.4,w:5.4,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
s.addText("i, we, them  — a stories room",{x:7.2,y:2.85,w:5.4,h:0.5,fontFace:SERIF,fontSize:16,italic:true,color:GREEN,margin:0});
s.addText("you, your, if  — an advice room",{x:7.2,y:3.45,w:5.4,h:0.5,fontFace:SERIF,fontSize:16,italic:true,color:BLUE,margin:0});
s.addText([{text:"A small gap in a very common word can be stronger evidence than a big gap in a rare one. Both lists are true; they answer different questions.",options:{breakLine:true}},
 {text:"She Giggles, He Gallops is exactly this method: verbs after “she” vs. “he” in 2,000 screenplays.",options:{}}],
 {x:M,y:4.8,w:11.9,h:1.6,fontFace:SANS,fontSize:14.5,color:INK,valign:"top",lineSpacingMultiple:1.2,paraSpaceAfter:8});

// 10 three questions
s=base(); kicker(s,"THE STATISTICS, SIMPLIFIED",GOLD); title(s,"Three questions every counted claim must answer");
[["Compared to what?","A count needs a denominator. Bollen: share of ALL n-grams. Us: per 1,000 words, per control community.",TERRA],
 ["Could chance draw it?","Shuffle what should not matter (labels, years) 1,000 times. The fraction of shuffles that match the real gap IS the p-value.",GREEN],
 ["How big, give or take?","Effect size with error bars (the bootstrap). Significant is not big; small is not false. Report both.",BLUE]].forEach((c,i)=>{
  const x=M+i*4.15;
  s.addShape("roundRect",{x,y:2.2,w:3.9,h:3.9,fill:{color:TINT},line:{type:"none"},rectRadius:0.12});
  s.addShape("ellipse",{x:x+0.35,y:2.55,w:0.55,h:0.55,fill:{color:c[2]},line:{type:"none"}});
  s.addText(String(i+1),{x:x+0.35,y:2.55,w:0.55,h:0.55,fontFace:SERIF,fontSize:18,bold:true,color:WHITE,align:"center",valign:"middle"});
  s.addText(c[0],{x:x+0.35,y:3.3,w:3.2,h:0.6,fontFace:SERIF,fontSize:19,bold:true,color:INK,margin:0});
  s.addText(c[1],{x:x+0.35,y:3.95,w:3.25,h:2.0,fontFace:SANS,fontSize:13,color:INK,valign:"top",lineSpacingMultiple:1.18,margin:0});
});
s.addText("Every trap is a way of dodging one of the three: selection dodges 2, multiplicity cheats 2, a bare p dodges 3.",{x:M,y:6.5,w:11.9,h:0.4,fontFace:SANS,fontSize:13,italic:true,color:MUTED});

// 11 shuffle drawn
s=base(); kicker(s,"QUESTION 2, DRAWN",GREEN); title(s,"The shuffle test: could chance deal this gap?");
bullets(s,["The real gap: “water” appears 2.7 more times per 1,000 words in r/gardening than r/buildapc.",
 "Shuffle the community labels 1,000 times, recount each time: the gray pile is what chance can do.",
 "The real gap stands far outside the pile. Empirical p ≈ 0: this elevation is not luck.",
 "Five moves, in the notebook with YOUR-TURN blanks: pick, predict, shuffle, read the effect, say the sentence."],{w:5.4});
fig(s,"shuffle.png",6.4,2.1,6.2,4.3);

// 12 bootstrap drawn
s=base(); kicker(s,"QUESTION 3, DRAWN",BLUE); title(s,"The bootstrap: how big, give or take?");
bullets(s,["The shuffle asked “could it be zero?” The bootstrap asks the other question: “what sizes are believable?”",
 "Resample your own comments WITH replacement, 1,000 times; recompute the gap each time. Your data votes on its own uncertainty.",
 "The middle 95% is the confidence interval: here, 1.4 to 4.1 per 1,000. Far from zero (a finding), wide (stay humble about the exact number).",
 "The error bars on today's replication plot are exactly this, one bootstrap per year."],{w:5.4});
fig(s,"bootstrap.png",6.4,2.1,6.2,4.3);

// 13 traps
s=base(); kicker(s,"THE TRAPS, NAMED",TERRA); title(s,"Three ways significance fools you");
[["Selection","We shuffle-tested our top keyness word: p = 0, guaranteed. We picked it FOR its extremity. State the hypothesis before looking.",TERRA],
 ["Multiplicity","Split one community randomly in half: keyness still returns a convincing “distinctive vocabulary.” Pure noise. 1,500 words at p < .05: ~75 pass by luck.",GOLD],
 ["Size","“Significant” answers “is it chance?”, never “does it matter?” Report the effect and the p, together, with the bootstrap's interval around the effect.",BLUE]].forEach((t,i)=>{
  s.addShape("roundRect",{x:M,y:2.2+i*1.5,w:11.9,h:1.3,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addText(t[0],{x:M+0.35,y:2.3+i*1.5,w:2.2,h:1.1,fontFace:SERIF,fontSize:18,bold:true,color:t[2],valign:"middle",margin:0});
  s.addText(t[1],{x:M+2.7,y:2.3+i*1.5,w:8.9,h:1.1,fontFace:SANS,fontSize:13.5,color:INK,valign:"middle",margin:0});
});

// 14 replication design
s=base(); kicker(s,"THE REPLICATION · YOURS",TERRA); title(s,"Bollen on Reddit: hold the community fixed");
bullets(s,["Schmidt's demand, satisfied: one subreddit, fifteen years, only the year varies. Composition cannot write this trend.",
 "The honest adaptation: the paper's phrases are too rare for our samples, so we count the absolutist index (always, never, nothing...), 19 words that track distress language (Al-Mosaiwi & Johnstone 2018).",
 "The room's protocol: predict the shape out loud → run the default together → each pair swaps in a community they know → bring the plot back.",
 "Ten plots from ten communities is a real replication study, made in one classroom."]);
s.addShape("roundRect",{x:6.4,y:2.2,w:6.2,h:4.0,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("the design, in one line",{x:6.7,y:2.5,w:5.6,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
s.addText("rate(absolutist words | r/AskReddit, year)\nfor year in 2010 … 2024",{x:6.7,y:3.0,w:5.6,h:1.2,fontFace:"Courier New",fontSize:15,color:INK,margin:0});
s.addText("…then the trend itself goes on trial:\ncorrelate with year, and shuffle the years 1,000 times.",{x:6.7,y:4.4,w:5.6,h:1.4,fontFace:SANS,fontSize:14,italic:true,color:INK,margin:0});

// 15 replication result
s=base(); kicker(s,"THE REPLICATION · A SAMPLE RUN",GOLD); title(s,"It climbs here too, with composition controlled");
fig(s,"replication.png",M,2.1,6.4,4.3);
bullets(s,["Our sample run: absolutist words climb from ~8 toward ~15 per 1,000 across fifteen years of one community. Trend r ≈ 0.8; shuffled years rarely match it.",
 "Evidence the composition story cannot explain. Not proof of sadness: AskReddit's users drifted, the proxy is 19 words, each point is a few hundred comments (the error bars are the bootstrap saying so).",
 "What survives a second community, another word list, and bigger samples, you may say out loud."],{x:7.4,w:5.2,fontSize:14});

// 15b: how statistical truth is argued
s=base(); kicker(s,"THE CAPSTONE IDEA",TERRA); title(s,"How do we prove anything with statistics?");
s.addText("We don't. Statistics never proves a claim; it eliminates rivals. A finding is the claim left standing after every challenger you and your critics could name has had its turn.",
 {x:M,y:1.9,w:11.9,h:0.85,fontFace:SERIF,fontSize:17,italic:true,color:INK,lineSpacingMultiple:1.2});
[["Rival 1: chance","“Randomly dealt data would show this too.” Answer: the shuffle test. Break the structure 1,000 times; if chance rarely draws your gap, this rival is out. That is all a p-value ever says.",GREEN],
 ["Rival 2: something else did it","“The corpus changed under you” (Schmidt). Answer: design, not statistics. Hold the community fixed; remove the fiction; re-run without the suspect slice. Each control retires one rival by name.",GOLD],
 ["Rival 3: true but trivial, or true but local","Answer: the bootstrap's interval for size, and scope stated out loud: announced-in-the-Times brides, one subreddit, 19 proxy words. A claim without its scope is not yet a claim.",BLUE]].forEach((c,i)=>{
  s.addShape("roundRect",{x:M,y:2.95+i*1.25,w:11.9,h:1.08,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addText(c[0],{x:M+0.35,y:3.02+i*1.25,w:3.1,h:0.95,fontFace:SERIF,fontSize:15,bold:true,color:c[2],valign:"middle",margin:0});
  s.addText(c[1],{x:M+3.6,y:3.02+i*1.25,w:8.0,h:0.95,fontFace:SANS,fontSize:12,color:INK,valign:"middle",margin:0});
});
s.addText("So the argument's shape is: named claim → named rivals → a test or a design that retires each → the size, with its interval → the scope. Bollen argued this way; Schmidt answered this way; you replicated this way. Truth, here, is what survives.",
 {x:M,y:6.75,w:11.9,h:0.65,fontFace:SANS,fontSize:12.5,italic:true,color:MUTED,lineSpacingMultiple:1.15});

// 16 discussion counting
s=base(); kicker(s,"DISCUSSION · COUNTING",TERRA); title(s,"What did the count actually measure?");
qcards(s,[["Absolutist words rose. List every explanation: feelings, phones, age of users, comment length, moderation. Which could you test with today's tools?",TERRA],
 ["Daniels ranked rappers by unique words; Aesop Rock wins. What is that number a measurement OF: skill, genre, era, or the denominator?",GOLD],
 ["When is a zero a fact, and when is it a small sample? (Recall: “money” appeared 0 times in one gardening pull.)",GREEN]]);

// 17 discussion vectors + truth
s=base(); kicker(s,"DISCUSSION · VECTORS AND TRUTH",BLUE); title(s,"When numbers stand in for meaning");
qcards(s,[["A comment became a row of numbers, a community a cloud of points. What survived the translation, and what did not? One example of each.",BLUE],
 ["Two communities sit far apart in count-space. What exactly is far apart: the people, their topics, or the genre of writing? How would you tell?",GREEN],
 ["Your trend beat shuffled years. Is the finding TRUE? What separates “not chance” from “what I said it means”?",TERRA],
 ["The ratio climbed in books AND on Reddit. One truth measured twice, or two facts about two archives? What third corpus would decide?",GOLD]],1.95,1.28,13.5);

// 18 homework
s=base(true); kicker(s,"BEFORE WEEK 3",GOLD);
s.addText("Homework",{x:M,y:1.0,w:11,h:0.8,fontFace:SERIF,fontSize:34,bold:true,color:WHITE});
[["Reading","Matt Daniels, “The Largest Vocabulary in Hip Hop” (The Pudding, ~10 min). Today's session in the wild: token analysis, a chosen denominator, honest caveats. Name three choices Daniels made.",GOLD],
 ["Sketch","Finish your replication: your community, your prediction, the plot, and the three written answers from YOUR TURN 3.",GREEN],
 ["Check (AI closed)","Explain: why two tokenizers split a sentence differently, and what your shuffle test can and cannot rule out.",CREAM]].forEach((r,i)=>{
  s.addShape("ellipse",{x:M,y:2.25+i*1.45,w:0.24,h:0.24,fill:{color:r[2]},line:{type:"none"}});
  s.addText(r[0],{x:M+0.45,y:2.1+i*1.45,w:11,h:0.4,fontFace:SANS,fontSize:15,bold:true,color:r[2],margin:0});
  s.addText(r[1],{x:M+0.45,y:2.5+i*1.45,w:10.8,h:0.95,fontFace:SANS,fontSize:14,color:CREAM,valign:"top",margin:0});
});
s.addText("Next week: the classifier. r/sandiego vs. r/SanDiegan, and the words that give a comment away.",{x:M,y:6.6,w:11.9,h:0.5,fontFace:SANS,fontSize:13,italic:true,color:GOLD});

pres.writeFile({ fileName: "week-02-lecture-draft.pptx" }).then(()=>console.log("written"));
