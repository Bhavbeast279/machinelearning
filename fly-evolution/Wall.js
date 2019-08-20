class Wall {
    constructor() {

    }

    hitWall(flyX, flyY) {
        // Check if the flies position is within the bounds of the wall
        if (flyX > this.pos.x - this.w / 2 && flyX < this.pos.x + this.w / 2 && flyY > this.pos.y - this.h / 2 && flyY < this.pos.y + this.h / 2) {
            // If so we have hit the wall
            return true;
        } else {
            // Otherwise we haven't
            return false;
        }
    }
}