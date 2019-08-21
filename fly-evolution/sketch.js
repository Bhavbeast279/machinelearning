const LIFE_SPAN = 1000; // life of the flies
const POP_SIZE = 500 // population size
const REWARD_MULT = 1000 // reward of finding food
const PUNISH_DIV = 3 // punshment for hitting stuff
const MUTATION_RATE = 0.1 // rates of fly mutation

let count = 0;
let generation = 0;
let averageFit = 0;
let successRate = 0;


function setup() {
    createCanvas(640, 480);

    population = new Population(LIFE_SPAN, POP_SIZE, REWARD_MULT, PUNISH_DIV);
}
function draw() {
    background(3, 252, 232);
    textSize(32);
    text("Generation: " + generation, 0, 50);
    text ("average fitness: " + averageFit, 0, 75)
    text("Success Rate: " + successRate + "%", 0, 100);
    population.run(count);
    count++;

    if(count == LIFE_SPAN){
        population.evaluate();
        averageFit = population.findAverageFitness();
        successRate = population.successRate;
        let newFlies = population.generateNewPopulation(MUTATION_RATE);
        population = new Population(LIFE_SPAN, POP_SIZE, REWARD_MULT, PUNISH_DIV, newFlies);
        count = 0;
        generation++;
    }
}