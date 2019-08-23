class NeuralNetwork {
    constructor(a, b, c, d) {
        
        if(a instanceof tf.Sequential) {
            this.model = a;
            this.input_nodes = b;
            this.hidden_nodes = c;
            this.output_nodes = d;
        }else{
            this.input_nodes = a;
            this.hidden_nodes = b;
            this.output_nodes = c;
            this.model = this.create_model();
        }
    }

    create_model() {
        // Unsurpervised Dense Neural Network
        const model = tf.sequential();
        const hidden = tf.layers.dense({
            units: this.hidden_nodes,
            inputShape: [this.input_nodes],
            activation: 'sigmoid'
        });
        model.add(hidden);
        const hidden2 = tf.layers.dense({
            units: this.hidden_nodes,
            activation: 'sigmoid'
        });
        model.add(hidden2);
        const output = tf.layers.dense({
            units: this.output_nodes,
            activation: 'softmax'
        });
        model.add(output);

        return model;
    }

    dispose(){
        this.model.dispose();
    }

    predict(inputs) {
        return tf.tidy(() => {
            const xs = tf.tensor2d([inputs]); // [[]] lives in this GPU

            const ys = this.model.predict(xs); // Predict using our inputs

            const outputs = ys.dataSync(); // Convert Tensor to Array

            return outputs;
        });
    }
}