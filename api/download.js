export default function handler(req, res) {

const url=req.query.url;

if(!url){
return res.status(400).json({error:"Video link required"});
}

// YouTube block
if(url.includes("youtube.com") || url.includes("youtu.be")){
return res.status(403).json({
error:"YouTube downloading not allowed"
});
}

// TikTok example response
res.json({
download:url
});

}
