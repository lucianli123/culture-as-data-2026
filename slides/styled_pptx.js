// Styled weekly decks for Culture as Data. Reads /tmp/slides.json, writes slides/pptx/.
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const weeks = JSON.parse(fs.readFileSync(require("path").join(__dirname,"slides.json"),"utf8"));
const OUT = require("path").join(__dirname,"pptx");

const TERRA="7A3B2E", TERRA_DK="4E261D", INK="1A1A1A", MUTED="6B6B63",
      GREEN="3F6F5F", GOLD="B9852F", TINT="F4EEE8", WHITE="FFFFFF", CREAMTX="E8DCD6";
const SERIF="Cambria", SANS="Calibri";
const HUES=[TERRA, GREEN, GOLD];

function dotScatter(slide, x, y, w, h, n, seed){
  // deterministic pseudo-random scatter of small dots in 3 hues (the "map of meaning" motif)
  let s=seed;
  const rnd=()=>{ s=(s*9301+49297)%233280; return s/233280; };
  for(let i=0;i<n;i++){
    const cx=x+rnd()*w, cy=y+rnd()*h, r=0.05+rnd()*0.06;
    slide.addShape("ellipse",{x:cx,y:cy,w:r,h:r,fill:{color:HUES[i%3]},line:{type:"none"}});
  }
}
function triDots(slide, x, y){
  HUES.forEach((c,i)=>slide.addShape("ellipse",{x:x+i*0.26,y:y+(i%2?0.1:0),w:0.16,h:0.16,fill:{color:c},line:{type:"none"}}));
}

