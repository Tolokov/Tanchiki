let map = `#########################
#########################
###@@@@@@@@##@@@@@@@@@###
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@@@###########@@@####
######@###@@@@@###@######
######@###########@######
######@###########@######
#########################
#########################
#########################
@@@@@@@@@@#####@@@@@@@@@@
#########################
#########################
#########################
`
const size = 32;
let cvs = document.getElementById("canvas");
let ctx = cvs.getContext("2d");

let player = new Image();
let brick = new Image();
let bullet = new Image();
let bg = new Image();


player.src = "../images/playerW.png";
brick.src = "../images/bricks.png"
bullet.src = "../images/fireW.png"
bg.src = "../images/bg.png";
let animationPlayermodel = false;
document.addEventListener('keydown', function (event) {
    if (event.code == 'KeyW') {
        user.move(0, -1);
        animationPlayermodel = !animationPlayermodel;
        if (animationPlayermodel)
            player.src = "../images/playerW.png";
        else
            player.src = "../images/playerW1.png";
    }
    if (event.code == 'KeyA') {
        user.move(-1, 0);
        animationPlayermodel = !animationPlayermodel;
        if (animationPlayermodel)
            player.src = "../images/playerA.png";
        else
            player.src = "../images/playerA1.png";
    }
    if (event.code == 'KeyS') {
        user.move(0, 1);
        animationPlayermodel = !animationPlayermodel;
        if (animationPlayermodel)
            player.src = "../images/playerS.png";
        else
            player.src = "../images/playerS1.png";
    }
    if (event.code == 'KeyD') {
        user.move(1, 0);
        animationPlayermodel = !animationPlayermodel;
        if (animationPlayermodel)
            player.src = "../images/playerD.png";
        else
            player.src = "../images/playerD1.png";
    }
    if (event.code == 'Space') {
        var bull = new projectile(user.getXpos(), user.getYpos(), user.getDirection(), 3, bullet);
    }
});
class projectile {
    constructor(Xpos, Ypos, direction, speed, sprite) {
        this._Xpos = Xpos;
        this._Ypos = Ypos;
        this._direction = direction;
        this._speed = speed;
        this._sprite = sprite;
    }
    getXpos() {
        return this._Xpos;
    }
    getYpos() {
        return this._Ypos;
    }
    getSpeed() {
        return this._speed;
    }
    setpos(newXpos, newYpos) {
        this._Xpos = newXpos;
        this._Ypos = newYpos;

    }
    move(moveX, moveY) {
        this.setpos(this.getXpos() + moveX * this.getSpeed(), this.getYpos() + moveY * this.getSpeed());
        if (moveY < 0)
            this._direction = "w";
        if (moveX < 0)
            this._direction = "a";
        if (moveY > 0)
            this._direction = "s";
        if (moveX > 0)
            this._direction = "d";
    }
    getDirection() {
        return this._direction;
        }
    fly() {
        if (this._direction == "w")
            this.move(0, -1);
        if (this._direction == "a")
            this.move(-1, 0);
        if (this._direction == "s")
            this.move(0, 1);
        if (this._direction == "d")
            this.move(1, 0);
        }
}

class tank {
    constructor(Xpos, Ypos, health, speed, sprite, direction) {
        this._Xpos = Xpos;
        this._Ypos = Ypos;
        this._health = health;
        this._speed = speed;
        this._sprite = sprite;
        this._direction = direction;
    }
    getXpos() {
        return this._Xpos;
    }
    getYpos() {
        return this._Ypos;
    }
    getSpeed() {
        return this._speed;
    }
    setpos(newXpos, newYpos) {
        this._Xpos = newXpos;
        this._Ypos = newYpos;

    }
    move(moveX, moveY) {
        this.setpos(this.getXpos() + moveX * this.getSpeed(), this.getYpos() + moveY * this.getSpeed());
        if (moveY < 0)
            this._direction = "w";
        if (moveX < 0)
            this._direction = "a";
        if (moveY > 0)
            this._direction = "s";
        if (moveX > 0)
            this._direction = "d";
    }
    getDirection() {
        return this._direction;
    }
}
let user = new tank(400 - 16, 800 - 32, 5, 8, player, "w");
let bull = new projectile(user.getXpos(), user.getYpos(), user.getDirection(), 3, bullet);
function draw() {
    //bull.move(0, -1);
    ctx.drawImage(bull._sprite, bull.getXpos(), bull.getYpos(), 32, 32)
    ctx.drawImage(bg, 0, 0);
    ctx.drawImage(user._sprite, user.getXpos(), user.getYpos());
    let i = 0, j = 0;
    for (let  char of map) {
        if (char == "@") {
            ctx.drawImage(brick, i * size, j * size);
        }
        i++;
        if (i % 26 == 0) {
            j++;
            i = 0;
        }
    }
    for (let col = 0; col < 26; col++)
        for (let row = 0; row < 26; row++)
            if (map[col * 26 + row] == "@") {
                if (user.getDirection() == "w")
                if (col * 32 + 32 > user.getYpos() && row * 32 + 32 > user.getXpos() && col * 32 < user.getYpos() && row * 32 - 32 < user.getXpos())
                        user.move(0, 1);
                if (user.getDirection() == "d")
                if (row * 32 - 32 < user.getXpos() && col * 32 - 32 < user.getYpos() && col * 32+32> user.getYpos() && row * 32 > user.getXpos())
                        user.move(-1, 0);
                if (user.getDirection() == "a")
                if (row * 32 + 32 > user.getXpos() && col * 32 - 32 < user.getYpos() && col * 32 + 32 > user.getYpos() && row * 32 < user.getXpos())
                        user.move(1, 0);
                if (user.getDirection() == "s")
                if (col * 32 - 32 < user.getYpos() && row * 32 + 32 > user.getXpos() && row * 32 - 32 < user.getXpos() && col * 32 > user.getYpos())
                    user.move(0, -1);
            }
    requestAnimationFrame(draw);
}
bg.onload = draw;
draw();
