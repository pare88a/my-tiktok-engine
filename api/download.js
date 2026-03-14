export default function handler(req, res) {

try {

const { url } = req.query;

if(!url){
res.status(400).json({error:"Video URL required"});
return;
}

// YouTube block
if(url.includes("youtube.com") || url.includes("youtu.be")){
res.status(403).json({error:"YouTube download not allowed"});
return;
}

res.status(200).json({
download:url
});

} catch(e){

res.status(500).json({error:"Server error"});

}

}
