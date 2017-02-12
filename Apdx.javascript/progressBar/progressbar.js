

function Progress(width, height, parent){
    this.parent = document.getElementById(parent) || document.body;
    this.div = document.createElement('div');
    this.div_span = document.createElement('span');
    this.div_div = document.createElement('div');
    this.div_div_span = document.createElement('span');
    this.div.className = "progress";
    this.div_span.className = "text";
    this.div_div.className = "bar";
    this.div_div_span.className = "text";
    
    this.div.appendChild(this.div_span);
    this.div.appendChild(this.div_div);
    this.div_div.appendChild(this.div_div_span);
    this.parent.appendChild(this.div);
    this.setSize(width, height);
    this.setPercent(0);
    
}

Progress.prototype.setSize = function(width, height){
    width = width || 300 ;
    height = height || 20;
    this.div.style.width = width + "px";
    this.div.style.height = height + "px";
    this.div_div_span.style.width = width + "px"; 
    this.div_span.style.lineHeight = height + "px";    
    this.div_div_span.style.lineHeight = height + "px";
};
Progress.prototype.setPercent = function(percent){
    this.div_span.innerHTML = percent + "%";
    this.div_div_span.innerHTML = percent + "%";
    this.div_div.style.width = percent + "%";
};