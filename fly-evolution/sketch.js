const LIFE_SPAN = 600; // life of the flies
const POP_SIZE = 500 // population size
const REWARD_MULTI = 10 // reward of finding food
const PUNISH_DIV = 3 // punshment for hitting stuff
const MUTATION_RATE = 0.1 // rates of fly mutation

let count = 0;
let fly, food, wall;
function setup() {
   console.log('hello');
   
   createCanvas(640, 480);
   fly = new Fly(LIFE_SPAN);
   food = new Food(width/2, 50, 30);
   wall = new Wall(width/2, height - height/3, 300, 30);
}
function draw() {
    background(3, 252, 232);
    fly.update(count);
    fly.show();
    food.show();
    wall.show();
    count ++;

    if(count == LIFE_SPAN){
        count = 0;
    }
}