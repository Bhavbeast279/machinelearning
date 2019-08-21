class DNA {
    constructor(length) {
        this.genes = []

        for (let i = 0; i < length; i++){
            this.genes[i] = p5.Vector.random2D();
            this.genes[i].setMag(0.1); 
        }

    }

    generateMergedDNA(mutationRate, parentA, parentB){

        let tempGenes = [];

        for(let i = 0; i < parentA.dna.genes.length; i++){

            let p = int(random());

            tempGenes.push(p ? parentA.dna.genes[i] : parentB.dna.genes[i]);

            let shouldMutate = random();

            if (mutationRate > shouldMutate){
                tempGenes[i] = p5.Vector.random2D();
                tempGenes[i].setMag(0.1);
            }
        }

        this.genes = tempGenes;
    }
}