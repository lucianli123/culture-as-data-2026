// Week 3 lecture draft deck: logistic regression + classification.
//
// Figures and numbers come from slides/week03_figs.py, which fits the models on the
// same corpus the group-work notebook loads. Run that first; this script reads its
// PNGs and week03_figs.json out of $FIG_DIR (default /tmp/figs), so every number on
// a slide is one the code produced, not one anyone typed.
//
//   python3 slides/week03_figs.py && node slides/week03_deck_build.js
//
// The committed .pptx is a snapshot of one run; the corpus is live, so re-running
// moves the numbers a point or two. Re-run both before teaching.
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");

const F = (process.env.FIG_DIR || "/tmp/figs") + "/";
const facts = JSON.parse(fs.readFileSync(F + "week03_figs.json", "utf8"));
const A = facts.label_a, B = facts.label_b;
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
function caption(s,t){ s.addText(t,{x:M,y:6.85,w:11.9,h:0.4,fontFace:SANS,fontSize:11,italic:true,color:MUTED}); }

// 1 title
let s=base(true);
s.addText("CULTURE AS DATA · WEEK 3",{x:M,y:0.7,w:8,h:0.3,fontFace:SANS,fontSize:13,color:GOLD,bold:true,charSpacing:3});
s.addText("Classification:",{x:M,y:2.0,w:11.5,h:1.0,fontFace:SERIF,fontSize:48,bold:true,color:WHITE});
s.addText("Counting with Weights",{x:M,y:2.95,w:11.5,h:1.0,fontFace:SERIF,fontSize:48,bold:true,color:CREAM});
s.addText(`Modelling in practice: one model built live on r/${A} against r/${B},\nthen yours, in threes, in the blank notebook`,
 {x:M,y:4.5,w:10.5,h:1.1,fontFace:SANS,fontSize:17,italic:true,color:CREAM,lineSpacingMultiple:1.25});
[GOLD,GREEN,CREAM].forEach((c,i)=>s.addShape("ellipse",{x:11.3+i*0.42,y:0.62,w:0.22,h:0.22,fill:{color:c},line:{type:"none"}}));

