let ground;
function setup() {
    createCanvas(640, 480)
    ground = new Ground();
    
}
function draw() {
    background(255);
    ground.show();
}