function build(w){
  const pres=new pptxgen();
  pres.defineLayout({name:"W",width:13.333,height:7.5});
  pres.layout="W";
  const M=0.7, PW=13.333;

  // ---------- 1. Title (dark) ----------
  let s=pres.addSlide(); s.background={color:TERRA_DK};
  s.addText("CULTURE AS DATA",{x:M,y:0.55,w:8,h:0.3,fontFace:SANS,fontSize:13,color:GOLD,bold:true,charSpacing:3});
  s.addText(`Week ${w.n}`,{x:M,y:1.7,w:6,h:0.6,fontFace:SANS,fontSize:20,color:CREAMTX});
  s.addText(w.title,{x:M,y:2.2,w:9.8,h:2.0,fontFace:SERIF,fontSize:40,bold:true,color:WHITE,valign:"top",autoFit:true});
  s.addText(w.promise,{x:M,y:4.5,w:8.4,h:1.6,fontFace:SANS,fontSize:16,italic:true,color:CREAMTX,valign:"top",autoFit:true});
  s.addText(`Tool / method:  ${w.tool}`,{x:M,y:6.6,w:11,h:0.4,fontFace:SANS,fontSize:12,color:GOLD});
  dotScatter(s, 9.7, 0.7, 3.0, 1.9, 16, w.n*37+5);

  // ---------- 2. Look at This (light, two-column) ----------
  s=pres.addSlide(); s.background={color:WHITE};
  s.addShape("ellipse",{x:M,y:1.5,w:2.6,h:2.6,fill:{color:TINT},line:{type:"none"}});
  triDots(s, M+0.75, 2.65);
  s.addText("LOOK AT THIS",{x:4.0,y:1.0,w:8,h:0.35,fontFace:SANS,fontSize:13,bold:true,color:GOLD,charSpacing:3});
  s.addText("The study we open with",{x:4.0,y:1.4,w:8.6,h:0.8,fontFace:SERIF,fontSize:30,bold:true,color:INK});
  s.addText(w.admire,{x:4.0,y:2.5,w:8.6,h:3.6,fontFace:SANS,fontSize:19,color:INK,valign:"top",lineSpacingMultiple:1.15,autoFit:true});

  // ---------- 3. Question It (light) ----------
  s=pres.addSlide(); s.background={color:WHITE};
  s.addText("QUESTION IT",{x:M,y:0.9,w:8,h:0.35,fontFace:SANS,fontSize:13,bold:true,color:TERRA,charSpacing:3});
  s.addText("What did they choose, and where might it be wrong?",{x:M,y:1.3,w:11.9,h:1.0,fontFace:SERIF,fontSize:26,bold:true,color:INK,autoFit:true});
  s.addShape("ellipse",{x:M,y:2.7,w:0.28,h:0.28,fill:{color:GOLD},line:{type:"none"}});
  s.addText(w.interrogate,{x:M+0.5,y:2.5,w:11.2,h:4.0,fontFace:SANS,fontSize:20,color:INK,valign:"top",lineSpacingMultiple:1.2,autoFit:true});

  // ---------- 4. Three modes (light, three cards) ----------
  s=pres.addSlide(); s.background={color:WHITE};
  s.addText("Three modes today",{x:M,y:0.8,w:11,h:0.8,fontFace:SERIF,fontSize:30,bold:true,color:INK});
  s.addText("about a third of the session each",{x:M,y:1.55,w:11,h:0.4,fontFace:SANS,fontSize:14,italic:true,color:MUTED});
  const cards=[["Lecture / demo", w.tool, TERRA],
               ["Workshop", "Build hands-on on your own data.", GREEN],
               ["Discussion", "Interrogate the study, debate it, or critique each other's work.", GOLD]];
  const cw=3.7, gap=0.55, x0=M;
  cards.forEach((c,i)=>{
    const x=x0+i*(cw+gap);
    s.addShape("roundRect",{x,y:2.4,w:cw,h:3.6,fill:{color:TINT},line:{type:"none"},rectRadius:0.12});
    s.addShape("ellipse",{x:x+0.45,y:2.85,w:0.6,h:0.6,fill:{color:c[2]},line:{type:"none"}});
    s.addText(c[0],{x:x+0.4,y:3.7,w:cw-0.8,h:0.6,fontFace:SERIF,fontSize:21,bold:true,color:INK});
    s.addText(c[1],{x:x+0.4,y:4.35,w:cw-0.8,h:1.5,fontFace:SANS,fontSize:15,color:INK,valign:"top",lineSpacingMultiple:1.15,autoFit:true});
  });

  // ---------- 5. The session (light, timeline) ----------
  s=pres.addSlide(); s.background={color:WHITE};
  s.addText("The session",{x:M,y:0.7,w:11,h:0.8,fontFace:SERIF,fontSize:30,bold:true,color:INK});
  const rows=w.flow; const top=1.7, rh=Math.min(0.62,(6.6-top)/rows.length);
  const fs=rows.length>7?11:12.5;
  rows.forEach((r,i)=>{
    const y=top+i*rh;
    s.addShape("roundRect",{x:M,y:y+0.02,w:0.95,h:rh-0.12,fill:{color:TERRA},line:{type:"none"},rectRadius:0.06});
    s.addText(r.t,{x:M,y:y+0.02,w:0.95,h:rh-0.12,fontFace:SANS,fontSize:11,bold:true,color:WHITE,align:"center",valign:"middle"});
    s.addText(r.a,{x:M+1.15,y:y,w:10.55,h:rh,fontFace:SANS,fontSize:fs,color:INK,valign:"middle",autoFit:true});
  });

  // ---------- 6. Reading & homework (light, rows) ----------
  s=pres.addSlide(); s.background={color:WHITE};
  s.addText("Reading & homework",{x:M,y:0.7,w:11,h:0.8,fontFace:SERIF,fontSize:30,bold:true,color:INK});
  const items=[["Reading",w.reading,TERRA],["Supplement",w.supplement,GREEN],
               ["Sketch",w.sketch,GOLD],["Check (AI closed)",w.check,TERRA]];
  items.forEach((it,i)=>{
    const y=1.9+i*1.25;
    s.addShape("ellipse",{x:M,y:y+0.08,w:0.24,h:0.24,fill:{color:it[2]},line:{type:"none"}});
    s.addText(it[0],{x:M+0.45,y:y,w:11.4,h:0.4,fontFace:SANS,fontSize:15,bold:true,color:it[2]});
    s.addText(it[1],{x:M+0.45,y:y+0.42,w:11.4,h:0.8,fontFace:SANS,fontSize:14,color:INK,valign:"top",autoFit:true});
  });

  // ---------- 7. Closing (dark) ----------
  s=pres.addSlide(); s.background={color:TERRA_DK};
  s.addText("THE CHECK, AI CLOSED",{x:M,y:1.1,w:9,h:0.35,fontFace:SANS,fontSize:13,bold:true,color:GOLD,charSpacing:3});
  s.addText(w.check,{x:M,y:1.8,w:9.5,h:3.4,fontFace:SERIF,fontSize:26,color:WHITE,valign:"top",lineSpacingMultiple:1.15,autoFit:true});
  s.addText(`Culture as Data  ·  Week ${w.n}`,{x:M,y:6.7,w:8,h:0.4,fontFace:SANS,fontSize:12,color:CREAMTX});
  dotScatter(s, 9.9, 4.9, 2.8, 1.9, 14, w.n*53+11);

  const fn=`${OUT}/week-${String(w.n).padStart(2,"0")}.pptx`;
  return pres.writeFile({fileName:fn}).then(()=>console.log("wrote",fn));
}

(async()=>{ for(const w of weeks){ await build(w); } })();