// 2 the arc
s=base(); kicker(s,"TODAY",TERRA); title(s,"One method, four questions, then your turn");
[["1","The article, argued","Underwood's genres: what did he count, and who labelled it?",TERRA],
 ["2","What a classifier is","Every word votes; the model learns the weights and adds them up",GREEN],
 ["3","Would you believe the score?","Baseline, held-out rows, and the shape of the errors",BLUE],
 ["4","What did it learn?","Signed weights: topic, register, or community habit",GOLD],
 ["5","What goes wrong","Memorising, imbalance, leakage, and no box for “neither”",TERRA],
 ["6","Your model","Threes, one screen, a workbench, and one decision changed at a time",GREEN]].forEach((st,i)=>{
  const col=i%2,row=Math.floor(i/2),x=M+col*6.2,y=2.15+row*1.55;
  s.addShape("roundRect",{x,y,w:5.9,h:1.3,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addShape("ellipse",{x:x+0.25,y:y+0.33,w:0.62,h:0.62,fill:{color:st[3]},line:{type:"none"}});
  s.addText(st[0],{x:x+0.25,y:y+0.33,w:0.62,h:0.62,fontFace:SERIF,fontSize:20,bold:true,color:WHITE,align:"center",valign:"middle"});
  s.addText(st[1],{x:x+1.05,y:y+0.16,w:4.7,h:0.45,fontFace:SANS,fontSize:16,bold:true,color:INK,margin:0});
  s.addText(st[2],{x:x+1.05,y:y+0.6,w:4.7,h:0.6,fontFace:SANS,fontSize:12.5,color:MUTED,margin:0,valign:"top"});
});

// 3 discussion opener
s=base(); kicker(s,"DISCUSSION · YOU READ IT, YOU ARGUE IT",GREEN);
title(s,"Underwood, “The Life Cycles of Genres” (2016)");
qcards(s,[["What did he actually count? Name the unit, the features, and the span of years before anyone defends or attacks the finding.",TERRA],
 ["Who decided which novels were detective fiction, and on what evidence? Where in the paper is that decision visible?",GOLD],
 ["The model misreads Pynchon's The Crying of Lot 49, a detective-fiction spoof. Is that a failure of the model, or a finding about genre?",GREEN],
 ["What would have to be true for you to believe the figures? Name the one check you would want run.",BLUE]],2.1,1.28,13.5);

// 4 Underwood in detail
s=base(); kicker(s,"THE FEATURED STUDY",TERRA); title(s,"A logistic regression, on a century of novels");
bullets(s,["Underwood trained the exact tool of today's session to recognise detective fiction and science fiction, then used it to trace how those genres consolidated.",
 "The labels came from human judgment: shelf lists, reviews, a scholar's reading. What counts as science fiction is a choice made before any modelling.",
 "Open data and code on Zenodo. You can rerun his argument, which is the standard this course holds you to as well."]);
s.addShape("roundRect",{x:6.6,y:2.2,w:6.0,h:3.9,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("the misread, and why it is the best part",{x:6.9,y:2.45,w:5.4,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
s.addText("“The Crying of Lot 49”",{x:6.9,y:2.95,w:5.4,h:0.5,fontFace:SERIF,fontSize:20,bold:true,color:TERRA,margin:0});
s.addText("The classifier calls Pynchon's novel detective fiction. Critics call it a detective-fiction spoof — which means the machine read the surface correctly and the joke not at all.",
 {x:6.9,y:3.5,w:5.4,h:1.4,fontFace:SANS,fontSize:13.5,color:INK,margin:0,valign:"top",lineSpacingMultiple:1.15});
s.addText("Genre boundaries are real but fuzzy. The error showed that; the accuracy could not.",
 {x:6.9,y:5.1,w:5.4,h:0.8,fontFace:SERIF,fontSize:14,italic:true,color:GREEN,margin:0});
caption(s,"Carry this into the second hour: where would YOUR classifier fail, and what would that failure teach you?");

// 5 counting with weights
s=base(); kicker(s,"THE IDEA",GREEN); title(s,"A classifier is counting, with weights");
bullets(s,["Every word casts a vote, for or against. The model adds the votes up. That is the whole mechanism.",
 "Training means learning one weight per word from labelled examples — a few thousand numbers, tuned until the votes come out right.",
 "Nothing understands anything. Spam filters have worked this way for twenty years.",
 "The words you hand it are the only evidence it has. Sarcasm, tone, and irony are not in the bag."],{w:5.6});
s.addShape("roundRect",{x:6.6,y:2.2,w:6.0,h:4.0,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("six sentences, two piles (the notebook's warm-up)",{x:6.9,y:2.45,w:5.4,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
[["tide, sand, shore","→ sea",GREEN],["butter, bread, pasta","→ kitchen",TERRA],
 ["“in” (once each side)","weight ≈ 0.01",MUTED],["“salt” vs “salted”","two columns, opposite ways",BLUE]].forEach((r,i)=>{
  s.addText(r[0],{x:6.9,y:3.0+i*0.78,w:3.2,h:0.6,fontFace:SERIF,fontSize:15,italic:true,color:INK,margin:0,valign:"middle"});
  s.addText(r[1],{x:10.1,y:3.0+i*0.78,w:2.3,h:0.6,fontFace:SANS,fontSize:13,bold:true,color:r[2],margin:0,valign:"middle"});
});
caption(s,"Uninformative words earn small weights by themselves. And the model has no idea that salt and salted are the same word — Week 2's argument, now visible as two numbers.");

// 6 the sigmoid
s=base(); kicker(s,"FROM VOTES TO A DECISION",BLUE); title(s,"The weighted sum, squeezed into a probability");
bullets(s,["Add the weights of the words present. That sum is one number on the horizontal axis, and it can be anything.",
 "The logistic curve squeezes it into 0–1, which is where the name comes from.",
 "Above 0.5 it answers one way, below the other. The threshold is a choice, not a law: move it when one kind of error costs more than the other.",
 "A probability is not a confidence. The curve will hand you 0.85 on a sentence about nothing at all."],{w:5.4});
fig(s,"w3_sigmoid.png",6.4,2.1,6.2,4.3);

// 7 what fitting does
s=base(); kicker(s,"WHAT TRAINING ACTUALLY DOES",TERRA); title(s,"Four lines, and the search inside them");
s.addShape("roundRect",{x:M,y:2.15,w:11.9,h:1.75,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("X = CountVectorizer().fit_transform(df[\"text\"])      # text  → a matrix of word counts\ny = (df[\"label\"] == \"" + A + "\").astype(int)           # labels → 0 and 1\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)\nclf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)   # the search happens here",
 {x:M+0.3,y:2.35,w:11.3,h:1.4,fontFace:MONO,fontSize:12.5,color:INK,margin:0,lineSpacingMultiple:1.25});
bullets(s,["The search: find the set of weights that leans the right way for as many TRAINING documents as possible.",
 `Our corpus: ${facts.n_rows} documents, ${facts.n_features.toLocaleString()} word-columns after dropping words that appear once.`,
 "More columns than documents, which is why the next slide about held-out data is not a technicality."],{y:4.15,w:5.6,h:2.1});
s.addShape("roundRect",{x:6.6,y:4.15,w:6.0,h:2.1,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("the one line people skip",{x:6.9,y:4.35,w:5.4,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
s.addText("train_test_split",{x:6.9,y:4.75,w:5.4,h:0.45,fontFace:MONO,fontSize:16,bold:true,color:TERRA,margin:0});
s.addText("A quarter of the rows are set aside before any fitting, and never looked at until the score. Skip it and you are measuring memory.",
 {x:6.9,y:5.25,w:5.4,h:0.9,fontFace:SANS,fontSize:13,color:INK,margin:0,valign:"top"});

// 8 the 2-D view
s=base(); kicker(s,"WHY THE NUMBER IS WHAT IT IS",GOLD); title(s,"Two communities, one city, heavily overlapping");
fig(s,"w3_boundary.png",M,2.1,6.6,4.4);
bullets(s,[`Every document is a point in ${facts.n_features.toLocaleString()}-dimensional word-space. Here it is flattened to the two directions that carry the most variation.`,
 `The two piles sit on top of each other. The best straight line in this flattened view gets ${pct(facts.boundary_accuracy_2d)} right.`,
 `With all ${facts.n_features.toLocaleString()} columns the model reaches ${pct(facts.accuracy)} — better, because the separating evidence lives in directions this picture cannot show.`,
 "A hard pair is the honest case. Two unrelated subreddits would split cleanly and teach you nothing you didn't already know."],{x:7.5,w:5.1,fontSize:14});

// 9 baseline
s=base(); kicker(s,"QUESTION 1 · COMPARED TO WHAT?",TERRA); title(s,"An accuracy alone means nothing");
fig(s,"w3_baseline.png",M,2.1,6.4,4.3);
bullets(s,[`A model that always guesses the bigger pile scores ${pct(facts.baseline)} here, having read nothing. That is the floor.`,
 `Ours lands at ${pct(facts.accuracy)} on rows it never saw: real, and modest.`,
 `Refit on five different splits it averages ${facts.cv_mean.toFixed(2)} ± ${facts.cv_std.toFixed(2)} — so a two-point difference between two models is inside the noise.`,
 "Report the floor next to the score, always. A number without its baseline is a number designed not to be checked."],{x:7.4,w:5.2,fontSize:14});

// 10 confusion
s=base(); kicker(s,"QUESTION 2 · WHICH ERRORS?",GREEN); title(s,"The same accuracy, two different animals");
fig(s,"w3_confusion.png",M,2.1,5.6,4.4);
bullets(s,["Rows are the truth, columns are what the model said. The diagonal is right; the other two cells are the mistakes.",
 `Here: ${facts.confusion.true_a_said_b} comments from r/${A} called r/${B}, and ${facts.confusion.true_b_said_a} the other way. Roughly even, which is the healthy shape.`,
 "A model at the same accuracy that called almost everything one side would be a different thing entirely: it found the bigger pile, not the difference.",
 "classification_report says the same in precision and recall, one row per side."],{x:6.9,w:5.7,fontSize:14});

// 11 overfitting
s=base(); kicker(s,"WHAT GOES WRONG · 1",BLUE); title(s,"Memorising is not reading");
fig(s,"w3_regularisation.png",M,2.1,6.4,4.3);
bullets(s,[`Turn C up and the model trusts the training data harder. At C=${facts.c_high.C} it scores ${pct(facts.c_high.train)} on rows it trained on and ${pct(facts.c_high.test)} on rows it didn't.`,
 "The blue line is memory. The terracotta line is reading. The gap between them is overfitting, drawn.",
 `Best held-out score here: ${pct(facts.c_best.test)} at C=${facts.c_best.C}. Note it is not at the far right.`,
 "This is why the score you quote must come from data the model never saw. On this corpus the difference is forty points."],{x:7.4,w:5.2,fontSize:14});

// 12 how much data
s=base(); kicker(s,"WHAT GOES WRONG · 2",GOLD); title(s,"One number is luck; the curve is the story");
fig(s,"w3_learning.png",M,2.1,6.4,4.3);
bullets(s,["Accuracy against how many documents the model was allowed to train on, five draws at each size.",
 "The band is best-to-worst across those draws. At small sizes it is wide enough to swallow most of the finding.",
 "Useful before Week 4: more data helps, and it stops helping. Knowing where it flattens tells you how much collecting is worth doing.",
 "If your result moves when you re-run it, you are reporting the draw, not the corpus."],{x:7.4,w:5.2,fontSize:14});

// 13 read the weights
s=base(); kicker(s,"READ ITS MIND",TERRA); title(s,"The signed weights, all of them, on the table");
fig(s,"w3_weights.png",M,2.1,6.2,4.6);
bullets(s,["One number per word. Positive pushes one way, negative the other, and you can read every one of them.",
 `Most r/${A}: ${facts.top_a.slice(0,5).join(", ")}.`,
 `Most r/${B}: ${facts.top_b.slice(0,5).join(", ")}.`,
 "A big weight is not proof of a big pattern: a rare word that happens to fall on one side gets a large coefficient. Check how many documents it is actually in.",
 "Week 7's annotator is far more powerful and will not let you do any of this."],{x:7.2,w:5.4,fontSize:14});

// 14 topic / register / habit
s=base(); kicker(s,"THE READING, NOT THE SCORE",GREEN); title(s,"Three kinds of word, three different claims");
[["Topic","The two piles talk about different things.\nbeaches · lebron · espresso","Often the boring answer: you knew the subjects differed before you started.",TERRA],
 ["Register","The two piles talk in different styles.\ncitation · lol · therefore","The more interesting claim: same subject, different voice.",BLUE],
 ["Habit","The two piles have different rituals.\nthis sub · mods · OP · edit","A finding about community, not language. Also the easiest to over-read.",GREEN]].forEach((c,i)=>{
  const x=M+i*4.15;
  s.addShape("roundRect",{x,y:2.2,w:3.9,h:3.9,fill:{color:TINT},line:{type:"none"},rectRadius:0.12});
  s.addShape("ellipse",{x:x+0.35,y:2.55,w:0.55,h:0.55,fill:{color:c[3]},line:{type:"none"}});
  s.addText(String(i+1),{x:x+0.35,y:2.55,w:0.55,h:0.55,fontFace:SERIF,fontSize:18,bold:true,color:WHITE,align:"center",valign:"middle"});
  s.addText(c[0],{x:x+0.35,y:3.3,w:3.2,h:0.5,fontFace:SERIF,fontSize:19,bold:true,color:INK,margin:0});
  s.addText(c[1],{x:x+0.35,y:3.85,w:3.25,h:1.1,fontFace:SANS,fontSize:13,color:INK,valign:"top",lineSpacingMultiple:1.18,margin:0});
  s.addText(c[2],{x:x+0.35,y:5.0,w:3.25,h:1.0,fontFace:SANS,fontSize:12.5,italic:true,color:MUTED,valign:"top",margin:0});
});
caption(s,"Sort your top ten into these three before you say what the model found. The sort IS the finding; the accuracy is the ticket to make it.");

// 15 the four failures
s=base(); kicker(s,"WHAT GOES WRONG, NAMED",TERRA); title(s,"Four ways a classifier flatters you");
[["Scoring on itself","Report accuracy on the training rows and you have measured memory. With more columns than documents it can hit 100 percent and mean nothing.",TERRA],
 ["Imbalance","Nine parts A to one part B: guess A every time and you are 90 percent “accurate.” Always print the baseline, and reach for class_weight=\"balanced\".",GOLD],
 ["Leakage","A giveaway feature you never meant to hand it: the subreddit's own name, a bot's template, a scraping artifact. Accuracy near 1.00 is a red flag, not a triumph.",BLUE],
 ["No “neither” box","Two boxes and no way to abstain. Hand it Shakespeare and it answers confidently anyway. Every classifier you meet has this property.",GREEN]].forEach((t,i)=>{
  s.addShape("roundRect",{x:M,y:2.15+i*1.2,w:11.9,h:1.05,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addText(t[0],{x:M+0.35,y:2.22+i*1.2,w:2.5,h:0.9,fontFace:SERIF,fontSize:17,bold:true,color:t[2],valign:"middle",margin:0});
  s.addText(t[1],{x:M+3.0,y:2.22+i*1.2,w:8.6,h:0.9,fontFace:SANS,fontSize:13,color:INK,valign:"middle",margin:0});
});
caption(s,"Three of the four are invisible in the accuracy number. That is the argument for reading the weights and the errors, every time.");

// 16 teachable machine
s=base(); kicker(s,"SIXTY SECONDS, LIVE",GOLD); title(s,"Bias is not a ghost in the machine");
bullets(s,["Teachable Machine, two classes, trained in the browser while you watch: cats and dogs.",
 "The reveal: it only ever saw orange cats and brown dogs.",
 "Predict, out loud, before the test: what does it say about a black cat?",
 "It learned colour, because colour was what separated the piles it was given. It was never asked to learn what a cat is."],{w:6.0});
s.addShape("roundRect",{x:7.0,y:2.2,w:5.6,h:3.4,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
s.addText("the sentence to remember",{x:7.3,y:2.45,w:5.0,h:0.35,fontFace:SANS,fontSize:12,bold:true,color:MUTED,charSpacing:2});
s.addText("The bias is the training set,\nand you assembled it.",{x:7.3,y:2.95,w:5.0,h:1.0,fontFace:SERIF,fontSize:22,bold:true,color:TERRA,margin:0,lineSpacingMultiple:1.15});
s.addText("Your two piles were also a choice. Which comments the archive kept, which the moderators removed, which users post at all — each of those is in your weights.",
 {x:7.3,y:4.1,w:5.0,h:1.3,fontFace:SANS,fontSize:13.5,color:INK,margin:0,valign:"top",lineSpacingMultiple:1.15});
caption(s,"For image projects: this IS a classifier on pixels. Same move, different features.");

// 17 group work
s=base(); kicker(s,"YOUR TURN · 32 MINUTES",GREEN); title(s,"Threes, one screen, stations not answers");
[["Driver","types, and prompts the AI — never a line nobody has read aloud",TERRA],
 ["Reader","says what the cell will do before it runs, then whether it did",BLUE],
 ["Skeptic","asks: is that better than guessing? would that word survive elsewhere?",GREEN]].forEach((r,i)=>{
  const x=M+i*4.15;
  s.addShape("roundRect",{x,y:2.15,w:3.9,h:1.45,fill:{color:TINT},line:{type:"none"},rectRadius:0.1});
  s.addText(r[0],{x:x+0.3,y:2.3,w:3.3,h:0.4,fontFace:SERIF,fontSize:18,bold:true,color:r[2],margin:0});
  s.addText(r[1],{x:x+0.3,y:2.72,w:3.3,h:0.8,fontFace:SANS,fontSize:12.5,color:INK,margin:0,valign:"top"});
});
s.addText("Rotate at every station.",{x:M,y:3.65,w:11.9,h:0.3,fontFace:SANS,fontSize:12,italic:true,color:MUTED});
[["0–1","warm-up (written for you), your question, your prediction"],
 ["2–3","features, then fit"],
 ["4","judge it: baseline, held-out, confusion matrix"],
 ["5","read the weights, and sort them: topic / register / habit"],
 ["6","break it: three inputs from neither pile, one real error read in full"],
 ["7","the workbench: sweep min_df · tf-idf · bigrams · C · class_weight into one table"],
 ["8 or 9","interrogate a weight (how many PEOPLE wrote it?) — or swap in your own two subreddits"],
 ["10","report back: ninety seconds"]].forEach((r,i)=>{
  s.addText(r[0],{x:M+0.1,y:4.1+i*0.4,w:0.9,h:0.35,fontFace:SANS,fontSize:13,bold:true,color:TERRA,margin:0});
  s.addText(r[1],{x:M+1.1,y:4.1+i*0.4,w:10.6,h:0.35,fontFace:SANS,fontSize:13.5,color:INK,margin:0});
});
caption(s,"Behind schedule? Stations 4, 5 and 7 are the ones that must happen. One model is a result; several are an argument — and 8 and 9 are where the homework starts.");

// 18 discussion, after the build
s=base(); kicker(s,"DISCUSSION · AFTER THE BUILD",BLUE); title(s,"What did your model actually measure?");
qcards(s,[["Your top words: topic, register, or habit? What claim about these communities does each kind license — and which one were you hoping for?",TERRA],
 ["Your accuracy beat the baseline by a few points. What is the honest one-sentence finding, and what would a critic say to it?",GOLD],
 ["You changed one decision and the words changed but the score didn't. Which model do you report, and how do you justify the choice in writing?",GREEN],
 ["Underwood's misread taught something his accuracy could not. What did YOUR errors teach about the categories you chose?",BLUE]],2.1,1.28,13.5);

// 19 homework
s=base(true); kicker(s,"BEFORE WEEK 4",GOLD);
s.addText("Homework",{x:M,y:1.0,w:11,h:0.8,fontFace:SERIF,fontSize:34,bold:true,color:WHITE});
[["Sketch","Take one of today's models to a labelled set you care about. Screenshot its five most positive and five most negative words — do they make sense?",GOLD],
 ["Corpus existence proof","A screenshot showing you can load 50 rows of the data you want to use. The cookbook notebook works now; Week 4 teaches the how. No proof, no pitch.",GREEN],
 ["Check (AI closed)","Read your classifier's top weights aloud — what did it learn — and name one input where it would fail, and why.",CREAM]].forEach((r,i)=>{
  s.addShape("ellipse",{x:M,y:2.25+i*1.45,w:0.24,h:0.24,fill:{color:r[2]},line:{type:"none"}});
  s.addText(r[0],{x:M+0.45,y:2.1+i*1.45,w:11,h:0.4,fontFace:SANS,fontSize:15,bold:true,color:r[2],margin:0});
  s.addText(r[1],{x:M+0.45,y:2.5+i*1.45,w:10.8,h:0.95,fontFace:SANS,fontSize:14,color:CREAM,valign:"top",margin:0});
});
s.addText("Next week: pick a corpus, pick two methods, commit. Bring the pitch and the 50 rows.",{x:M,y:6.6,w:11.9,h:0.5,fontFace:SANS,fontSize:13,italic:true,color:GOLD});

pres.writeFile({ fileName: path.join(__dirname, "week-03-lecture-draft.pptx") })
    .then(()=>console.log("written: slides/week-03-lecture-draft.pptx"));
