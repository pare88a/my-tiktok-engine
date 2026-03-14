export default async function handler(req, res) {

const { url } = req.query;

if(!url){
return res.status(400).json({error:"Video URL required"});
}

// YouTube block
if(url.includes("youtube.com") || url.includes("youtu.be")){
return res.status(403).json({error:"YouTube download not allowed"});
}

try{

const response = await fetch(url,{
headers:{
"User-Agent":"Mozilla/5.0"
}
});

const html = await response.text();

// TikTok video link extract
const match = html.match(/"playAddr":"(.*?)"/);

if(!match){
return res.status(404).json({error:"Video not found"});
}

let video = match[1].replace(/\\u0026/g,"&");

res.status(200).json({
download:video
});

}catch(e){

res.status(500).json({error:"Server error"});

}

}
