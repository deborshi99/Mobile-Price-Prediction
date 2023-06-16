function GoToPredict(page_name) {
    if(page_name === "predict"){
        location.replace("./predict_price.html")
    }else if(page_name === "about"){
        location.replace("./about.html")
    }else if(page_name === "source_code"){
        location.replace("./source_code.html")
    }
    
}

tags = ['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
'touch_screen', 'wifi']


function onclick(){
  results = {}
  for(i=0; i<=tags.lenght; i++){
    var datuml = tags[i];    
    if(!results[datuml.key]){
        results[datuml.key]=[];
    }
    var value = document.getElementById(tags[i])
    results[datuml.key].push(value);
  }
  return results
}

console.log(onclick())


