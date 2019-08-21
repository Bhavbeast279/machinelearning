class Population {
    constructor(lifeSpan, popSize, reward, punishment, newPopulation){
        this.lifeSpan = lifeSpan;
        this.popSize = popSize;
        this.punishment = punishment;
        this.reward = reward;
        this.successRate = 0;

        this.food = new Food(width/2, 50, 30);
        this.wall = new Wall(width/2, height - height/3, 300, 30);

        this.flies = [];
        this.pool = [];

        if (newPopulation === undefined){
            for(let i = 0; i < this.popSize; i++){
                this.flies[i] = new Fly(this.lifeSpan, this.reward, this.punishment, this.food);
            }
        }else{
            this.flies = newPopulation;
        }
    }

    evaluate(){
        let maxFit = 0;
        for(let i = 0; i < this.popSize; i++){

            if(this.flies [i].gotFood){
                this.successRate += 1;
            }

            if (this.flies[i].fitness > maxFit){
                maxFit = this.flies[i].fitness;
            }
        }

        this.successRate = ((this.successRate/this.popSize) * 100).toFixed(1);

        for(let i = 0; i < this.popSize; i++){
            let poolRank = int(this.flies[i].fitness / maxFit * 40)

            for(let j = 0; j < poolRank; j++){
                this.pool.push(this.flies[i]);
            }
        }
    }

    findAverageFitness(){
        let totalFitness = 0;
        for(let i = 0; i < this.popSize; i++){
            totalFitness += this.flies[i].fitness;
        }
        return totalFitness/this.popSize.toFixed(20);
    }

    generateNewPopulation(mutationRate){
       
        let newFlies = [];
      
        for(let i = 0; i < this.popSize; i++){
            
            let newFly = new Fly(this.lifeSpan, this.reward, this.punishment, this.food);
           
            let randomA = int(random(0, this.pool.length));
            let randomB = int(random(0, this.pool.length));
            
            let parentA = this.pool[randomA];
            let parentB = this.pool[randomB];
            
            newFly.dna.generateMergedDNA(mutationRate, parentA, parentB);
            newFlies.push(newFly);

            
        }
        return newFlies;
    }

    run(count){
        this.food.show();
        this.wall.show();
        for(let i = 0; i < this.popSize; i++){
            this.flies[i].update(count, this.wall);
            this.flies[i].show();
        }
    }
}