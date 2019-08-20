class DNA {
    constructor(length) {
        this.genes = []

        for (let i = 0; i < length; i++){
            this.genes[i] = p5.Vector.random2D();
            this.genes[i].setMag(0.1); 
        }

    }
}