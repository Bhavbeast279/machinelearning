class Fly {
    constructor(lifeSpan, reward, punishment, food) {
        this.pos = createVector(width/2, height - 40);
        this.acc = createVector();
        this.vel = createVector ();
        this.dna = new DNA(lifeSpan);
        this.reward = reward;
        this.punishment = punishment;
        this.food = food;
        this.fitness = 0;
        this.hitSomething = false;
        this.gotFood = false;
    }

    
    calcFitness(){
        // fitness
        let distance = dist(this.pos.x, this.pos.y, this.food.pos.x, this.food.pos.y)
        this.fitness = map(distance, 0, width, width, 0)

        // Apply Modifiers
        if(distance <= this.food.radius){
            this.fitness *= this.reward;
        }

        if(this.hitSomething){
            this.fitness /= this.punishment
        }
    }
    update(count, wall){
        if(!this.hitSomething){
            this.applyForce(this.dna.genes[count]);
            this.vel.add(this.acc);
            this.pos.add(this.vel);
            this.acc.mult(0);
        }
        // Hit edges
        if(this.pos.y > height || this.pos.y < 0 || this.pos.x > width || this.pos.x < 0){
            this.hitSomething = true;
        }
        // Hit Wall
        if (wall.hitWall(this.pos.x, this.pos.y)){
            this.hitSomething = true;
        }
        // Check Food
        let distance = dist(this.pos.x, this.pos.y, this.food.pos.x, this.food.pos.y);
        if(distance < this.food.radius){
            this.gotFood = true;
            this.hitSomething = true;
        }

        this.calcFitness();
    }
    applyForce(force){
        this.acc.add(force);
    }
    show(){
        push();
        noStroke();
        translate(this.pos.x, this.pos.y);
        fill(0);
        textSize(10);
        text(this.fitness.toFixed(1), 0, 0);
        rotate(this.vel.heading());
        fill(255, 0, 0, 150);
        rectMode(CENTER);
        rect(0, 0, 40, 15);
        pop()
    }
}