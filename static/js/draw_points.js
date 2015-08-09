function draw(canvas_id,data,scaling){
    if (scaling == undefined){
        scaling = 1;
    }
    var canvas = document.getElementById(canvas_id);
    var context = canvas.getContext('2d');

    prepare_painting(canvas,context,data,scaling);
    draw_axes(canvas,context);
    draw_points(canvas,context,data,scaling);
};

function auto_skaling(canvas_id,data,scaling){
    var canvas = document.getElementById(canvas_id);
    var x_max = data[0].x * scaling;
    var x_min = data[0].x * scaling;
    var y_max = data[0].y * scaling;
    var y_min= data[0].y * scaling;
    for( var i in data){
        var x = data[i].x * scaling;
        var y = data[i].y * scaling;
        x_max = x_max < x ? x : x_max;
        x_min = x_min > x ? x : x_min;
        y_max = y_max < y ? y : y_max;
        y_min = y_min > y ? y : y_min;
    }
    var w_max = Math.abs(x_max) < Math.abs(x_min) ? Math.abs(x_min) : Math.abs(x_max);
    w_max=(w_max* 2);

    var h_max = Math.abs(y_max) < Math.abs(y_min) ? Math.abs(y_min) : Math.abs(y_max);
    h_max=(h_max* 2);
    var s_w = canvas.width / w_max;
    var s_h = canvas.height / h_max;
    return s_w < s_h ? s_w : s_h;
}

function prepare_painting(canvas,context,data,scaling){
    canvas.width = 500;
    canvas.height = 300;
    var x_max = canvas.width /2 - 10;
    var x_min = canvas.width/-2 + 10;
    var y_max = canvas.height/2 - 10;
    var y_min= canvas.height/-2 + 10;
    for( var i in data){
        var x = data[i].x * scaling;
        var y = data[i].y * scaling;
        x_max = x_max < x ? x : x_max;
        x_min = x_min > x ? x : x_min;
        y_max = y_max < y ? y : y_max;
        y_min = y_min > y ? y : y_min;
    }
    var w_max = Math.abs(x_max) < Math.abs(x_min) ? Math.abs(x_min) : Math.abs(x_max);
    w_max=(w_max* 2) + 20;

    var h_max = Math.abs(y_max) < Math.abs(y_min) ? Math.abs(y_min) : Math.abs(y_max);
    h_max=(h_max* 2) + 20;

    canvas.width = w_max;
    canvas.height = h_max;
};

function draw_points(canvas,context,data,scaling){
    var width  = canvas.width;
    var height = canvas.height; 
    for( var i in data){
        context.beginPath();
        if ('color' in data[i])
            context.fillStyle = data[i].color;
        else
            context.fillStyle = 'black';
        var x =data[i].x * scaling + width/2;
        var y = height/2 - data[i].y * scaling ;
        context.arc(x,y,3,0,2*Math.PI,false);
        context.fill();   
        context.closePath();  
    }        
}

function draw_axes(canvas,context){
    var width  = canvas.width;
    var height = canvas.height;
    context.beginPath();
    context.moveTo(0,height/2);
    context.lineTo(width,height/2);
    context.lineTo(width - 10,height/2 -8);
    context.moveTo(width,height/2);
    context.lineTo(width - 10,height/2 +8);

    context.moveTo(width/2,height);
    context.lineTo(width/2,0);
    context.lineTo(width/2 - 8,10);
    context.moveTo(width/2,0);
    context.lineTo(width/2 + 8,10);
    context.stroke();
    context.closePath();


    context.textBaseline = "top";
    context.font = "bold 15px Arial";
    context.fillStyle = "red";
    context.fillText("PC1", width - 42,height/2 +10);
    context.fillText("PC2", width/2 - 40,13);
}