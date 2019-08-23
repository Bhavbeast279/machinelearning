class Cactus {
    constructor() {
        this.count = random(0, 4); 
        this.speed = 5; 
        this.width = 20;
        this.height = 50;
        this.pos = createVector(width + this.width + this.width/2, height - height/4 - this.height/2);
        this.spacing = 5;
        
        this.fullWidth = (this.width + this.spacing) * this.count - this.spacing;
    }

    update() {
        this.pos.x -= this.speed;
    }

    show() {
        for (let i = 0; i < this.count; i++) {
            push();
            noStroke();
            translate(this.pos.x + (this.width + this.spacing) * i, this.pos.y);
            fill(0 ,200,0);
            rectMode(CENTER);
            rect(0, 0, this.width, this.height);
            pop();
        }
    }
}